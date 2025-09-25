class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class RobotSystem:
    def __init__(self):
        self.queue= []
        self.bst = None

    def getParent(self, index):
        if (index == 0):
            return None
        return (index-1)//2
    
    def getLeftChild(self, index):
        if (2*index + 1 > len(self.queue)-1):
            return None
        return 2*index + 1
    
    
    def getRightChild(self, index):
        if (2*index + 2 > len(self.queue)-1):
            return None
        return 2*index + 2
    
    def addDelivery(self, id, priority,location):
        data = [id,priority,location]
        index = self._insertHeap(data)
        self._insertBst(id,index)

    def _insertBst(self, id, index):
        if self.bst is None:
            self.bst = Node([id,index])

        curr = self.bst
        while (True):
            if (id == curr.data[0]):
                return
            if (id < curr.data[0]):
                if curr.left is None:
                    curr.left = Node([id,index])
                    return
                curr = curr.left
                
            if (id > curr.data[0]):
                if curr.right is None:
                    curr.right = Node([id,index])
                    return
                curr = curr.right

            

    def _insertHeap(self, arr):
        self.queue.append(arr)
        index = self._heapifyUp(len(self.queue)-1)
        return index

    def _heapifyUp(self,i):
        curr = i
        while (True):
            par = self.getParent(curr)
            if (par is None):
                break

            if (self.queue[par][1] > self.queue[curr][1]):
                break

            self.queue[par], self.queue[curr] = self.queue[curr], self.queue[par]
            self._updateBstIndex(self.queue[curr][0],curr)
            curr = par

        self._updateBstIndex(self.queue[curr][0],curr)

        return curr
    
    
    def _deleteRootHeap(self):
        data = self.queue[0]
        self.queue[0] = self.queue[len(self.queue)-1]
        self.queue.pop()
        print(f"Robot is send to delivery for id: {data[0]}, priority: {data[1]}, location{data[2]}")
        if (len(self.queue)==0 ):
            return None
        index = self._heapifyDown(0)

        return index


    def _heapifyDown(self, index):
        par = index
        while (True):
            maxChild = self.getLeftChild(index)
            if maxChild is None:
                break

            rightChild = self.getRightChild(index)
            if (rightChild is not None):  
                if (self.queue[maxChild][1] < self.queue[rightChild][1]):
                    maxChild = rightChild

            if (self.queue[par][1] > self.queue[maxChild][1]):
                break

            self.queue[par], self.queue[maxChild] = self.queue[maxChild], self.queue[par]
            self._updateBstIndex(self.queue[par][0],par)
            par = maxChild

        self._updateBstIndex(self.queue[par][0],par)
        return par

    def SendRobot(self):
        if (len(self.queue) == 0):
            print("No Deliveries to be made")
            return
        self._deleteBst(self.queue[0][0])
        self._deleteRootHeap()

    def _deleteBst(self, id):
        data = self._findNode(id)
        if (data == [None,None]):
            print("Id not found")
            return


        if (data[0] == None):
            node = data[1]
            if node.left is None and node.right is None:
                self.bst = None
                return

            if (node.left is None):
                self.bst = node.right
                return

            if (node.right is None):
                self.bst = node.left
                return

            data1 = self._predecessor(node)
            self.bst.data = data1

        par = data[0]
        node = data[1]

        if (node.left is None and node.right is None):
            if (par.left == node):
                par.left = None
            else:
                par.right = None
            return

        if (node.left is None or node.right is None):
            if node.left is None:
                if (par.right == node):
                    par.right = node.right
                else:
                    par.left = node.right
            else:
                if (par.right == node):
                    par.right = node.left
                else:
                    par.left = node.left
            return

        new_data = self._predecessor(node)
        node.data = new_data

    def _predecessor(self,node):
        par = node
        res = node.left

        while (res.right):
            par = res
            res = res.right

        temp = res
        if (par.right == res):
            par.right = None
        else:
            par.left = None

        return temp.data

    def _findNode(self,id):
        curr = self.bst
        if (curr.data[0] == id):
            return [None,curr]

        while (True):
            if (curr is None):
                return [None,None]
            
            if (curr.left is not None and curr.left.data[0] == id):
                return [curr,curr.left]
            if (curr.right is not None and curr.right.data[0] == id):
                return [curr,curr.right]
            
            if (curr.data[0] > id):
                curr = curr.left

            if (curr.data[0] < id):
                curr = curr.right


    def _updateBstIndex(self, id, index):
        if (self.bst.data[0] == id):
            self.bst.data[1] = index
            return
        
        curr = self.bst
        while (True):
            if (curr is None):
                break

            if (curr.data[0] == id):
                curr.data[1] = index
                break

            if (curr.data[0] < id):
                curr = curr.right

            if (curr.data[0] > id):
                curr = curr.left

    def update_order(self, id,location):
        if (self.bst == None):
            print("No orders exist")
            return
        data = self._findNode(id)
        if data == [None,None]:
            print("Id not in data")
            return

        index = data[1].data[1]
        self.queue[index][2] = location


    def cancel_order(self,id):
        if (len(self.queue) == 0):
            print("No Deliveries to be made")
            return
        self._deleteBst(id)
        self._deleteNodeHeap(id)

    def _deleteNodeHeap(self, id):

        index = 0
        while (index < len(self.queue)):
            if (self.queue[index][0] == id):
                break
            index+=1

        if (index == len(self.queue)):
            print("Order not found")
            return

        temp = self.queue[index]
        self.queue[index] = self.queue[-1]
        self.queue.pop()
        self._heapifyDown(index)
        self._heapifyUp(index)
        print(f"The order is cancelled. ID: {temp[0]}, Priority: {temp[1]}, Location: {temp[2]}")


    def get_level_order_bst(self):
        res = []

        que = []

        if (self.bst is None):
            return res

        que.append(self.bst)
        
        while (len(que) > 0):
            curr = que.pop(0)


            if curr is None:
                res.append(None)
                continue

            res.append(curr.data[0])
            que.append(curr.left)
            que.append(curr.right)


        return res





        








        



            
            
if __name__ == "__main__":
    robot = RobotSystem()

    while (True):
        print("1. Enter a node\n2. Send a robot\n3. Update a order\n4. Cancel a order\n5. Look up details of order\n6. Print orders\n7. exit")
        choice = int(input("Enter your choice: "))
        match (choice):
            case 1:
                id = int(input("Enter the id: "))
                priority = int(input("Enter the priority: "))
                location = input("Enter location")
                robot.addDelivery(id,priority,location)
                
            case 2:
                robot.SendRobot()

            case 3:
                id = int(input("Enter the id: "))
                location = input("Enter the location")

                robot.update_order(id,location)

            case 4:
                id = int(input("Enter the id: "))
                robot.cancel_order(id)

            case 6:
                print(f"Queue: {robot.queue}")
                print(f"BST: {robot.get_level_order_bst()}")

            case 7:
                break

            case _:
                print("Invalid input")

        
