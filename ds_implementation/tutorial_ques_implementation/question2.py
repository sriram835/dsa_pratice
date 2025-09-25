

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

exprs = "((2+3)*5)"

root = Node('*')
root.left = Node('+')
root.left.left = Node('2')
root.left.right = Node('3')
root.right = Node('5')

def postorder(root):
    if root is None:
        return
    
    left = postorder(root.left)
    right = postorder(root.right)

    if root.data == '-' or root.data == '+' or root.data == '*' or root.data == '/':
        eps = "(" + left + root.data + right + ")"
        return eps
    else:
        return root.data

def find_answer(root,exp):
    return postorder(root) == exp