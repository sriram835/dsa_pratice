

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None


    def add_front(self, data):
        new_node = Node(data)

        if (self.front is None):
            self.front = self.rear = new_node

            return

        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def add_rear(self, data):
        new_node = Node(data)

        if (self.rear is None):
            self.rear = self.front = new_node

            return

        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node


    def pop_front(self):

        if (self.front is None):
            print("Queue is empty")
            return

        if (self.front.next is None):
            temp_data = self.front.data
            temp_node = self.front
            self.front = None
            self.rear = None
            del temp_node
            return temp_data

        temp_data = self.front.data
        temp_node = self.front

        self.front = self.front.next
        self.front.prev = None

        del temp_node
        return temp_data


    def pop_rear(self):

        if (self.rear is None):
            print("Queue is empty")
            return

        if (self.rear == self.front):
            temp_data = self.rear.data
            temp_node = self.rear

            self.front = None
            self.rear = None

            del temp_node

            return temp_data


        temp_data = self.rear.data
        temp_node = self.rear

        self.rear = self.rear.prev

        self.rear.next = None

        del temp_node

        return temp_data
