import random


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data 


def generate_random_linked_list(n):
    dummy = Node(0)
    curr_ptr = dummy

    for i in range(n):
        data = random.randint(1,10)
        curr_ptr.next = Node(data)
        curr_ptr = curr_ptr.next

    return dummy.next

def print_linked_list(head):
    curr_ptr = head
    while (curr_ptr):
        print(f"{curr_ptr.data}", end=" ")
        curr_ptr = curr_ptr.next

    print()


head = generate_random_linked_list(10)


def merger(left, right):
    dummy = Node(0)
    curr_ptr = dummy

    while (left != None and right != None):
        if (left.data < right.data):
            temp = Node(left.data)
            left = left.next
            curr_ptr.next = temp
            curr_ptr = curr_ptr.next

        else:
            temp = Node(right.data)
            right = right.next
            curr_ptr.next = temp
            curr_ptr = curr_ptr.next

    while (left != None):
        temp = Node(left.data)
        left = left.next
        curr_ptr.next = temp
        curr_ptr = curr_ptr.next

    while (right != None):
        temp = Node(right.data)
        right = right.next
        curr_ptr.next = temp
        curr_ptr = curr_ptr.next

    return dummy.next


def merge_sort(head):
    if (head == None or head.next == None):
        return head

    slow = head
    fast = head
    temp = head


    while (fast != None and fast.next != None):
        temp = slow
        slow = slow.next
        fast = fast.next.next
    
    temp.next = None


    left_side = merge_sort(head)
    right_side = merge_sort(slow)

    return merger(left_side, right_side)


head = generate_random_linked_list(10)
print_linked_list(head)
new_head = merge_sort(head)
print_linked_list(new_head)
