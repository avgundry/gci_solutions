# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
from typing import Optional

from linked_list_cycle import ListNode


class Solution:
    def findMid(self, head):
        # returns pointer to middle node of a given linkedlist
        # if of even length, returns the rightmost 'middle'
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # reverses a given linked list
    def reverse(self, head):
        # print(f"mid before reversing: {head}")
        prev = None
        curr = head
        after = curr.next

        while after != None:
            curr.next = prev
            prev = curr
            curr = after
            after = curr.next

        # for the very last node
        curr.next = prev
        # print(f"mid after reversing: {curr}")
        return curr

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle of list.
        if not head or head.next == None:
            return True
        mid = self.findMid(head)
        # print(mid)
        new_mid = self.reverse(mid)
        # print(f"mid after reverse: {mid}")
        orig = head
        curr = new_mid 

        palin = True
        while palin and curr != None and orig != None:
            if curr.val != orig.val:
                palin = False
            curr = curr.next
            orig = orig.next

        # re-reverse the original list and connect it back up
        # print(f"curr: {curr}")
        self.reverse(new_mid)
        # print(f"list: {head}")

        return palin

        

if __name__ == "__main__":
    s = Solution()