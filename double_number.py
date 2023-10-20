# "Single Number III" on leetcode

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x1 = x2 = nums[0]
        x2 = x2 ^ nums[0]
        for i in range(1, len(nums)):
            x1 = x1 ^ nums[i]
            x2 = x1 ^ nums[i]
        
        print(x1)
        print(x2)
        print(x1 ^ x2)
        

        return [x1, x1 ^ x2]

        
if __name__ == "__main__":
    s = Solution()
    s.singleNumber([1,2,1,3,2,5])
    s.singleNumber([-1, 0])
    s.singleNumber([1, 0])