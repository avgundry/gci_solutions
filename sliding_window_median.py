from typing import List

import heapq

class Solution:
    def __init__(self):
        # stores smallest half of numbers; len always >= len minheap
        self.max_heap = []
        # stores largest half of numbers
        self.min_heap = []

    def _median(self):
        # if len(max_heap) > len(min_heap), we have an odd amnt of
        # numbers, so only return the middle value
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # otherwise, return average of two vals
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        
    def _insert_num(self, num):
        if len(self.max_heap) == 0:
            # always insert into max_heap first
            heapq.heappush(self.max_heap, -num)
        elif len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
        elif len(self.min_heap) < len(self.max_heap):
            heapq.heappush(self.min_heap, num)
        else:
            print("SOMETHING WRONG")

        self._rebalance()


    def _rebalance(self):
        if len(self.min_heap) == 0 or self.max_heap[0] <= self.min_heap[0]:
            # then they're already balanced.
            return
        else:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            else:
                temp = heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, -temp)
    #     # if already balanced, just do nothing.
    #     if len(self.max_heap) == len(self.min_heap) or len(self.max_heap) == 0:
    #         return


    def _build_heap(self, start, win, nums):
        for i in range(start, start + win):
            self._insert_num(nums[i])
        
        return


    #
        

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # hm. brute force method is just to rebuild the heaps every 
        # single time...
        medians = []
        n = len(nums)
        for i in range(n - k):
            self._build_heap(i, k, nums)
            medians.append(self._median())
            self.min_heap = []
            self.max_heap = []

        return medians

if __name__ == "__main__":
    s = Solution()
    print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))