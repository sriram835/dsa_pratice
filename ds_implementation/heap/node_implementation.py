
class Node:
    def __init__(self, data=None,parent=None,left=None,right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

class MinHeap:
    def __init__(self):
        self.root = None

    def addElement(self,data):
        new_node = Node(data)
        que1 = []
        if (self.root is None):
            self.root = new_node

            return

        que1.append(self.root)

        while (len(que1) > 0):
            curr = que1.pop(0)

            if (curr.left is None):
                curr.left = new_node
                new_node.parent = curr
                break
            else:
                que1.append(curr.left)


            if (curr.right is None):
                curr.right = new_node
                new_node.parent = curr
                break 
            else:
                que1.append(curr.right)

        self.heapifyUp(new_node)

    def heapifyUp(self,node):
        curr = node

        while (curr is not None):
            if (curr.parent is None):
                break
            if (curr.parent.data < curr.data):
                break

            curr.parent.data, curr.data = curr.data, curr.parent.data
            curr = curr.parent


    def find_last_node(self):
        if self.root is None:
            return None

        que= []
        curr = None
        que.append(self.root)

        while (len(que) > 0):
            curr = que.pop(0)
            if curr.left is not None:

                que.append(curr.left)

            if curr.right is not None:
                que.append(curr.right)

        return curr




    def removeElement(self):
        if (self.root is None):
            print("heap is empty")
            return None

        if (self.root.left is None and self.root.right is None):
            temp = self.root.data
            self.root = None
            return temp

        last_node = self.find_last_node()

        res = self.root.data
        self.root.data = last_node.data
        temp = last_node.parent
        if (temp.left == last_node):
            temp.left = None
        else:
            temp.right = None

        self.heapifyDown()
        return res


    def heapifyDown(self):
        curr = self.root

        while (curr is not None):
            if (curr.left is None):
                break
            minChild = curr.left
            if (curr.right is not None and curr.right.data < curr.left.data):
                minChild = curr.right

            if (minChild.data > curr.data):
                break
            minChild.data, curr.data = curr.data,minChild.data

            curr = minChild


    def print_tree_structure(self):
        """Print tree structure with parent-child relationships"""
        if self.root is None:
            print("Heap is empty")
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            parent_data = node.parent.data if node.parent else "None"
            left_data = node.left.data if node.left else "None"
            right_data = node.right.data if node.right else "None"
            
            print(f"Node: {node.data}, Parent: {parent_data}, Left: {left_data}, Right: {right_data}")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def print_heap(self):
        """Print heap in level order format"""
        if self.root is None:
            print("Heap is empty")
            return
        
        queue = [self.root]
        level = 0
        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end="")
            
            for i in range(level_size):
                node = queue.pop(0)
                print(f"{node.data} ", end="")
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()  # New line after each level
            level += 1

# Driver Program
def main():
    heap = MinHeap()
    
    while True:
        print("\n=== Min Heap Operations ===")
        print("1. Insert element")
        print("2. Extract minimum")
        print("3. Print heap (level order)")
        print("4. Print tree structure")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                value = int(input("Enter value to insert: "))
                heap.addElement(value)
                print(f"Inserted {value}")
                
            elif choice == 2:
                min_val = heap.removeElement()
                if min_val is not None:
                    print(f"Extracted minimum: {min_val}")
                    
            elif choice == 3:
                print("\nHeap contents:")
                heap.print_heap()
                
            elif choice == 4:
                print("\nTree structure:")
                heap.print_tree_structure()
                
            elif choice == 5:
                print("Exiting...")
                break
                
            else:
                print("Invalid choice! Please enter 1-5.")
                
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
















