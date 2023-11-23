# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def __init__(self):
        self.maxDiam = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # hm. just find two that are farthest apart which....will be the 
        # leftmost and rightmost at greatest depth?
        # print(f"base root: {root}")
        if root == None or (root.left == None and root.right == None):
            return 0

        self.recurse(root)
        return self.maxDiam


    def recurse(self, root):
        if root == None:
            return 0
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        # own height is 1 + max of left and right
        # in case of leaf node this will be 0 
        # own diameter is just left + right heights
        self.maxDiam = max(left + right, self.maxDiam)
        # but then the *best* diameter is the maximum of its own diameter
        # and the diameter of any subtrees
        # diam = max(diam, left[1], right[1])


        # for each node, return its height (i.e. max height of left/right subtrees),
        # and its maximum diameter - i.e. max diameter among it and all subtrees
        return 1 + max(left, right)
 

        
        