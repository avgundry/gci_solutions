# seeing if it's diff in Python
import collections
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)
        # I'm so incredibly stupid. god I've wasted like 30 mins on this

    def add(self, val: int) -> int:
        if len(self.minHeap) > self.k - 1:
            heapq.heappushpop(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)

        return self.minHeap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    obj = KthLargest(3, [4,5,8,2])
    param_1 = obj.add(3)
    param_2 = obj.add(5)
    param_3 = obj.add(10)
    param_4 = obj.add(9)
    param_5 = obj.add(4)
    print(param_1)
    print(param_2)