# Definition for singly-linked list.
from typing import Optional

def PrintLL(head):
    temp = head
    while temp != None:
        print(str(temp.val) + " -> ", end="")
        temp = temp.next
    print("None")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
    # advance to the point we get the left node
    # Doing the third step in an inelegant fashion at first:
    # - save node immediately before left node
    # - save node immediately after right node 
    # - save left node
    # - save right node 
        preceding_node = None
        temp = head
        i = 0
        while i < left - 1:
            preceding_node = temp
            temp = temp.next
            i += 1
        # temp will now be the node immediately before the left one.
        left_node = temp

        # then advance to right
        while i < right - 1:
            temp = temp.next
            i += 1
        # temp will now be the right node.
        right_node = temp
        if temp != None:
            succeeding_node = temp.next
        else:
            succeeding_node = None

        print(f"preceding_node: {preceding_node.val}\nleft_node: {left_node.val}\n ")
        print(f"right_node: {right_node.val}\nsucceeding_node: {str(succeeding_node.val) if succeeding_node else 'None'}")
        PrintLL(head)



    # reverse the sublist like reversing a normal linked list
        temp = left_node
        prev = preceding_node 
        forward = temp.next 

        while temp != succeeding_node:
            forward = temp.next
            temp.next = prev
            prev = temp
            temp = forward

    # connect up the rest of the list
    # this consists of:
    # - Connect the node immediately before sublist to the new beginning 
    #   of the reversed sublist
    # - Connect the new end of the sublist to the node immediately after
    #   sublist
    # so in above example, point 1 to 4, and then 2 to 5. 
        print(f"left_node: {left_node.val}")
        left_node.next = succeeding_node
        if preceding_node != None:
            preceding_node.next = right_node
        
        return head

if __name__ == "__main__":
    s = Solution()
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    head2 = ListNode(3, ListNode(5, None))
    PrintLL(s.reverseBetween(head1, 2, 4))
    #s.reverseBetween(head2, 1, 2)