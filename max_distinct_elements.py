# closest leetcode problem to this is "Least Number of Unique Integers After
# K Removals".

from typing import List
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        not great runtime or memory
        """
        min_heap = []
        freq_table = dict()

        # first make frequency table of the array values
        for num in arr:
            freq_table[num] = freq_table.get(num, 0) + 1

        for key, val in freq_table.items():
            heapq.heappush(min_heap, [val, key])


        dels = 0
        while dels < k and min_heap:
            if min_heap[0][0] == 1:
                del freq_table[heapq.heappop(min_heap)[1]]
            else:
                min_heap[0][0] -= 1
            dels += 1

        return len(freq_table.keys())


        


if __name__ == "__main__":
    s = Solution()
    arr1 = [5,5,4]
    print(s.findLeastNumOfUniqueInts(arr1, 1))
