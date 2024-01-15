from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return 0

        memo = dict()
        return self.recurse(nums, target, len(nums) - 1, 0, memo)

    def recurse(self, nums, targ, ind, curr, memo):
        if (ind, curr) in memo:
            return memo[(ind, curr)]
        if ind < 0 and curr == targ:
            return 1
        elif ind < 0:
            return 0

        pos = self.recurse(nums, targ, ind - 1, curr + nums[ind], memo)
        neg = self.recurse(nums, targ, ind - 1, curr - nums[ind], memo)

        # OHHH I see.
        memo[(ind, curr)] = pos + neg
        return memo[(ind, curr)]

if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
    print(s.findTargetSumWays([1], target = 1))
        