class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        opener = "{(["
        stack =[]

        for char in s:
            if char in opener:
                stack.append(char)
                print(stack)
            else:
                if not stack:
                    return False
                top = stack.pop()
                print(top)
                if pair[char] != top:
                    return False

        return not stack


solution = Solution()
input_str = "()"
result = solution.isValid(input_str)

print("Input:", input_str)
print("Is valid:", result)