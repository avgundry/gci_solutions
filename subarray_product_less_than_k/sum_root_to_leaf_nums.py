# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """Recursive solution #3: Multiplicative streamlined"""
        return self.sum_path_numbers(root, 0)

    def sum_path_numbers(self, root, curr):
        """GTCI solution - slower than my solution #2 below"""
        # if not root:
        #     return 0

        # curr = 10 * curr + root.val

        # if root.left == None and root.right == None:
        #     return curr

        # return self.sum_path_numbers(root.left, curr) + self.sum_path_numbers(root.right, curr)

        """Recursive solution #2: Multiplicative approach"""
        paths = []
        self.recurseMult(root, 0, paths) 
        return sum(paths)

    def recurseMult(self, root, path, paths):
        if root == None:
            return
        if path == 0:
            # should work
            path = root.val
        else:
            path = path*10 + root.val

        if root.left == None and root.right == None:
            paths.append(path)
        else:
            self.recurseMult(root.left, path, paths)
            self.recurseMult(root.right, path, paths)
            


        """ Recursive solution #1: naive approach"""
    #     paths = []
    #     self.recursePath(root, "", paths)
    #     return sum(paths)

    # def recursePath(self, root, path, paths):
    #     if root == None:
    #         return
    #     path += str(root.val)

    #     if root.left == None and root.right == None:
    #         paths.append(int(path))
    #     else:
    #         self.recursePath(root.left, path, paths)
    #         self.recursePath(root.right, path, paths)

    #     path = path[:-1]
