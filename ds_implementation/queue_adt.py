
class Queue:
    queue = []
    length = 0

    def enqueue(self, x):
        self.queue.append(x)
        self.length+=1

    def dequeue(self):
        if (self.length > 0):
            temp = self.queue[0]
            del self.queue[0]
            self.length-=1
            return temp
        else:
            raise QueueError("Cannot Deque due to queue being empty")

    def peek(self):
        if (self.length > 0):
            return self.queue[0]
        else:
            print("No elements in queue")

    def is_empty(self):
        return True if self.length == 0 else False
    
    def size(self):
        return self.length
    
    def printAll(self):
        print(self.queue)


class QueueError(BaseException):
    err = ""
    def __init__ (self, x):
        self.err = x

    def getErr(self):
        return self.err