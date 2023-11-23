from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first find the node where we're reattach
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
        while curr != None:
            curr = curr.next
            n += 1
        k %= n
        while k > 0:
            prev = curr
            # end of list.
            # if curr.next == None:
            #     curr = head
            # else:
            curr = curr.next
            k -= 1

        end = curr
        while end.next != None:
            end = end.next

        print(f"curr: {curr}")
        print(f"prev: {prev}")
        print(f"end: {end}")

        prev.next = None
        end.next = head
        head = curr

        return head

if __name__ == "__main__":
    s = Solution()
    print(s.rotateRight([1, 2, 3], 1))
