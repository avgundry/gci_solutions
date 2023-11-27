from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    #     if self.right is not None:
    #         fmt = '{}({value!r}, {left!r}, {right!r})'
    #     elif self.left is not None:
    #         fmt = '{}({value!r}, {left!r})'
    #     else:
    #         fmt = '{}({value!r})'
    #     return fmt.format(type(self).__name__, **vars(self))

class Solution:
    def __init__(self):
        # self.visited: set(TreeNode) = set()
        # self.stack: list[TreeNode] = []
        self.best: int = -float('inf')
        # can optimize further with DP as below:

        # array of best values at the ith node.
        # root is 0. children are 2i + 1, 2i + 2
        # self.bestvals: [int] = []

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return root.val
        self.DFS(root)

        return self.best


    def DFS(self, root):
        if root == None:
            return 0

        # print(f"root: {root}")
        # print(f"root.left: {root.left}")
        # print(f"self.DFS(root.left): {self.DFS(root.left)}")
        # x = self.DFS(root.left)
        # print(f"val of self.DFS(root.left): {x}")
        # print('\n\n')
        # print(max(0, 0))
        maxleft = max(self.DFS(root.left), 0)
        maxright = max(self.DFS(root.right), 0)

        mxpath = root.val + maxleft + maxright
        self.best = max(mxpath, self.best) 

        return max(root.val + maxleft, root.val + maxright



if __name__ == "__main__":
    s = Solution()
    ll = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    print(s.maxPathSum(ll))