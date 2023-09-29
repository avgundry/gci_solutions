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
        res = []
        if root == None:
            return res
        
        # whether we're going left to right or opposite on this level
        l2r = True
        dq = deque()
        dq.append(root)

        while dq:
            print(dq)
            temp_nodes = deque() 
            curr_level = []
            lvl_size = len(dq)
            for _ in range(lvl_size):
                curr = dq.popleft()
                curr_level.append(curr.val)
                if l2r:
                    if curr.right:
                        temp_nodes.append(curr.right)
                    if curr.left:
                        temp_nodes.append(curr.left)
                else:
                    if curr.right:
                        temp_nodes.appendleft(curr.right)
                    if curr.left:
                        temp_nodes.appendleft(curr.left)
            
            res.append(curr_level)
            dq.extend(temp_nodes)
            l2r = not l2r

        return res

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)

def recursiveBSTbuild(arr):
    length = len(arr)

    return traverseAndReplace(arr, arr[0], 0, length)

def traverseAndReplace(arr, root, i, length):
    if i < length:
        root = TreeNode(arr[i])
        root.left = traverseAndReplace(arr, root.left, 2*i+1, length)
        root.right = traverseAndReplace(arr, root.right, 2*i+2, length)

    return root

#inorder(recursiveBSTbuild([0,2,4,1,None,3,-1,5,1,None,6,None,8]))
            
if __name__ == "__main__":
    s = Solution()
    print(s.zigzagLevelOrder(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
    print(s.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, None, TreeNode(5, None, None)))))
    root1 = bst_tools.BST_from_array([0,2,4,1,None,3,-1,5,1,None,6,None,8])
    import binary_tree_level_order_traversal
    x = binary_tree_level_order_traversal.Solution()
    print(x.levelOrder(root1))

            
            