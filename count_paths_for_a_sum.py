# Path Sum III on Leetcode.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        return self.recursePaths([root])

    # recursive method that is hopefully not as memory/time intensive
    # reutilizes the same path
    def recursePaths(self, path):
        curr = path[-1]
        if curr == None:
            del path[-1]
            return 0
        
        num_paths = 0
        path_sum = 0
        for i in range(len(path)):
            path_sum += path[-i-1].val
            if path_sum == self.targetSum:
                num_paths += 1
            
        path.append(curr.left)
        left = self.recursePaths(path)
        path.append(curr.right)
        right = self.recursePaths(path)
        del path[-1]

        return num_paths + left + right


    # this is the really awful way, that technically works but fails on runtime
    # and probably also memory cause it takes an absurd amount of memory
    # path is the path so far, INCLUDING curr
    # def recursePaths(self, path, targetSum):
    #     # each node should return 1 if its addition creates a new path
    #     if path[-1] == None:
    #         return 0

    #     # I thiiiiink we have to search for each subset within the path...
    #     # we only have to search N nodes though, where N is the path so far
    #     curr = path[-1]
    #     num_paths = 0
    #     for i in range(len(path)):
    #         if sum([x.val for x in path[i:]]) == targetSum:
    #             num_paths += 1
        
    #     # god this memory usage will be HORRENDOUS won't it 
    #     left = path.copy()
    #     left.append(curr.left)
    #     right = path.copy()
    #     right.append(curr.right)
    #     return num_paths + self.recursePaths(left, targetSum) + self.recursePaths(right, targetSum)

    


if __name__ == "__main__":
    s = Solution()
    print(s.pathSum(TreeNode(1, None, TreeNode(4, None, None)), 5))
    print(s.pathSum(TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(4, None, None)), 0))
    print(s.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3, None, None), TreeNode(-2, None, None)), TreeNode(2, None, TreeNode(1, None, None))), TreeNode(-3, None, TreeNode(11, None, None))), 8))