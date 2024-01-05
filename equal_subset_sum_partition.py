from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # basically, must find a subset such that sum(subset) = sum(nums) // 2
        # If we can't cleanly divide sum(nums) by 2 it clearly can't exist
        s = sum(nums)
        if s % 2 != 0:
            return False

        targ = s // 2
        # Ah! Optimize even further by just having a 1d array of
        # whether we can reach given targ with the numbers so far.
        dp = [False for i in range(targ + 1)]
        # Can always reach 0.
        dp[0] = True
        
        # Go backwards to avoid double-counting self
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(targ, -1, -1):
                if curr <= j:
                    dp[j] = dp[j - curr] or dp[j]

        # By the end of our loop, return whether we can reach the targ
        # or not.
        return dp[targ]


if __name__ == "__main__":
    s = Solution()
    # print(s.canPartition([1, 2, 3])) # true
    # print(s.canPartition([1,2,3,4,5,6,7])) # true
    print(s.canPartition([1,2,5])) # false
    print(s.canPartition([1, 5, 11, 5])) # true
    print(s.canPartition([1,2,3,5])) # false
