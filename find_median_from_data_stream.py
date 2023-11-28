import heapq


class MedianFinder:
    def __init__(self):
        # contains the largest half of the numbers
        self.min_heap = []
        # contains the smallest half of the numbers
        # forgot I have to negate everything in the max heap. UGH
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # make max heap always larger than min?
        # or...
        if len(self.max_heap) == 0 or -num > self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # then rebalance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            # if max heap is more than 1 greater than min heap,
            # pop one off it and move to min heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))


    def findMedian(self) -> float:
        print(f"max_heap: {self.max_heap} min_heap: {self.min_heap}")
        # only occurs in the case we have a single number added
        # if len(self.min_heap) == 0:
        #     return -self.max_heap[0]
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2

        return -self.max_heap[0]



# param_2 = obj.findMedian()
if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.findMedian()
    obj.addNum(3)
    obj.findMedian()
    # obj.addNum(1)
    # param_2 = obj.findMedian()
    # print(param_2)
    # obj2 = MedianFinder()
    # obj2.addNum(1)
    # obj2.addNum(2)
    # obj2.addNum(5)
    # param_3 = obj2.findMedian()
    print(param_3)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()