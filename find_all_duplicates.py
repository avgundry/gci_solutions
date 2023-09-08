from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # index
        i = 0

        while i < len(nums):
            #print(f"current i: {i}  current nums: {nums}")
            # current num we're on
            num = abs(nums[i])
            # if num in correct position, increment i
            if num == i + 1:
                i += 1
            else:
                # otherwise we try to swap
                if nums[num - 1] == num:
                    # if there's already the correct number in the position
                    # we want, that means this one is a duplicate, so mark it
                    # as negative and increment i. MUST use abs to avoid
                    # repeatedly negating a number and making it pos again.
                    nums[i] = -abs(nums[i])
                    i += 1
                else:
                    # if not, we swap, and don't increment i
                    nums[num - 1], nums[i] = num, nums[num-1]
        
        #print(f"final nums: {nums}")
        # keeps track of where last space we swapped is
        pos = 0
        i = len(nums) - 1

        while i > pos - 1:
            if nums[i] > 0:
                # it's positive so we pop it, which is O(1) time since it's
                # at the end of the list.
                nums.pop()
                i -= 1
            else:
                # if it's negative, we must swap it with a positive number.
                # to do so we swap with pos, which keeps track of what spaces
                # are used by array and "safe", i.e. holding negative numbers
                nums[i], nums[pos] = nums[pos], nums[i]
                # we also convert it to positive for when we return the list.
                nums[pos] = abs(nums[pos])
                pos += 1
        
        return nums
        
        



if __name__ == "__main__":
    s1 = Solution()
    print(s1.findDuplicates([4,3,2,7,8,2,3,1]))
    print(s1.findDuplicates([1,1,2]))
    print(s1.findDuplicates([1]))