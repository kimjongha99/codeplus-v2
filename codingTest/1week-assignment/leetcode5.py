class Solution:
    # 주어진 문자열 s에서 가장 긴 팰린드롬 부분 문자열을 찾는 함수 정의
    def longestPalindrome(self, s: str) -> str:
        # 빈 문자열이거나 길이가 0인 경우 빈 문자열 반환
        if not s or len(s) == 0:
            return ""

        # 시작점과 끝점 초기화
        start, end = 0, 0

        # 문자열의 각 문자에 대하여 반복
        for i in range(len(s)):
            # 홀수 길이 팰린드롬을 찾기 위한 확장
            len1 = self.expandAroundCenter(s, i, i)
            # 짝수 길이 팰린드롬을 찾기 위한 확장
            len2 = self.expandAroundCenter(s, i, i + 1)
            # 홀수, 짝수 길이 팰린드롬 중 최대 길이 계산
            max_len = max(len1, len2)

            # 최대 길이 팰린드롬의 시작점과 끝점 갱신
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # 가장 긴 팰린드롬 부분 문자열 반환
        return s[start:end + 1]

    # 주어진 문자열에서 중심점을 기준으로 팰린드롬의 길이를 계산하는 함수
    def expandAroundCenter(self, s, left, right):
        # 왼쪽, 오른쪽 포인터 초기화
        L, R = left, right

        # 왼쪽과 오른쪽 문자가 같고, 포인터가 문자열 범위 안에 있는 동안 반복
        while L >= 0 and R < len(s) and s[L] == s[R]:
            # 포인터를 왼쪽과 오른쪽으로 이동
            L -= 1
            R += 1

        # 팰린드롬의 길이 반환
        return R - L - 1

# 예시 사용
sol = Solution()
print(sol.longestPalindrome("babad"))  # 출력: "bab" 또는 "aba"
print(sol.longestPalindrome("cbbd"))   # 출력: "bb"
