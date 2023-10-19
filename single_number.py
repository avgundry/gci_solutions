from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        x1 = nums[0]
        for i in range(1, n):
            x1 = x1 ^ nums[i]

        return x1
