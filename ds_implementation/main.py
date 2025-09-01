from stack_adt import *
from queue_adt import *
from set_adt import *

def test_stack():
    try:
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        stack.printAll()
        print(stack.peek())
        print(stack.size())
        stack.pop()
        stack.printAll()
        print(stack.peek())
        print(stack.size())
        print(stack.is_empty())
        stack.pop()
        stack.pop()
        print(stack.is_empty())
        stack.pop()
    except StackError as e:
        print("ERR: "+e.getErr())

def test_queue():
    try:
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        queue.printAll()
        print(queue.peek())
        queue.dequeue()
        queue.printAll()
        print(queue.size())
        print(queue.is_empty())
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
    except QueueError as e:
        print("ERR: "+e.getErr())

def test_set():
    try:
        my_set = Set()
        my_set2 = Set()
        my_set2.add(1)
        my_set2.add(20)
        my_set2.add(50)
        my_set.add(10)
        my_set.add(20)
        my_set.add(30)
        my_set.add(10)
        my_set.printAll()
        print(my_set.contains(10))
        print(my_set.contains(40))
        my_set.remove(30)
        my_set.printAll()
        new_set = my_set.union(my_set2)
        
        print("set1: ", end="")
        my_set.printAll()
        
        print("set2: ", end="")
        my_set2.printAll()
        
        print("Union: ",end="")
        new_set.printAll()
        
        new_set = my_set.intersection(my_set2)
        print("Intersection: ",end ="")
        new_set.printAll()
        
        new_set = my_set.difference(my_set2)
        print("Difference: ", end="")
        new_set.printAll()

        my_set.remove(100)
    except SetError as e:
        print("ERR: "+e.getErr())

test_stack()
test_queue()
test_set()
