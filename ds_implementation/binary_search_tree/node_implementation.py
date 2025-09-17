
class Node:
    def __init__(self, data =None,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right 


class BST:
    def __init__(self):
        self.root = None

    def addElement(self, data):
        new_node = Node(data)
        if (self.root is None):
            self.root = new_node
            return

        curr = self.root
        while (curr is not None):
            if (new_node.data == curr.data):
                print("Duplicate insertion")
                return

            if (new_node.data > curr.data):
                if (curr.right is None):
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                if (curr.left is None):
                    curr.left = new_node
                    return
                curr = curr.left

    def searchElement(self,data):
        temp = self.searchHelper(self.root,data)
        if (temp is not None):
            return temp

        
        
    def searchHelper(self,root, data):
        if (root is None):
            print("Element does not exists")
            return None

        if (root.data == data):
            return data
        
        if (root.data > data):
            return self.searchHelper(root.left,data)
        else:
            return self.searchHelper(root.right,data)


    def removeElement(self,data):
        if (self.root is None):
            print("BST is empty")
            return

        curr = self.root
        prev = None

        while (curr):
            if (curr.data == data):
                break

            if (curr.data > data):
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

        if (curr is None):
            print("Element not found")
            return
        
        if (curr.left is None and curr.right is None):
            if (curr == self.root):
                self.root = None
                return
            if (prev.left == curr):
                prev.left = None
            else:
                prev.right = None
            return


        if (curr.left is None or curr.right is None):
            child = curr.left
            
            if (curr.left is None):
                child = curr.right
            if (curr == self.root):
                self.root = child
                return
            if (prev.left == curr):
                prev.left = child
            else:
                prev.right = child
            return 

        res = self.findPredessor(curr)
        pred = res[0]
        prevpred=res[1]

        curr.data = pred.data
        if (prevpred.right == pred):
            prevpred.right = pred.left
        else:
            prevpred.left = pred.left



    def findPredessor(self,node):
        prev = node
        curr = node.left
        while (curr.right):
            prev = curr
            curr = curr.right
        return [curr,prev]

    def findSuccessor(self,node):
        prev = node
        curr = node.right
        while (curr.left):
            prev = curr
            curr = curr.left
        return [curr,prev]

    def _printTreeHelper(self, node, level=0):
        if node is not None:
            self._printTreeHelper(node.right, level + 1)
            print("    " * level + str(node.data))
            self._printTreeHelper(node.left, level + 1)

    def printTree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            print("Current BST structure:")
            self._printTreeHelper(self.root)


def menu():
    print("\n--- Binary Search Tree Operations ---")
    print("1. Insert element")
    print("2. Search element")
    print("3. Delete element")
    print("4. Print tree")
    print("5. Exit")
    print("------------------------------------")

def main():
    tree = BST()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            data = int(input("Enter value to insert: "))
            tree.addElement(data)
            print(f"Inserted {data}.")
            tree.printTree()

        elif choice == "2":
            data = int(input("Enter value to search: "))
            node = tree.searchElement(data)
            if node:
                print(f"Element {data} found in BST")
            else:
                print(f"Element {data} not found in BST")

        elif choice == "3":
            data = int(input("Enter value to delete: "))
            tree.removeElement(data)
            print(f"Attempted to delete {data}.")
            tree.printTree()

        elif choice == "4":
            tree.printTree()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()



