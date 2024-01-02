from heapq import *
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [sorted(nums)[-i] for i in range(1, k + 1)]
        heapify(self.nums)
        

    def add(self, val: int) -> int:
        if val > self.nums[0]:
            heappushpop(self.nums, val)
        
        return self.nums[0]

    """
    Two-heap method.
    """
    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = []
    #     self.klargest = nums
    #     heapify(self.klargest)
    #     while len(self.klargest) > k:
    #         self.nums.append(heappop(self.klargest))

    # def add(self, val: int) -> int:
    #     if len(self.klargest) < self.k:
    #         heappush(self.klargest, val)
    #     elif val > self.klargest[0]:
    #         self.nums.append(heappushpop(self.klargest, val))
    #     else:
    #         self.nums.append(val)
    #         heappush(self.nums, val)

    #     return self.klargest[0]


    """
    Brute force method. Times out for large inputs.
    """
    # def __init__(self, k: int, nums: List[int]):
    #     self.k: int = k
    #     # This really feels like a two-heap problem, honestly. Hm.
    #     # Or at least it could be sped up a lot by doing so...anyways.
    #     # Trying with one heap first.

    #     self.nums: List[int] = nums
    #     # Takes O(len(nums)) time.
    #     heapify(self.nums)
        

    # def add(self, val: int) -> int:
    #     # Brute force method is to add to the heap, then use heapq's
    #     # nlargest to get the kth largest element.
    #     heappush(self.nums, val)
        
    #     if self.k > 100:
    #         return sorted(self.nums)[-self.k]
    #     else:
    #         return nlargest(self.k, self.nums)[-1]

if __name__ == "__main__":
    s = KthLargest(3, [4, 5, 8, 2])
    print(s.add(3))
    print(s.add(5))
    print(s.add(10))
    print(s.add(9))
    print(s.add(4))

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)