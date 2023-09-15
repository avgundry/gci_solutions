# Definition for singly-linked list.
from typing import Optional
from reverse_linked_sublist import PrintLL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first step is to split them into groups of k elements each?
        if head == None or head.next == None:
            return head

        i = 0
        curr = head
        # make an array of "subheads", the starting nodes of sublists
        subheads = []
        # we will also need an array of the end of sublists, to link to
        # afterwards.
        subends = []

        while curr != None:
            if i == 0:
                subheads.append(curr)
                i += 1
            elif k == i + 1:
                # only occurs at the end of sublists
                subends.append(curr)
                i = 0
            else:
                # move along until finding either a subend or subhead

                i += 1

            # if curr.next == None:
            # # then we need to link the last subend up
            #     subends.append(curr)
            curr = curr.next
            
        # hm. after the loop, if we didn't hit another subend, then we need to
        # NOT reverse the last sublist chunk. i.e. it shouldn't be a sublist at
        # all. hmm
        link_normal = None
        if len(subheads) > len(subends):
            # we have an incomplete sublist at the end that won't be reversed
            link_normal = subheads[-1]
            del subheads[-1]
        print(f"subheads: {[node.val for node in subheads]}")
        print(f"subends: {[node.val for node in subends]}")

        # if len(subends) < len(subheads):
        #     subends.append(None)

        # then reverse them
        for j in range(len(subends)):
            subhead = subheads[j]
            subend = subends[j]
            
            prev = None
            curr = subhead
            forward = None
            i = 0

            while i < k and curr != None:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
                i += 1
            # while curr != subend:
            #     forward = curr.next
            #     curr.next = prev
            #     prev = curr
            #     curr = forward

        # then link them together?
        for i in range(len(subends) - 1):
            print(subheads[i].val)
            subheads[i].next = subends[i+1]

        # if link_normal exists, link the last thing to it
        # if it doesn't then it will just point to none.
        subheads[-1].next = link_normal

        head = subends[0]

        return head
        
if __name__ == "__main__":
    s = Solution()
    PrintLL(s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2))
    PrintLL(s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 3))