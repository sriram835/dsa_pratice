

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertNodeAtPos(self, data, k):
        

        if (k < 0):
            print("Invalid Position")
            return

        new_node = Node(data)
        if (k == 0):
            if (self.head == None):
                self.head = new_node
                self.tail = self.head
            else:
                new_node.next = self.head
                self.head = new_node
            self.length+=1
            return

        curr = self.head
        count = 0

        while (curr.next != None and count < k-1):
            curr = curr.next
            count+=1

        if (curr.next == None and count < k -1 ):
            print("k is more than length of list")
            return

        if (curr.next == None and count == k -1):
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1
            return

        temp = curr.next
        curr.next = new_node
        new_node.next = temp
        self.length+=1

    def deleteNodeAtPos(self, k):
        if (k < 0):
            print("Invalid position")
            return

        if (self.head == None):
            print("List is empty")
            return

        if (k == 0 and self.head.next != None):
            temp = self.head
            self.head = self.head.next
            del temp
            self.length-=1
            return

        if (k == 0 and self.head.next == None):
            self.head = None
            self.tail = None
            self.length -=1
            return
        
        curr = self.head
        count = 0

        while (curr.next != None and count < k - 1):
            curr = curr.next
            count+=1

        if (curr.next == None):
            print("K is more than length of list")
            return

        if (curr.next == self.tail):
            self.tail = curr
            temp = curr.next
            self.tail.next = None
            del temp
            self.length-=1
            return

        temp = curr.next
        curr.next = curr.next.next
        self.length-=1
        del temp


                
            


