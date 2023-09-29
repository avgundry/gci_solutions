# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_cycle import ListNode


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # start with recursive I guess? 
    #     if head == None or head.next == None:
    #         return head
    #     return self.flip(None, head)

    # def flip(self, prev, curr):
        
    #     if curr == None:
    #         # we've reached the end of the list and should return prev as the 
    #         # new head
    #         return prev
    #     newHead = self.flip(curr, curr.next)
    #     # so to flip we must set curr's next to prev. I know that much at least.
    #     curr.next = prev

    #     return newHead

    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        prev = None
        curr = head
        forward = head.next

        

        while forward != None:
            curr.next = prev
            prev = curr
            curr = forward
            forward = curr.next

        # when forward is none we are at the end of the list. which means curr is the new head.
        head = curr
        head.next = prev

        return head
