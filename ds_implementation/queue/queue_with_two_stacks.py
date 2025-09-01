

class Queue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, data):
        self.stack_in.append(data)

    def dequeue(self):
        if (len(self.stack_out) == 0 and len(self.stack_in) == 0):
            print("Queue is empty")
            return

        if (len(self.stack_out) == 0):
            while (len(self.stack_in) > 0):
                self.stack_out.append(self.stack_in.pop())


        return self.stack_out.pop()

    
def test_queue():
    q = Queue()

    # Normal cases
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4

    # Single element
    q.enqueue(10)
    assert q.dequeue() == 10

    # Empty dequeue
    assert q.dequeue() is None  # Expect None or handled output

    # Dequeue from empty repeatedly
    assert q.dequeue() is None

    # Enqueue after emptying
    q.enqueue(5)
    assert q.dequeue() == 5

    # Enqueue identical elements
    q.enqueue(7)
    q.enqueue(7)
    assert q.dequeue() == 7
    assert q.dequeue() == 7

    # Large input test
    for i in range(10000):
        q.enqueue(i)
    for i in range(10000):
        assert q.dequeue() == i

    print("All test cases passed!")

test_queue()

