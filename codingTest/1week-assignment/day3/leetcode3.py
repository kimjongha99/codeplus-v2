#문제 이해하기가 힘들었다
#반복되는 문자열 중 가장 긴것 문자열 s가 주어졌을 때, 반복되지 않는 문자로 이뤄진 가장 긴 부분문자열의 길이를 리턴하세요!
import collections


# abcabcaa 이면 a시작 abc , b 시작 bcab , c 시작 abc


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = collections.deque()
        max_len = 0

        for char in s:
            if char not in q:
                q.append(char)
            else:
                index = q.index(char)  # 큐가비어있지않다면 큐에서 char를 찾는다
                for j in range(index+1):
                    q.popleft()
                q.append(char)

            max_len = max(max_len,len(q))
        return max_len

if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print("Output:", result)
