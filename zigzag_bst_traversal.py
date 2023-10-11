# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional
import bst_tools


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue used to store current level AND next level's children
        dq = deque()

        if root == None:
            return dq
        else:
            dq.append(root)

        levels = []
        l2r = True

        while dq:
            level = []
            lvl_len = len(dq)
            for i in range(lvl_len):
                curr = dq.popleft()
                level.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            
            if not l2r:
                level.reverse()
            levels.append(level)
            l2r = not l2r


        return levels


if __name__ == "__main__":
    s = Solution()
    print(s.zigzagLevelOrder(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
    print(s.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, None, TreeNode(5, None, None)))))
    root1 = bst_tools.BST_from_array([0,2,4,1,None,3,-1,5,1,None,6,None,8])
    import binary_tree_level_order_traversal
    x = binary_tree_level_order_traversal.Solution()
    print(x.levelOrder(root1))

            
            