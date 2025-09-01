from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.left or root.right:  # Only go deeper if there are children
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

def insert_node(root, data):
    node_queue = deque()
    
    if (root == None):
        root = Node(data)
        return root

    node_queue.append(root)


    while (len(node_queue) != 0):
        curr = node_queue.popleft()

        if (curr.left != None):
            node_queue.append(curr.left)
        else:
            curr.left = Node(data)
            break

        if (curr.right != None):
            node_queue.append(curr.right)
        else:
            curr.right = Node(data)
            break

    return root




root = Node(1)
root.left = Node(2)
root.right = Node(3)
print_tree(root)

insert_node(root, 4)
print_tree(root)
