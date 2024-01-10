class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        stack = [(0, "")]
        result = []

        while stack:
            index, path = stack.pop()
            if len(path) == len(digits):
                result.append(path)

            else:
                for i in phone_map[digits[index]]:
                    stack.append((index + 1, path + i))

        return result
