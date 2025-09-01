class Node:
    next = None
    val = None
    prev = None

    def __init__(self, val):
        self.val = val


head = Node(1)
tail = head

if (head.val == 1):
    dummy = head
    head = head.next
    del dummy

if (tail.val == 1):
    dummy = tail
    tail = tail.prev
    del dummy


print(tail)
