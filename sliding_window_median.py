from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if nums == []:
            return nums

        medians = []

        # build initial window
        window = nums[:k]
        medians = []

        left = 0
        right = k
        while right < len(nums):
            # append current median
            if k % 2 == 0:
                # even case we average the middle two numbers
                medians.add((window[k // 2]) + window[k // 2 - 1])
            else:
                # otherwise just add the middle num
                medians.add(window[k // 2])

            # remove old left element from window
            window.remove(nums[left])

            # add right element
            
            

        # # data structure that preserves ordering..but how
        # # use two heaps??? 
        # window = []

        # # begin by building sorted list of initial k-length subarray
        # for i in range(k):
        #     pass
            

        # # loop through array one at a time, starting at end of initial window
        # for i in range(k - 1, len(nums)):
        #     pass
        #     # add current median to list of medians
        #     # remove old element from window

        #     # add new element to list in sorted order 

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    print(s.medianSlidingWindow(nums, 3))
