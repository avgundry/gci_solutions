import heapq


class MedianFinder:

    def __init__(self):
        # instantiate min- and max-heaps
        self.min_heap  = []
        self.max_heap  = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or self.max_heap[0] < num:
            self._maxHeapPush(num)
        else:
            self._minHeapPush(num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            # push biggest num from max_heap onto min_heap
            self.
        
        
    def findMedian(self) -> float:
        return self.median

    def _minHeapPop(self):
        num = self.min_heap[0]

        if len(self.min_heap) == 1:
            self.min_heap = []
        else:
            self.min_heap[0] = self.min_heap[-1]
            del self.min_heap[-1]

            # then bubble down...sigh



        return num

    def _minHeapPush(self, num):
        # append to the end of the list
        self.min_heap.append(num)
        # set curr to be the end of the list, i.e. the number we just appended
        curr = len(self.min_heap) - 1

        # while the invariant is not maintained, bubble the smallest number up 
        # uses inverted floor division to mimic ceil without use of math module
        par = -(curr // -2) - 1
        while self.min_heap[curr] < self.min_heap[par] and par != -1:
            # swap until inserted num is in correct spot
            temp = self.min_heap[curr]
            self.min_heap[curr] = self.min_heap[par]
            self.min_heap[par] = temp
            curr = par
            par = -(curr // -2) - 1

        self.min_len += 1
        # return the new len of min_heap
        return self.min_len 


    def _maxHeapPush(self, num):
        # similar to above, append to end of array and bubble up, simply with
        # different direction.

        self.max_heap.append(num)
        curr = len(self.max_heap) - 1

        # while the invariant is not maintained, bubble up
        # again uses inverted floor division to mimic ceil without use of math 
        # module
        par = -(curr // -2) - 1
        while self.max_heap[curr] > self.max_heap[par] and par != -1:
            # swap until inserted num is in correct spot
            temp = self.max_heap[curr]
            self.max_heap[curr] = self.max_heap[par]
            self.max_heap[par] = temp
            curr = par
            par = -(curr // -2) - 1
        
        self.max_len += 1
        # return the new len of min_heap
        return self.max_len 

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