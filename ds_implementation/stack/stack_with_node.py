

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length= 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length+=1


    def pop(self):
        if (self.length == 0):
            raise IndexError("Stack is empty")

        temp_node = self.head
        temp_data = self.head.data
        self.head = self.head.next
        self.length-=1
        del temp_node
        return temp_data


    def top(self):
        if (self.length == 0):
            raise IndexError("Stack is empty")

        return self.head.data

    def isEmpty(self):
        return self.length == 0

def main():
    stack = Stack()
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Top")
        print("4. Check if Empty")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                data = input("Enter value to push: ")
                stack.push(data)
                print(f"Pushed {data} onto stack.")

            elif choice == "2":
                print(f"Popped {stack.pop()} from stack.")

            elif choice == "3":
                print(f"Top element: {stack.top()}")

            elif choice == "4":
                print("Stack is empty." if stack.isEmpty() else "Stack is NOT empty.")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please try again.")

        except IndexError as e:
            print(f"Error: {e}")   # handle errors gracefully


if __name__ == "__main__":
    main()

