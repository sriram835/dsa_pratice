

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Manager:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtPos(self, data, k):
        if (k < 0):
            print("Invalid Position")
            return

        new_node = Node(data)
        if (self.head is None):
            if (k == 0):
                self.head = self.tail = new_node
                self.head.prev = self.head
                self.head.next = self.head
            else:
                print("K is more than length of list")
            return

        if (self.head.next == self.head):
            if (k == 0):
                new_node.next = self.head
                self.head.prev = new_node
                self.head.next = new_node
                new_node.prev = self.tail
                self.head = new_node
            elif (k == 1):
                self.head.next = new_node
                self.head.prev = new_node
                new_node.prev = self.head
                new_node.next = self.head
                self.tail = new_node
            else:
                print("K is more than lenght of list")
            return

        if (k == 0):
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node

            return



        curr = self.head

        count = 0

        while (curr != self.tail and count < k-1):
            count+=1
            curr = curr.next

        if (curr == self.tail and count < k-1):
            print("Length of list is less than given position")
            return

        if (curr == self.tail and count == k -1):
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

            return

        temp = curr.next

        curr.next = new_node
        new_node.prev = curr
        temp.prev = new_node
        new_node.next = temp
        return
    
    def displayForward(self, n=None):
        """Traverse forward and print n elements (default = full circle)."""
        if self.head is None:
            print("List is empty")
            return

        curr = self.head
        result = []
        count = 0
        while True:
            result.append(curr.data)
            curr = curr.next
            count += 1
            if curr == self.head or (n is not None and count >= n):
                break
        print("Forward:", result)

    def displayBackward(self, n=None):
        """Traverse backward and print n elements (default = full circle)."""
        if self.tail is None:
            print("List is empty")
            return

        curr = self.tail
        result = []
        count = 0
        while True:
            result.append(curr.data)
            curr = curr.prev
            count += 1
            if curr == self.tail or (n is not None and count >= n):
                break
        print("Backward:", result)


    def deleteNodeAtPos(self, k):
        if (k < 0):
            print("Invalid position")
            return

        if (self.head is None):
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
                self.head.prev = self.tail
                self.tail.next = self.head
                del temp
            return

        if (self.head == self.head.next and k > 0):
            print("positon is more than length of list")
            return

        count = 0
        curr = self.head

        while (curr.next != self.tail and count < k-1):
            curr = curr.next
            count +=1

        if (curr.next == self.tail and count < k -1):
            print("Position is more than length of list")
            return

        if (curr.next == self.tail and count == k - 1):
            self.tail = self.tail.prev
            temp = self.tail.next
            self.tail.next = self.head
            self.head.prev = self.tail
            del temp
            return


        temp = curr.next
        next_node = curr.next.next

        curr.next = next_node
        next_node.prev = curr
        del temp










            
if __name__ == "__main__":
    m = Manager()

    print("\n=== Insertion Tests ===")
    m.insertNodeAtPos(10, 0)   # head=10
    m.displayForward()
    m.displayBackward()

    m.insertNodeAtPos(5, 0)    # insert at head
    m.displayForward()
    m.displayBackward()

    m.insertNodeAtPos(20, 2)   # insert at tail
    m.displayForward()
    m.displayBackward()

    m.insertNodeAtPos(15, 2)   # insert in the middle
    m.displayForward()
    m.displayBackward()

    m.insertNodeAtPos(100, 10) # invalid position
    m.displayForward()

    print("\n=== Deletion Tests ===")
    m.deleteNodeAtPos(-1)      # invalid
    m.deleteNodeAtPos(10)      # invalid
    m.displayForward()

    m.deleteNodeAtPos(0)       # delete head (5)
    m.displayForward()
    m.displayBackward()

    m.deleteNodeAtPos(2)       # delete tail (20)
    m.displayForward()
    m.displayBackward()

    m.deleteNodeAtPos(1)       # delete middle (15)
    m.displayForward()
    m.displayBackward()

    m.deleteNodeAtPos(0)       # delete last node (10), list empty
    m.displayForward()
    m.displayBackward()

    m.deleteNodeAtPos(0)       # delete from empty list               
