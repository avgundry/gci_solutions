from typing import List

# Given an array of integers nums and an integer k, return the number of 
# contiguous subarrays where the product of all the elements in the 
# subarray is strictly less than k.
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        num = left = 0 
        P = 1
        for right in range(len(nums)):
            P *= nums[right]

            while (right >= left and P >= k):
                P //= nums[left]
                left += 1
            
            num += right - left + 1

        return num            


if __name__ == "__main__":
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
    print(s.numSubarrayProductLessThanK([1,2,3], 0))