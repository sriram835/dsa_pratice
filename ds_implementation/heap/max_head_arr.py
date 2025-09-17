

class MaxHeap:
    def __init__(self):
        self.data = []

    def parentIndex(self, i):
        if i < 1:
            return None
        return (i-1)//2

    def leftChildIndex(self,i):
        if 2*i + 1 > len(self.data)-1:
            return None
        return 2*i + 1

    def rightChildIndex(self,i):
        if 2*i + 2 > len(self.data)-1:
            return None
        return 2*i + 2

    def insert(self, data):
        self.data.append(data)
        self.heapifyUp(len(self.data)-1)

    def heapifyUp(self, index):

        par = self.parentIndex(index)
        child = index

        while (par is not None):
            if (self.data[par] > self.data[child]):
                break

            self.data[par], self.data[child] = self.data[child], self.data[par]

            child = par
            par = self.parentIndex(child)



    def delete(self):

        if (len(self.data) == 0):
            print("heap is empty")
            return
        
        res = self.data[0]

        child = self.data[len(self.data)-1]

        self.data[0] = child
        self.data.pop()

        self.heapifyDown(0)
        return res

    def heapifyDown(self, index):

        maxChild = self.leftChildIndex(index)
        rightChild = self.rightChildIndex(index)

        if (rightChild is not None and self.data[maxChild] < self.data[rightChild]):
            maxChild = rightChild

        par = index

        while (maxChild is not None):
            
            if (rightChild is not None and self.data[maxChild] < self.data[rightChild]):
                maxChild = rightChild

            if (self.data[maxChild] < self.data[par]):
                break

            self.data[maxChild], self.data[par] = self.data[par], self.data[maxChild]

            par = maxChild
            maxChild = self.leftChildIndex(par)
            rightChild = self.rightChildIndex(par)



    def Heapify(self, arr):
        self.data = [i for i in arr]
        
        for i in range((len(self.data)//2)-1,-1,-1):
            self.heapifyDown(i)



            



        


h = MaxHeap()

# Insert and delete in order
for x in [3, 1, 6, 5, 2, 4]:
    h.insert(x)
print(h.data)   # [6, 5, 4, 3, 2, 1] (valid heap)

while h.data:
    print(h.delete(), end=" ")  # 6 5 4 3 2 1

# Build heap from array
h.Heapify([1, 2, 3, 4, 5, 6, 7])
print(h.data)   # [7, 5, 6, 4, 2, 1, 3]
