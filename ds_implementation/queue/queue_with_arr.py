
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, size):
        self.capacity = size
        self.front = None
        self.rear = None
        self.length = 0

    def push(self, data):

        if (self.length == self.capacity):

            print("Capacity of queue is reached")
            return

        new_node = Node(data)
        if (self.front == None):
            self.front = self.rear = new_node
            self.length +=1
            return

        self.rear.next = new_node
        self.rear = new_node
        self.length+=1

    def pop(self):
        if (self.front == None):
            print("Queue is empty")
            return


        temp = self.front
        if (self.front.next is None):
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next


        temp_data = temp.data
        del temp
        self.length-=1
        return temp_data


    def top(self):

        if (self.front == None):
            print("Queue is empty")
            return

        return self.front.data

    def isEmpty(self):
        return self.length == 0

        

        

        

