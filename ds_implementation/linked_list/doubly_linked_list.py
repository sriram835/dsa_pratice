
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Manager:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtPos(self, data, pos):
        if pos < 0:
            print("Invalid position")
            return

        new_node = Node(data)

        # Empty list
        if self.head is None:
            if pos == 0:
                self.head = self.tail = new_node
            else:
                print("Given position is more than length")
            return

        # Insert at head
        if pos == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # Traverse to position
        curr = self.head
        count = 0
        while count < pos and curr is not None:
            curr = curr.next
            count += 1

        if curr is None:
            if count == pos:  # Append at end
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                print("Given position is more than length")
            return

        # Insert in middle
        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node


    def deleteNodeAtPos(self, k):
        if (k < 0):
            print("Invalid position")
            return

        if (self.head == None):
            print("List is empty")
            return

        if (k == 0):
            if (self.head.next == None):
                temp = self.head
                self.head = None
                self.tail = None
                del temp

            else:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                del temp
            return


        curr = self.head
        count = 0

        while (curr != None and count < k):
            curr = curr.next
            count+=1

        if (curr == None):
            print("Length of the list is less than given position")
            return

        if (curr.next == None):
            prev_node = curr.prev
            self.tail = prev_node
            self.tail.next = None
            del curr
            return

        prev_node = curr.prev
        next_node = curr.next

        prev_node.next = next_node
        next_node.prev = prev_node
        del curr



    def display_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")


    def display_backward(self):
        curr = self.tail
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None")


if __name__ == "__main__":
    dll = Manager()

    while True:
        print("\n--- Menu ---")
        print("1. Insert node")
        print("2. Delete node at position")
        print("3. Display list forward")
        print("4. Display list backward")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = int(input("Enter data: "))
            pos = int(input("Enter position (0-based index): "))
            dll.insertNodeAtPos(data, pos)

        elif choice == "2":
            pos = int(input("Enter position to delete: "))
            dll.deleteNodeAtPos(pos)

        elif choice == "3":
            dll.display_forward()

        elif choice == "4":
            dll.display_backward()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")


