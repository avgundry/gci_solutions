# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next == None:
            return f"{{{self.val}, None}}"
        else:
            return f"{{{self.val}, {self.next.__repr__()}}}"


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get n first
        curr = head
        n = 0
        while curr != None:
            curr = curr.next
            n += 1

        if n == 0:
            return head
        
        # print(f"Calling original mergesort on {head} with length {n}")
        return self.mergeSort(head, n)

    def mergeSort(self, head, length):
        if length == 1:
            return head
        else:
            # find the middle
            n = 0
            curr = head
            for i in range(length // 2):
                curr = curr.next
            # print(f"recursively mergesorting {head} with length {length // 2}\n")
            self.mergeSort(head, length // 2)
            # print(f"recursively mergesorting {curr} with length {length - length // 2}\n")
            self.mergeSort(curr, length - length // 2)
            return self.merge(head, curr, length)

    def merge(self, head1, head2, length):
        if head1.val <= head2.val:
            new_head = head1
            head1 = head1.next
        else:
            new_head = head2
            head2 = head2.next
            

        length -= 1
        curr = ListNode(new_head.val)

        while head1 and head2:
            if not head2 or head1.val <= head2.val:
                curr.next = head1
                curr = curr.next
                head1 = head1.next
            else:
                curr.next = head2
                curr = curr.next
                head2 = head2.next

        while head1:
            curr.next = head1
            curr = curr.next
            head1 = head1.next


        return new_head

    # swaps nodes such that node1.next = node2
    # only swaps if node1.val > node2
    # returns the node that will come first
    def swap_nodes(node1, node2):
        if node1.val <= node2.val:
            return node1
        else:
            temp = node2.next
            node2.next = node1
            node1.next = temp 
            return node2

if __name__ == "__main__":
    s = Solution()
    l = ListNode(4, ListNode(2, ListNode(1, ListNode(3, None))))
    print(s.sortList(l))