from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f"ListNode({self.val}, {self.next.__str__()}) "
        else:
            return f"ListNode({self.val}, None)"

    def __repr__(self):
        if self.next:
            return f"ListNode({self.val}, {self.next.__str__()}) "
        else:
            return f"ListNode({self.val}, None)"



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # begin by finding middle of linked list, so that we may split it in 2
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        # print(mid)

        # then reverse the second half
        prev = None
        # save a copy of mid for later...?
        mid_copy = mid
        after = mid.next

        while after != None:
            mid.next = prev
            prev = mid
            mid = after
            after = mid.next

        # don't forget to reverse very last node
        mid.next = prev

        # then. start interweaving.
        # mid starts as the end of the original LL, so the middle of the new one.
        slow = head
        while mid.next != None:
            temp = mid.next
            mid.next = slow.next
            slow.next = mid
            slow = mid.next
            mid = temp

        # return after modifying in place.
        return head 

if __name__ == "__main__":
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    print(s.reorderList(l))