# doing this in Python since prototyping recursion in C++ is more trouble than
# it's worth

import copy
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        sum2 = self.recurseStone(int(total / 2), stones, len(stones))
        return total - 2*sum2

    def recurseStone(self, capacity, stones, n):
        dp = [[-1 for i in range(int(capacity) + 1)] for j in range(n + 1)]
        return self.recurseStones(capacity, stones, n, dp)

    def recurseStones(self, capacity, stones, n, dp):
        if (n == 0 or capacity == 0):
            return 0;

        if dp[n][capacity] != -1:
            return dp[n][capacity]

        if stones[n - 1] <= capacity:
            dp[n][capacity] = max(
                stones[n - 1] + self.recurseStones(capacity - stones[n - 1], stones, n - 1, dp),
                self.recurseStones(capacity, stones, n - 1, dp)
            )
        else: 
            dp[n][capacity] = self.recurseStones(capacity, stones, n - 1, dp)
        return dp[n][capacity]

        
if __name__ == "__main__":
    s = Solution()
    print("OUTCOME: ")
    print(s.lastStoneWeightII([2,7,4,1,8,1]))
    print(s.lastStoneWeightII([31,26,33,21,40]))
