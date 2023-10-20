from collections import deque
from typing import List
from heapq import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # seems solvable without sorting in O(n) time IF using O(k) memory...
        # hm no it would be O(nk) time in that case...
        if len(nums) == 1:
            return nums[0]

        # Brute force solution first, where we keep a sorted array of k largest
        k_largest = []
        heappush(k_largest, nums[0])
        for i in range(1, len(nums)):
            curr = nums[i]
            if len(k_largest) < k:
                heappush(k_largest, curr)
            else:
                if curr > k_largest[0]:
                    heappop(k_largest)
                    heappush(k_largest, curr)
        
        return heappop(k_largest)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
