from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # iterative approach 
        result = []
        if not root:
            return result
        
        queue = [root]
        print(queue)
        while queue:
            current_level = []
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.pop(0)
                current_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(current_level)

        
        return result 
    #     # ~~~ RECURSIVE definition ~~~ #
    #     if root == None:
    #         return []

    #     queue = []

    #     return self.recurseBFS(queue, root, 0)

    # # returns an array of a binary tree in BFS order?
    # def recurseBFS(self, queue, curr, level):
    #     if curr == None:
    #         return

    #     self.recurseBFS(queue, curr.left, level + 1)
    #     self.recurseBFS(queue, curr.right, level + 1)
    #     while len(queue) <= level:
    #         queue.append([])
    #     queue[level].append(curr.val)

    #     return queue

if __name__ == "__main__":
    s = Solution()
    x = s.levelOrder(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))))
    print(x)