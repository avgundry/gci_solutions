import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        # it is INSANE that the standard solution for a max heap is to negate
        # every number in the max heap and use heapq. 
        # that's nuts
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -num)
        elif num < self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # then rebalance
        if len(self.max_heap) > len(self.min_heap) + 1:
            # we're fine with the max heap having the extra val in the case of
            # having an odd number of values
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]



# param_2 = obj.findMedian()
if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    param_2 = obj.findMedian()
    print(param_2)
    obj2 = MedianFinder()
    obj2.addNum(1)
    obj2.addNum(2)
    obj2.addNum(5)
    param_3 = obj2.findMedian()
    print(param_3)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()