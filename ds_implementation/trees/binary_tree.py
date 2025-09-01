from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Manager:
    def __init__(self):
        self.root = None


    def insertNode(self, data):
        new_node = Node(data)

        if (self.root is None):
            self.root = new_node
            return

        que = deque()

        que.append(self.root)

        while que:
            curr = que.popleft()

            if curr.left is not None:
                que.append(curr.left)
            else:
                curr.left = new_node
                return

            if curr.right is not None:
                que.append(curr.right)
            else:
                curr.right = new_node
                return
    
    def deleteNode(self, key):
        
        if (self.root is None):
            print("Tree is empty")
            return

        if (self.root.left is None and self.root.right is None):
            if (self.root.data == key):
                temp = self.root
                self.root = None
                del temp
            else:
                print("Key not in tree")
            return

        que = deque()
        que.append(self.root)
        key_node = None


        while que:
            curr = que.popleft()

            if (curr.data == key):
                key_node = curr
            
            if (curr.left is not None):
                que.append(curr.left)

            if (curr.right is not None):
                que.append(curr.right)

        if (key_node is not None):
            x = curr.data
            key_node.data = x

            self.deleteDeepest(curr)
        else:
            print("Key is not found")


    def deleteDeepest(self, dNode):
        que = deque()

        que.append(self.root)

        while que:
            curr = que.popleft()

            if (curr is dNode):
                curr = None
                del dNode
                return

            if (curr.right is not None):
                if (curr.right == dNode):
                    curr.right = None
                    del dNode
                    return
                que.append(curr.right)

            if (curr.left is not None):
                if (curr.left == dNode):
                    curr.left = None
                    del dNode
                    return  
                que.append(curr.left)


def inorder(curr):
    if curr is None:
        return
    inorder(curr.left)
    print(curr.data, end=' ')
    inorder(curr.right)
    

if __name__ == "__main__":
    manager = Manager()

    n = int(input("Enter number of nodes: "))
    print("Enter node values:")
    for _ in range(n):
        val = int(input())
        manager.insertNode(val)

    print("Inorder Traversal of Binary Tree:")
    inorder(manager.root)
    print()
