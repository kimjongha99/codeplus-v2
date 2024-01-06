#보석과 돌
#돌에있는 보석의 개수가 몇개인지 새는것


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count =0
        for s in stones:
            if s in jewels:
                count+=1

        return count


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    sol = Solution()
    result = sol.numJewelsInStones(jewels , stones)
    print("Output:", result)
