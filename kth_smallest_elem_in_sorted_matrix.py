from heapq import *
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # First, we just determine where the kth smallest element is.
        # This...seems a little trivial if they're sorted?
        # Oh, but they are NOT sorted overall - only relative to each row/col.
        # That does make this significantly harder.

        # Oh, I'm being silly.
        # This is just merging sorted lists, at its most naive, and then
        # getting the kth smallest element. Will be O(nlog(k)) time.

        min_heap = []
        n = len(matrix)
        # element i is index we're at for ith sublist
        inds = [1 for _ in range(n)]
        sorted_elems = []
        for i in range(n):
            heappush(min_heap, [matrix[i][0], i])

        # extremely naive method: merge all n sorted rows together
        # O(nlog(n)) time??
        # no, O(n^2log(n)). Hm.
        # Rewrite to only do up to the kth smallest element.
        # Then, we have O(klog(n)) time
        while min_heap and len(sorted_elems) < k:
            ind = min_heap[0][1]
            sorted_elems.append(heappop(min_heap)[0])
            if inds[ind] < n:
                heappush(min_heap, [matrix[ind][inds[ind]], ind])
            inds[ind] += 1

        return sorted_elems[-1]


        # """
        # Maybe(?) optimize brute force attempt
        # """
        # # to optimize the below, we can instead...hm.
        # # make a max heap instead of a min heap.
        # # if the first elem in a row is >= the top of the heap, then we know
        # # that we have all the smallest elements up until that point.
        # # so just store k elements, and then up until that point occurs
        # max_heap = []
        # n = len(matrix)
        # added = 0
        # found = False
        # i = 0
        # # so this is...what. O(n^2log(n^2)) theoretically still right??
        # # :\ 
        # while (added < k or found == False) and i < n:
        #     if added >= k and matrix[i][0] >= -max_heap[0]:
        #         found = True
        #     for j in range(n):
        #         heappush(max_heap, -matrix[i][j])
        #     added += n
        #     i += 1

        # min_heap = []
        # for num in max_heap:
        #     heappush(min_heap, -num)

        # # pop until we get to the smallest num
        # for _ in range(k - 1):
        #     heappop(min_heap)

        # return heappop(min_heap)
        



        # """
        # Brute force attempt first:
        # sort all elements in the matrix one by one.
        # """

        # # Now...how do we optimize it...?

        # min_heap = []
        # # O(n)
        # for i in range(len(matrix)):
        #     # times O(n)
        #     for j in range(len(matrix)):
        #         # times log(n^2)
        #         heappush(min_heap, matrix[i][j])
        # # So the above is O(n^2log(n^2)) total - very poor.

        # for _ in range(k - 1):
        #     heappop(min_heap)

        # return heappop(min_heap)


        # Hm. If k > (n^2) / 2...then we instead want to find the 
        # (n^2 - k)th largest number.

        # or just search backwards to begin with? fk, no, idk.
        # UGH. in the given example...we know the 8th smallest num
        # is the 2nd largest num. Ok. So we EITHER search in the same row,
        # or the row below it. We couldn't have it be in the second row below it.

        # n = len(matrix)
        # if k > (n^2) / 2:
        #     # search for n^2 - kth largest num
        #     # can at most be n^2 - k rows beneath?
        #     for i in range(n - (n**2 - k), n):
        #         row = matrix[i]
        #         for 

if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))