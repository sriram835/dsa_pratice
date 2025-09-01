

class Queue:
    def __init__(self, capacity):
        self.arr = [0]*capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0

    def getFront(self):
        if (self.size == 0):
            print("Queue is empty")
            return None

        return self.arr[self.front]

    def getRear(self):
        if (self.size == 0):
            print("Queue is empty")
            return None

        rear = (self.front + self.size-1)%self.capacity
        return self.arr[rear]

    def enqueue(self, data):
        
        if (self.size == self.capacity):
            print("Queue overflow")
            return None

        rear = (self.front + self.size)%self.capacity
        self.arr[rear] = data
        self.size+=1

    def dequeue(self):

        if (self.size == 0):
            print("Queue is empty")
            return None

        res = self.arr[self.front]

        self.front = (self.front+1)%self.capacity
        self.size-=1 
        return res

