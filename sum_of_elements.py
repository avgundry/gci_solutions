# Problem Statement: Given an array, find the sum of all numbers between the
# K1’th and K2’th smallest elements of that array.

import heapq 

class Solution:
    def find_sum_of_elements(self, nums, k1, k2):
        """
        O(Nlog(K2)) time optimal solution
        Taken from text
        """
        max_heap = []

        # keep smallest k2 numbers on the max_heap
        for i in range(len(nums)):
            if i < k2 - 1:
                heapq.heappush(max_heap, -nums[i])
            elif nums[i] < -max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -nums[i])

        total = 0
        for _ in range(k2 - k1 - 1):
            total += -heapq.heappop(max_heap)

        return total




        """
        O(Nlog(N)) time suboptimal solution
        """
        # first we actually have to find the k1th and k2th smallest elements of
        # the given array.
        # to do so, we can begin by sorting...a min heap will serve us well
        # if allowed to heapify the passed nums, O(1) space
        # else we'd have to make it ourselves, O(n) space.

        # O(n) time.
        # heapq.heapify(nums)

        # i = 0
        # while i < k1:
        #     print(f"popping {heapq.heappop(nums)}")
        #     i += 1

        # total = 0
        # while i < k2 - 1:
        #     x = heapq.heappop(nums)
        #     total += x
        #     print(f"adding {x}: new total is {total}")
        #     i += 1

        # return total


if __name__ == "__main__":
    s = Solution()
    print(s.find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))
    print(s.find_sum_of_elements([3, 5, 8, 7], 1, 4))