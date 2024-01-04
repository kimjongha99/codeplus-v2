#정수 온도 배열이 일일 기온을 나타내는 경우,
# 답변[i]가 i번째 날 이후 더 따뜻한 기온을 얻기 위해 기다려야 하는 일수인 배열 답변을 반환합니다.
# 이것이 가능한 미래의 날이 없다면 대신 대답[i] == 0을 유지하십시오.
from typing import List



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n # 배열을 온도 개수만 큼 초기화
        stack = [] # 스택을 만들어준다.

        for i in range(n):
            # 스택이 비어있지않고 현재 온도가 스택의 제일 위 온도보다 크면 돈다.
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i-prev_index

            stack.append(i)

        return result

# Test the function
if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution()
    result = sol.dailyTemperatures(temperatures)
    print("Output:", result)






        # n = len(temperatures)
        #
        #
        # result= [0]*n
        #
        #
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break
        # return result
        # n = len(temperatures)
        #
        #
        # result= [0]*n
        #
        #
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break
        # return result
