# Path Sum III on Leetcode.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # gotta do some crazy stuff here.
        # basically...pass each recursive function a list of all the previous?? god. uhh
        # well, wait. I mean...it's a binary tree. would putting it into array form help at all?
        



    


if __name__ == "__main__":
    s = Solution()
    print(s.pathSum(TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(4, None, None)), 0))
    print(s.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3, None, None), TreeNode(-2, None, None)), TreeNode(2, None, TreeNode(1, None, None))), TreeNode(-3, None, TreeNode(11, None, None))), 8))