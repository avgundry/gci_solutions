# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print2DUtil(root, space):
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += 10
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(10, space):
        print(end=" ")
    print(root.val)
 
    # Process left child
    print2DUtil(root.left, space)

def print2D(root):
    print2DUtil(root, 0)


class Solution:
    # iterative BFS approach
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # print2D(root)
        if root == None:
            return 0

        # use similar approach to level traversal
        dq = deque()
        dq.append(root)
        depth = 0
        while dq:
            depth += 1
            # print(f"loop at depth {depth}")
            lvl_size = len(dq)
            for _ in range(lvl_size):
                curr = dq.pop()
                if curr.left == curr.right == None:
                    # print(f"AT TIME OF RETURN: curr = {curr.val}, curr.left = {curr.left}, curr.right={curr.right}")
                    return depth
                else:
                    if curr.left:
                        dq.appendleft(curr.left)
                    if curr.right:
                        dq.appendleft(curr.right)


        return depth


    # recursive DFS approach
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if root == None:
    #         return 0
    #     return self.depthRecurse(root)

    # def depthRecurse(self, node):
    #     if node == None:
    #         return float('Inf')

    #     left = node.left
    #     right = node.right

    #     if left == right == None:
    #         return 1
        
    #     left_depth = self.depthRecurse(left)
    #     right_depth = self.depthRecurse(right)
    #     return min(left_depth, right_depth)+1
        
if __name__ == "__main__":
    s = Solution()
    s.minDepth(TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, None, TreeNode(5))))