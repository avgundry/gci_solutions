from typing import List

# Given an array of integers nums and an integer k, return the number of 
# contiguous subarrays where the product of all the elements in the 
# subarray is strictly less than k.
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Key is the length of array; val is how many arrays of that length we've found.
        # Will always be the maximum length for a valid array. Used to find subarrays of all arrays of
        # length n.
        left = right = 0
        # number of valid arrays
        num_arrs = 0

        # while left in range(len(nums)):
        #     while (curr_prod < k and right < len(nums) - 1):
        #         right += 1
        #         curr_prod *= nums[right]
        #     # once we've reached the maximum length, add the arr and all subarrs to our total
        #     num_arrs += ((right-left)**2 + (right - left))/2
        #     # above formula is equivalent to sum from k=1 to n of k
        #     left += 1
        #     # Hm. is there no better way than O(n)^2???
        
        # I guess O(n)^2 is best for now...there *must* be improvements to this, though.
        for left in range(len(nums)):
            curr = 1
            for right in range(left, len(nums)):
                curr *= nums[right]
                if curr < k:
                    num_arrs += 1
                else:
                    break

        return num_arrs
            

            






if __name__ == "__main__":
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
    print(s.numSubarrayProductLessThanK([1,2,3], 0))