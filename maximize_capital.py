"""'IPO', p502, on leetcode."""

from typing import List

import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # hmmm
        # how is this a two heap thing???
        # don't get it...
        # brute force method: for each step out of k total projects, 
        # choose the most profitable project at that step.

        # maybe have a max heap for projects that have less than a 
        # certain amnt of capital?
        # and then...yeah something like that. another heap containing
        # project which require more capital than we currently have?

        # If we...add all projects which require less capital than we 
        # currently have to a heap, I believe that will be O(nlogn)
        # initially. We want it to be a max_heap based on profit, so we
        # can choose the most profitable thing at each step. Do that
        # first.
        max_heap = []
        # same len for profits and capital
        n = len(capital)
        # use this to track projects we cannot currently do
        # min_heap organized by capital requirements
        min_heap = []

        for i in range(n):
            if capital[i] <= w:
                # then we have enough capital to complete the project.
                heapq.heappush(max_heap, (-profits[i], i))
            else:
                heapq.heappush(min_heap, (capital[i], i))
            # otherwise...push to our other heap?

        # then for k projects...choose the best, add to capital, 
        # iterate
        for _ in range(k): # O(k)
            # only occurs if we don't have enough capital to proceed 
            # further
            if not max_heap: # O(1)
                return w

            # Subtract here, since the max heap is negated.
            w -= heapq.heappop(max_heap)[0] # O(1)
            
            # Then update heaps with new capital.
            # O(len(min_heap)) ~ O(n) worst case
            while min_heap and min_heap[0][0] <= w: 
                x = heapq.heappop(min_heap)[1] # O(log(n))
                heapq.heappush(max_heap, (-profits[x], x)) # O(log(n))
            # While loop is O(nlog(n)) total
        # Overall loop is O(knlog(n)) total.

        return w
        

        """
        Brute force first.
        As expected - works but times out on last few testcases.
        """
        # done = set()
        # # w is capital. annoying they don't call it that
        # for _ in range(k): # O(k) loop
        #     # find the most profitable project 
        #     best = float('-inf') # O(1)
        #     for i in range(len(capital)): # O(n)
        #         if (not i in done) and (capital[i] <= w): # O(1 + len(done)) so O(n) worst case
        #             # if the ith project is most profitable update it
        #             if best == float('-inf'):
        #                 best = i
        #             elif profits[i] > profits[best]:
        #                 best = i

        #         # then do the best project
        #     w += profits[best]  # O(1)
        #     done.add(best) # O(1)
        
        # Above loop comes out to... O(kn^2) total.

        # return w


if __name__ == "__main__":
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))