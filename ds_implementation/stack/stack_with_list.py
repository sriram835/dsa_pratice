


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = [0]*capacity
        self.mytop = -1


    def push(self, data):
        if (self.mytop + 1 >= self.capacity):
            print("\nStack overflow\n")
            return

        self.mytop+=1
        self.list[self.mytop] = data
        print(f"\nInserted {data} in stack\n")

        
    def top(self):
        if (self.mytop == -1):
            print("\nStack is empty\n")
            return None
        
        return self.list[self.mytop]

    def pop(self):
        if (self.mytop == -1):
            print("\nStack is empty\n")
            return None

        element = self.list[self.mytop]
        self.mytop-=1
        return element






if (__name__ == "__main__"):
    size = int(input("Enter the capacity of stack: "))
    myStack = Stack(size)

    choice = -1

    while (True):

        print("1. Insert Element\n2. Top\n3. Pop\n4. Exit")
        choice = int(input("Enter choice: "))

        
        match (choice):
            case 1:
                data = input("Enter data: ")
                myStack.push(data)
                
            case 2:
                data = myStack.top()
                print(f"\nTop element = {data}\n")
            
            case 3:
                data = myStack.pop()
                print(f"\nPop element = {data}\n")

            case 4:
                exit()

            case _:
                print("Invalid data")

            
