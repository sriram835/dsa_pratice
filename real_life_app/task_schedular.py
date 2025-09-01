

class Task:
    def __init__(self, task_id, task_name, task_type):
        self.next = None
        self.prev = None
        self.task_id = task_id
        self.task_name = task_name
        self.task_type = task_type


class TaskManager:
    def __init__(self):
        self.head= None
        self.tail = None


    def add_task(self, task_id, task_name, task_type):
        if (self.head == None):
            self.head = Task(task_id, task_name, task_type)
            self.tail = self.head

        else:
            new_node = Task(task_id, task_name, task_type)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        print(f"Task {task_id} ({task_name}-{task_type}) added")

    def remove_task(self, task_id):
        curr_ptr = self.head
        is_found = False

        while (curr_ptr):
            if (curr_ptr.task_id == task_id):
                is_found = True
                curr_ptr.prev.next = curr_ptr.next
                curr_ptr.next.prev = curr_ptr.prev
                break
        
            curr_ptr = curr_ptr.next


        if (is_found):
            print(f"Task {task_id} removed")
        else:
            print(f"Task {task_id} not found")
        
    
    def print_in_order(self):
        curr_ptr = self.head
        if (curr_ptr == None):
            print("Task list is empty")
            return
        
        while (curr_ptr):
            print(f"{curr_ptr.task_id} {curr_ptr.task_name} {curr_ptr.task_type}")
            curr_ptr = curr_ptr.next

    def print_in_reverse(self):
        curr_ptr = self.tail
        if (curr_ptr == None):
            print("Task list is empty")
            return
        
        while (curr_ptr):
            print(f"{curr_ptr.task_id} {curr_ptr.task_name} {curr_ptr.task_type}")
            curr_ptr = curr_ptr.prev



task_manager = TaskManager()

n = int(input())
commands = []
for i in range(n):
    command_as_string = input()
    command = command_as_string.split(' ')
    commands.append(command)



for command in commands:
    match(command[0]):
        case 'A':
            task_manager.add_task(command[1], command[2], command[3])
        case 'P':
            task_manager.print_in_order()
        case 'R':
            task_manager.remove_task(command[1])
        case 'REV':
            task_manager.print_in_reverse()
