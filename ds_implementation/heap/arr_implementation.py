

class Heap:
    def __init__(self):
        self.data = []


    def getParentIndex(self,i):
        index = (i-1)//2
        if (index < 0):
            print("No parent")
            return None

        return index


    def getLeftChildIndex(self,i):
        if (2*i + 1 >= len(self.data)):
            print("No left child")
            return None

        return 2*i + 1

    def getRightChildIndex(self,i):
        if (2*i + 2 >= len(self.data)):
            print("No right child")
            return None

        return 2*i + 2

    def swap(self, index1, index2):
        if (index1 >= len(self.data) or index2 >= len(self.data)):
            print("Index out of bounds")
            return

        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]
        
    def getParent(self,i):
        index = self.getParentIndex(i)
        if (index == None):
            return None

        return self.data[index]


    def getLeftChild(self,i):
        index = self.getLeftChildIndex(i)
        if (index == None):
            return None

        return self.data[index]

    def getRightChild(self,i):
        index = self.getRightChildIndex(i)
        if (index == None):
            return None

        return self.data[index]

    def peek(self):
        if (len(self.data) == 0):
            print("heap is empty")
            return None

        return self.data[0]

    def poll(self):
        if (len(self.data) == 0):
            print("heap is empty")
            return None

        item = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        self.data.pop()
        self.heapifyDown()
        return item

    def add(self, data):
        self.data.append(data)
        self.heapifyUp()
        

    def heapifyUp(self):
        index = len(self.data)-1

        while (self.getParentIndex(index) is not None and self.getParent(index) > self.data[index]):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)


    def heapifyDown(self):
        index = 0
        while (self.getLeftChildIndex(index) is not None):
            smallerIndex = self.getLeftChildIndex(index)
            if (self.getRightChildIndex(index) is not None and self.data[self.getRightChildIndex(index)] < self.data[smallerIndex]):
                smallerIndex = self.getRightChildIndex(index)

            if (self.data[index] < self.data[smallerIndex]):
                break
            else:
                self.swap(index,smallerIndex)
                index = smallerIndex


    def print_heap(self):
        if  len(self.data) == 0:
            print("Heap is empty")
        else:
            print("Current heap:", self.data)

def main():
    h = Heap()
    while True:
        print("\nOptions:")
        print("1. Add element")
        print("2. Remove min (poll)")
        print("3. Print heap")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to add: "))
            h.add(val)
        elif choice == '2':
            removed = h.poll()
            if removed is not None:
                print(f"Removed: {removed}")
        elif choice == '3':
            h.print_heap()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

        




