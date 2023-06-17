"""
https://leetcode.com/problems/missing-number/
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # variety of ways to do this, but since it's in the "cyclic sort" category I suppose I should do that.

        # O(n) runtime complexity, O(1) space complexity using cyclic sort

        # TODO
        # i = 0 
        # num_len = len(nums)

        # # cyclic sort first
        # while i < num_len:
        #     num = nums[i]
        #     if num != i:
        #         nums[num], nums[i] = nums[i], nums[num]
        #     else:
        #         i += 1

        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i


        # mathematical approach
        return int((len(nums)**2 + len(nums))/2 - sum(nums))
            
if __name__ == "__main__":
    s = Solution()
    assert s.missingNumber([3,0,1]) == 2