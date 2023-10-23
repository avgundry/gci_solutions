from typing import List
from heapq import *


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # the naive way of doing this seems functionally identical to the previous problem.
        maxHeap = []

        for i in range(k):
            heappush(maxHeap, points[i])

        for i in range(k, len(points)):
            if points[i][0]*points[i][0] + points[i][1] * points[i][1] < maxHeap[0][0] * maxHeap[0][0] + maxHeap[0][1] * maxHeap[0][1]:
                heappop(maxHeap)
                heappush(maxHeap, points[i])

        return list(maxHeap)

if __name__ == "__main__":
    s = Solution()
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))