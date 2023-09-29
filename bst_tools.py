class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# tools for traversing etc. BSTs
def BST_from_array(arr):
    # root is index 0. children of val at index i are i*2+1, i*2+2
    if len(arr) == 0:
        return None
    
    return recursive_build(arr, 0)

def recursive_build(arr, i):
    if i >= len(arr) or arr[i] == None:
        return None

    # left = right = None
    # if 2*i + 1 <= len(arr):
    #     # it has a left child
    #     left = recursive_build(arr, 2*i+1)
    # if 2*i + 2 <= len(arr):
    #     # it has a right child
    #     right = recursive_build(arr, 2*i+2)
    left = recursive_build(arr, 2*i+1)
    right = recursive_build(arr, 2*i+2)

    return TreeNode(arr[i], left, right)

# testing
if __name__ == "__main__":
    import binary_tree_level_order_traversal
    x = binary_tree_level_order_traversal.Solution()
    root = BST_from_array([1, 2, 3, 4, 5])
    print(x.levelOrder(root))
