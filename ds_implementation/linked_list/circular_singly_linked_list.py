

class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class ListManager:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtPos(self,k,data):
        if (k < 0):
            print("Invalid position")
            return

        new_node = Node(data)

        if (k == 0 and self.head == None):
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return


        if (k == 0):
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
            return




        if (k > 0 and self.head == None):
            print("K is more than lenght of list")

            return

        
        count = 0

        dummy = Node(0)
        dummy.next = self.head

        temp = dummy
        count = 0


        while (self.tail != temp and count < k):
            temp = temp.next
            count += 1

        if (temp.next == self.tail and count < k):
            print("K is more than length of list")
            return
        
        if (temp == self.tail and count == k):
            self.tail.next = new_node
            new_node.next = dummy.next 
            self.tail = new_node
            return

        temp2= temp.next
        temp.next = new_node
        new_node.next = temp2


    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        result = []
        while True:
            result.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(result) + " -> (back to head)")

    def deleteNodeAtPos(self, k):
        if (k < 0):
            print("Invalid position")
            return

        if self.head == None:
            print("List is empty")
            return

        if (k == 0):
            if (self.head.next == self.head):
                temp = self.head
                self.head = None
                self.tail = None
                del temp

            else:
                temp = self.head
                self.head = self.head.next
                self.tail.next = self.head
                del temp
            return

        if (k >= 1 and self.head == self.head.next):
            print("K is more than length of list")
            return

        curr = self.head

        count = 0

        while (curr.next != self.tail and count < k-1):
            curr = curr.next
            count+=1

        if (curr.next == self.tail and count == k-1):
            self.tail = curr

            del curr.next

            self.tail.next = self.head
            return

        if (curr.next == self.tail and count < k-1):
            print("K is more than lenght of linked list")
            return

        temp = curr.next
        curr.next = curr.next.next
        del temp
        



if __name__ == "__main__":
    lm = ListManager()

    while True:
        print("\nMenu:")
        print("1. Insert node at position")
        print("2. Delete node at position")
        print("3. Display list")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                k = int(input("Enter position (0-based index): "))
                data = input("Enter data: ")
                lm.insertNodeAtPos(k, data)
            except ValueError:
                print("Invalid input. Please enter integers for position.")

        elif choice == "2":
            try:
                k = int(input("Enter position (0-based index): "))
                lm.deleteNodeAtPos(k)
            except ValueError:
                print("Invalid input. Please enter integers for position.")

        elif choice == "3":
            lm.display()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")
