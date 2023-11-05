# this seems suspiciously easy...?

from heapq import *
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # to optimize..hm. Only take the smallest one at a time? I guess that
        # does significantly improve heap insertion time, and changes runtime
        # to be O(nlog(len(lists))) instead. ok.
        min_heap = []
        # initialize min_heap to contain the first value of each of the given
        # lists.
        for i in range(len(lists)):
            heappush(min_heap, lists[i])
            # lists[i] = lists[i].next

        
        first = prev = None
        # then, repeatedly find the smallest one and add it to the list
        # runs O(n) times
        while min_heap:
            # O(log(len(lists))) each time, to rebalance.
            curr = heappop(min_heap)
            ind = curr[1]
            lists[ind] = lists[ind].next
            if lists[ind] != None:
                heappush(min_heap, [lists[ind].val, ind])
            if not first:
                first = ListNode(curr[0])
                prev = first
            else:
                prev.next = ListNode(curr[0])
                prev = prev.next 

        return first


        """
        O(Nlog(N)) solution
        """
        # max_heap = []
        # curr = None
        # for l in lists:
        #     curr = l
        #     while curr:
        #         heappush(max_heap, -curr.val)
        #         curr = curr.next

        # prev = None
        # while max_heap:
        #     curr = ListNode(-heappop(max_heap), prev)
        #     prev = curr

        # return curr

def printLL(node):
    while node:
        print(f"{node.val}->", end='')
        node = node.next
    print()

if __name__ == "__main__":
    s = Solution()
    ll1 = ListNode(1, ListNode(4, ListNode(5, None)))
    ll2 = ListNode(1, ListNode(3, ListNode(4, None)))
    ll3 = ListNode(2, ListNode(6, None))
    printLL(s.mergeKLists([ll1, ll2, ll3]))