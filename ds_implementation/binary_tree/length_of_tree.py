class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating a sample binary tree
#        1
#       / \
#      2   3
#     /   / \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right= TreeNode(7)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)


def findDepth(root):
    if (root == None):
        return 0
    
    left_length= findDepth(root.left)
    right_length=findDepth(root.right)

    return 1+max(left_length, right_length)


def isFullTree(root):
    if (root is None):
         return True

    if ((root.left is None and root.right is not None) or (root.left is not None and root.right is None)):
        return False
    
    if (isFullTree(root.left) == True and isFullTree(root.right)):
            return True
    return False

#print(findDepth(root))
print(isFullTree(root))
