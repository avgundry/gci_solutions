# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ## contains list of nodes on the right side
        # can be HEAVILY optimized.
        ret: List = []

        if root == None:
            return ret

        q: collections.deque = collections.deque()
        q.append(root)
        while q:
            # can def be optimized to ignore leftmost nodes. figure out when home
            for _ in range(len(q) - 1):
                rightmost: TreeNode = q.popleft()
                if rightmost.left:
                    q.append(rightmost.left)
                if rightmost.right:
                    q.append(rightmost.right)
            ret.append(rightmost.val)

        return ret

        