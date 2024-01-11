from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]
        stack = [([],nums)]
        print(stack)
        while stack:
            path, remaining = stack.pop()
            print(path,remaining)
            if not remaining:
                result.append(path)
            else:
                for i in range(len(remaining)):
                    next_path = path + [remaining[i]]
                    next_remaining = remaining[:i] + remaining[i + 1:]
                    stack.append((next_path, next_remaining))

        return result


sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))