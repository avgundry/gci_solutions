import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        if k > len(nums) or nums == None or nums == []:
            return []

        # contains largest half of nums in window
        min_heap = []
        # contains smallest half of nums in window
        max_heap = []

        

        # Brute force naive solution - simply sort window every time
        # O(kn^2) time, O(k) space
        # Appears to work but FAILS on large inputs due to egregious runtime
        # for i in range(len(nums) - k + 1):
        #     window = nums[i:i+k]
        #     if k % 2 == 0:
        #         # if even we have to divide middle two
        #         medians.append(sorted(window)[len(window) // 2]/2 + window[len(window) // 2 + 1]/2)
        #     else:
        #         # otherwise just append middle
        #         medians.append(sorted(window)[len(window) // 2])

        # return medians
        
if __name__ == "__main__":
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    print(s.medianSlidingWindow(nums, 3))
