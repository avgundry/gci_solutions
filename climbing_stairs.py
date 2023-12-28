from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        # how many distinct ways there are with index + 1 steps 
        # remaining. so memo[0] = 1, memo[1] = 2, etc.
        memo = [-1 for _ in range(n)]
        self.recurseStairs(n, memo)
        print(memo)
        return memo[-1]

    def recurseStairs(self, n: int, memo: List[int]) -> None:
        if n == 0 or n == 1:
            memo[n - 1] = 1
        elif memo[n - 1] == -1:
            memo[n - 1] = self.recurseStairs(n - 1, memo) + self.recurseStairs(n - 2, memo)
        return memo[n - 1]

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
