"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(n) runtime, O(1) space. Could definitely stand to be optimized a ton, though
        i = 0
        n = len(nums)

        while i < n:
            # out of place so must swap
            j = nums[i]
            if j == None:
                i += 1
            elif j != i + 1:
                # if we already have something sorted to that location, set the current
                # index to be None, for later.
                if nums[j - 1] == j:
                     nums[i] = None
                else:
                    nums[j - 1], nums[i] = nums[i], nums[j - 1]
            else:
                i += 1
        
        return [i + 1 for i in range(n) if nums[i] != i + 1]
    
if __name__ == "__main__":
    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    assert s1.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
    assert s2.findDisappearedNumbers([1,1]) == [2]