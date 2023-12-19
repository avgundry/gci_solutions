from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None or head.next == None:
            return head


        # ok, what do we actually want to find here.
        # we have three things, I think.
        # first is the new head. 
        # this will be the (k % n)th node. right? yeah.
        # then, the end of the second half of the list. this gets attached to the OLD head.
        # finally, the last node of the new list. we need to disconnect it.
        # this should be the...((k % n) - 1)th node?

        curr = head
        prev = None

        # find length of LL first, to avoid needlessly looping.
        n = 1
        while curr.next != None:
            curr = curr.next
            n += 1

        # print(n) 
        # if we don't rotate, simply return
        if (k % n) == 0:
            return head

        # after looping through we will have found end of the old list.
        # we need this to attach it to the new head. 
        old_end = curr

        # then. find the new head, and the new end of the list.
        # modulo k by n to avoid needlessly looping
        k %= n
        # then advance by (n - k) to find new head and new end of list
        new_end = None
        curr = head
        for i in range(n - k):
            new_end = curr
            curr = curr.next

        # print(f"new head: {curr}")
        # print(f"new end: {new_end}")
        # print(f"old head: {head}")
        # print(f"old end: {old_end}")

        # then just link them all up.
        # old end -> old head.
        # new end -> None.
        # head = new_head.
        old_end.next = head
        new_end.next = None
        head = curr

        return head 

if __name__ == "__main__":
    s = Solution()
    # print(s.rotateRight([1, 2, 3], 1))
