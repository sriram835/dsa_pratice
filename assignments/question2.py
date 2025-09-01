"""
Preamble:

add_visitor() - Adds a visitor to doubly linked list using tail pointer

remove_visitor() - Traverses through the list to find the given id. Once
        did, the node is removed. If the node to be deleted is head or tail,
        then the head or tail pointer is updated to remove the given node.

print_occupancy() - Goes through the entire list once. For each node we visit,
        we increment a counter and print the counter.

alternate_exit() - initializes dummy_head. where dummy_head.next_visitor = 
        visitor_list_head. temp_visitor is set to visitor_list_head.
        the previous  of temp_visitor is set to next visitor of temp_visitor
        and next visitor of temp_visitor is set to previous visitor of 
        temp_visitor. Then we jump two nodes using temp_visitor =
        temp_visitor.next_visitor.next_visitor

print_alphabetical() - Stores data in a tempory nested list, then 
        merge sort is used to sort tempory nested list. Finally,
        we print the data in tempory list that is now sorted.
"""


class Visitor:
    def __init__(self, inputed_visitor_id, inputed_visitor_name, inputed_ride_type):
        self.visitor_id = inputed_visitor_id
        self.visitor_name = inputed_visitor_name
        self.ride_type = inputed_ride_type
        self.next_visitor = None
        self.prev_visitor = None

class CarnivalRide:
    def __init__(self):
        self.visitor_list_head = None
        self.visitor_list_tail = None

    def add_visitor(self,inputed_visitor_id, inputed_visitor_name, inputed_ride_type):
        if (self.visitor_list_head == None):
            self.visitor_list_head = Visitor(inputed_visitor_id,inputed_visitor_name,inputed_ride_type)
            self.visitor_list_tail = self.visitor_list_head
            return

        temp_visitor = Visitor(inputed_visitor_id,inputed_visitor_name,inputed_ride_type)

        self.visitor_list_tail.next_visitor = temp_visitor
        temp_visitor.prev_visitor = self.visitor_list_tail

        self.visitor_list_tail = temp_visitor


    def remove_visitor(self, inputed_visitor_id):
        temp_visitor = self.visitor_list_head

        if (temp_visitor == None):
            print("No visitors in list")
            return

        if (self.visitor_list_head.visitor_id == inputed_visitor_id):
            if (self.visitor_list_head.next_visitor == None):
                del self.visitor_list_head
                self.visitor_list_head = None
                self.visitor_list_tail = None
                return
            dummy_to_be_deleted = self.visitor_list_head
            self.visitor_list_head = self.visitor_list_head.next_visitor
            self.visitor_list_head.prev_visitor = None
            del dummy_to_be_deleted

            return

        if (self.visitor_list_tail.visitor_id == inputed_visitor_id):
            self.visitor_list_tail = self.visitor_list_tail.prev_visitor
            del self.visitor_list_tail.next_visitor
            self.visitor_list_tail.next_visitor = None
            return

        is_found = False

        while (temp_visitor != None):
            if (temp_visitor.visitor_id == inputed_visitor_id):
                temp_visitor.prev_visitor.next_visitor = temp_visitor.next_visitor
                temp_visitor.next_visitor.prev_visitor = temp_visitor.prev_visitor
                del temp_visitor
                is_found = True
                break
            temp_visitor = temp_visitor.next_visitor

        if (is_found == False):
            print(f"{inputed_visitor_id} not found in list")

    def print_occupancy(self):
        count = 0

        temp_visitor = self.visitor_list_head

        while (temp_visitor != None):
            count+=1
            temp_visitor = temp_visitor.next_visitor

        print(f"Total Occupancy: {count}")
        print()


    def alternate_exit(self):
        if (self.visitor_list_head == None):
            print("List is empty")
            return

        print("Visitors exiting at alternate positions:")

        if (self.visitor_list_head.next_visitor == None):
            print(f"Visitor Exiting: {self.visitor_list_head.visitor_name}")
            del self.visitor_list_head
            self.visitor_list_head = None
            self.visitor_list_tail = None
            return

        dummy_head = Visitor(0,"","")
        dummy_head.next_visitor = self.visitor_list_head
        self.visitor_list_head.prev_visitor = dummy_head

        temp_visitor = self.visitor_list_head

        while (temp_visitor != None):

            temp_visitor.prev_visitor.next_visitor = temp_visitor.next_visitor

            if (temp_visitor == self.visitor_list_tail ):
                self.visitor_list_tail = self.visitor_list_tail.prev_visitor
                print(f"Visitor Exiting: {temp_visitor.visitor_name}")
                del self.visitor_list_tail.next_visitor
                self.visitor_list_tail.next_visitor = None
                break


            temp_visitor.next_visitor.prev_visitor = temp_visitor.prev_visitor
            print(f"Visitor Exiting: {temp_visitor.visitor_name}")

            if (temp_visitor.next_visitor.next_visitor == None):
                del temp_visitor
                break

            dummy_visitor_to_be_deleted = temp_visitor
            temp_visitor = temp_visitor.next_visitor.next_visitor

            del dummy_visitor_to_be_deleted

        self.visitor_list_head = dummy_head.next_visitor
        print()


    def merger(self,left_arr, right_arr):
        left_arr_pointer = 0
        right_arr_pointer = 0

        result_arr = []

        while (left_arr_pointer < len(left_arr) and right_arr_pointer < len(right_arr)):
            if (left_arr[left_arr_pointer][1] < right_arr[right_arr_pointer][1]):
                result_arr.append(left_arr[left_arr_pointer])
                left_arr_pointer+=1
            else:
                result_arr.append(right_arr[right_arr_pointer])
                right_arr_pointer+=1

        while (left_arr_pointer < len(left_arr)):
            result_arr.append(left_arr[left_arr_pointer])
            left_arr_pointer+=1

        while (right_arr_pointer < len(right_arr)):
            result_arr.append(right_arr[right_arr_pointer])
            right_arr_pointer+=1

        return result_arr
    
    def merge_sort(self, visitor_list):
        if (len(visitor_list) <= 1):
            return visitor_list

        mid_point = len(visitor_list)//2

        left_arr = visitor_list[:mid_point]
        right_arr = visitor_list[mid_point:]

        new_left_arr = self.merge_sort(left_arr)
        new_right_arr = self.merge_sort(right_arr)

        return self.merger(new_left_arr, new_right_arr)


    def print_alphabetical(self):
        temp_visitor_list = []

        if (self.visitor_list_head == None):
            print("No visitors in list")
            return

        temp_visitor_node = self.visitor_list_head

        while (temp_visitor_node != None):
            temp_visitor_list.append([temp_visitor_node.visitor_id,temp_visitor_node.visitor_name,temp_visitor_node.ride_type])
            temp_visitor_node = temp_visitor_node.next_visitor

        temp_visitor_list = self.merge_sort(temp_visitor_list)

        for i in range(len(temp_visitor_list)):
            print(f"Visitor ID: {temp_visitor_list[i][0]}, Name: {temp_visitor_list[i][1]}, Type: {temp_visitor_list[i][2]}")

        print()
        

if __name__ == "__main__":
    ride = CarnivalRide()
    
    while True:
        command = input().strip()
        if not command:
            continue


        if command == 'ALT':
            ride.alternate_exit()
        elif command[0] == 'A':
            parts = command.split()
            visitor_id, name, ride_type = int(parts[1]), parts[2], parts[3]
            ride.add_visitor(visitor_id, name, ride_type)
        elif command[0] == 'R':
            _, visitor_id = command.split()
            ride.remove_visitor(int(visitor_id))
        elif command == 'P':
            ride.print_alphabetical()
        elif command == 'O':
            ride.print_occupancy()
        elif command == 'END':
            break


