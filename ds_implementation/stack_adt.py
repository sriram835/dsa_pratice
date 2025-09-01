
class Stack:
    stack=[]
    length = 0

    def push(self, x):
        self.stack.append(x)
        self.length+=1
    
    def pop(self):
        if (self.length > 0):
            temp = self.stack[-1]
            del self.stack[-1]
            self.length-=1        
            return temp
        else:
            raise StackError("popping from empty stack")    
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return True if self.length == 0 else False
    
    def size(self):
        return self.length
    
    def printAll(self):
        print(self.stack)
        

class StackError(BaseException):
    err = ""
    def __init__ (self, x):
        self.err = x

    def getErr(self):
        return self.err
