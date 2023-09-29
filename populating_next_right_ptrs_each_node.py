from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        # simply use BFS level traversal, connect each node to the next one in the queue
        dq = deque()
        dq.append(root)
        prev = None

        # could be optimized by having a prev node, possibly
        # or being recursive...
        while dq:
            lvl_size = len(dq)
            for _ in range(len(dq)):
                curr = dq.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            # will always be the last one on this level
            curr.next = None
            prev = None

        return root