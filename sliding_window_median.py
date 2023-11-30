import heapq
from typing import List


class Solution:
    def __init__(self):
        # contains largest half of nums in window
        self.min_heap = []
        # contains smallest half of nums in window
        self.max_heap = []

    def rebalance(self):
        # rebalance
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


    def addNum(self, num):
        if len(self.max_heap) == 0 or -num > self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        # nums[i] is smaller than the largest number in self.max_heap, so is in
        # smallest half of numbers
        else:
            heapq.heappush(self.min_heap, num)

        self.rebalance()

    def median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        if k > len(nums) or nums == None or nums == []:
            return []

        # to begin, fill the heaps with the first k numbers
        for i in range(k):
            self.addNum(nums[i])

        # add the first median
        medians.append(self.median())

        # then slide the window. 
        for i in range(k + 1, len(nums) + 1):
            # for testing purposes, add the window over again each time
            # obv horrible runtime
            self.min_heap.clear()
            self.max_heap.clear()
            for j in range(i - k, i):
                self.addNum(nums[j])
            medians.append(self.median())
            # # remove the number at i from the heap...hm.
            # # is this O(n)? yes...so this will be O(n^2). Hm
            # if -nums[i - k] in self.max_heap:
            #     self.max_heap.remove(-nums[i - k])
            # else:
            #     self.min_heap.remove(nums[i - k])
            # self.rebalance()

            # # then add number at right side of window
            # self.addNum(nums[i])

            # # and finally, add the median of this window to the arr
            # medians.append(self.median())
        

        print(self.max_heap, self.min_heap)
        print(f"current median: {self.median()}")
        return medians
        
if __name__ == "__main__":
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    print(f"medians for {nums} with window size {3}:\n {s.medianSlidingWindow(nums, 3)}")
