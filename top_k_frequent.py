import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # approach optimized for memory
        # uses only O(n) with built in collections.Counter
        c = collections.Counter(nums)

        return [x[0] for x in c.most_common(k)]
        # Slightly less naive solution is to keep some sort of heap...are there heap maps in Python??
        # hm. once again turn into a dictionary....
        # this is suggested in GCI's solution. 
        # num_dict = dict()
        # for num in nums:
        #     num_dict[num] = num_dict.setdefault(num, 0) + 1

        # minHeap = []
        # for num, frequency in num_dict.items():
        #     heapq.heappush(minHeap, (frequency, num))
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)

        # topNumbers = []
        # while minHeap:
        #     topNumbers.append(heapq.heappop(minHeap)[1])

        # return topNumbers


        # Hm. Naive solution is to store in a map, then return highest values of map.
        # Try that first.

        # num_dict = dict()

        # for num in nums:
        #     num_dict[num] = num_dict.setdefault(num, 0) + 1

        # return [x[0] for x in sorted(num_dict.items(), key=lambda x:x[1], reverse=True)[:k]]

if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))