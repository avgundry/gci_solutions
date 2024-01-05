# "Target sum" on Leetcode.

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Hmmmm.
        # Let's say we have nums [a, b, c], target [z].
        # Let's have our base case be one number. We want to get the
        # possible outputs. The possible outputs from c are c, -c...
        # Hm. Or we can split this into two? Then do 0/1 knapsack?
        # Yeah, I think so. Let's have our target be... target - sum(nums).
        # So if we have target 3 and nums [1,2,1,1], our new target 
        # becomes 3 - (1+2+1+1) = 3 - 5 = -2.
        # Thus we want to 'include', i.e. negate, numbers until we get
        # to 0. So...no, that doesn't make sense. Hm. We want to activate 3...hm.


        # Ok do what I originally said. We have c, -c.
        # Recursively do that for b too: so b has b + c, b - c, -b + c,
        # -b - c. Then so on for a, any othe rnumbers etc. 
        # Hmm. Ok, is another way to think about it that we need to
        # find sum(nums) /2 - target? Sure.

        # Then...memoize it.
        # Do I just have a memo where each index contains all possible
        # values from that index onwards...? That'd mean a set and a
        # LOT of memory usage. I guess try that for now.

        """0/1 Knapsack method"""
        # Let P be positive nums, N be ones we'll mark negative.We need
        # sum(P) - sum(N) = target
        # -> sum(P) - sum(N) + sum(P) + sum(N) = target + sum(P) + sum(N)
        # -> 2sum(P) = target + sum(nums)
        # -> sum(P) = (target + sum(nums)) // 2
        # Ok. So we turn this into a 0/1 knapsack problem this way...
        # I was so close. Regardless, we have this and it's just a 
        # standard DP solution now.

        s: int = sum(nums)
        # would never be able to reach target, either because we can't
        # sum up enough or it's not divisible by 2, as shown above
        if s < target or -s > -target or (s + target) % 2 != 0:
            return 0

        dp: List[int] = [0 for _ in range((target + s) // 2 + 1)]
        dp[0] = 1 # why???

        for num in nums:
            for i in range(len(dp) - 1, -1, -1):
                dp[i] += dp[i - num] 


        return dp[len(dp) - 1]

        

        

        """Bad memoization"""
    """     memo = [[] for _ in range(len(nums))]

        self.recurse(nums, 0, memo)
        total = 0
        for val in memo[0]:
            total += (val == target)

        return total

    def recurse(self, nums, ind, memo):
        # If at the end of the list we just memoize & return.
        if ind == len(nums) - 1:
            memo[ind].append(-nums[ind])
            memo[ind].append(nums[ind])
            return
        
        # if we need to, fill in the memo of following indices first 
        if not memo[ind+1]:
            self.recurse(nums, ind + 1, memo)

        # Fill out the current index's memo
        curr = memo[ind+1]
        for val in curr:
            memo[ind].append(nums[ind] + val)
            memo[ind].append(-nums[ind] + val)

        return
 """



"""Brute force recursive method."""
"""     return self.recurse(nums, 0, target, 0)



        pass
        
    def recurse(self, nums, ind, target, curr):
        if ind == len(nums) - 1:
            return (curr + nums[ind] == target) + (curr - nums[ind] == target)
        else:
            return self.recurse(nums, ind + 1, target, curr + nums[ind]) \
                    + self.recurse(nums, ind + 1, target, curr - nums[ind])
 """

if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays([1,1,1,1,1], 3))
    print(s.findTargetSumWays([1], 1))
    print(s.findTargetSumWays([1, 2, 1, 1], 1))
    print(s.findTargetSumWays([1, 2, 1, 1], 2))
    print(s.findTargetSumWays([1, 2, 1, 1], 3))
    print(s.findTargetSumWays([1, 2, 1, 1], 4))
    print(s.findTargetSumWays([1, 2, 1, 1], 5))
    print(s.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 132))