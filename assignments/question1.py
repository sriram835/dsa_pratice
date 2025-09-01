"""
Preamble:
create_alphabet_trail() - the function loops through 65 to 90 and covert 
        each integer to character using ASCII values and creates Tree Nodes
        as it goes.

print_list() - The function travsres the  entire linked list while printing
        each label of tree.

chirpy_journey() - The function firsts takes energy scroll as input.
        Then stores first energy value as energy_value. Then 
        the function deletes energy_value Tree nodes and skips 
        energy_value tree using two for loops and for each iteration,
        we check if we reached the end. If yes, we set reached_end to
        true and break the for loop. Using a if statement to check
        reached_end, we break the while.
"""

class Tree:
    def __init__(self):
        self.label_of_tree = None
        self.next_tree = None



class SinglyLinkedList:
    forest_head = Tree()
    energy_scroll = []


    @staticmethod
    def create_alphabet_trail():
        SinglyLinkedList.forest_head.label_of_tree = chr(65)
        SinglyLinkedList.forest_head.next_tree = Tree()
        temp_tree = SinglyLinkedList.forest_head

        for i in range(66,90+1):
            temp_tree = temp_tree.next_tree
            temp_tree.label_of_tree = chr(i)
            if (i == 90):
                temp_tree.next_tree = None
            else:
                temp_tree.next_tree = Tree()
                

        return SinglyLinkedList


    @staticmethod
    def print_list():
        temp_tree = SinglyLinkedList.forest_head

        if (temp_tree == None):
            print("Forest list does not have tree nodes. Now forest is a desert")
            return

        while (temp_tree != None):
            print(f"{temp_tree.label_of_tree} ->", end=" ")
            temp_tree = temp_tree.next_tree

        print("None")


    @staticmethod
    def chirpy_journey(energy_scroll):
        SinglyLinkedList.energy_scroll = energy_scroll
        dummy_head = Tree()
        dummy_head.next_tree = SinglyLinkedList.forest_head
        temp_tree = dummy_head

        energy_index = 0
        reached_end = False

        while (temp_tree != None):
            if (energy_index >= len(SinglyLinkedList.energy_scroll)):
                break
            energy_value = SinglyLinkedList.energy_scroll[energy_index]
            energy_index += 1

            for i in range(1,energy_value+1):
                if (temp_tree.next_tree == None):
                    reached_end = True
                    break

                dummy_tree = temp_tree.next_tree
                temp_tree.next_tree = temp_tree.next_tree.next_tree
                del dummy_tree

            if (reached_end == True):
                break

            for i in range(1, energy_value+1):
                if (temp_tree == None):
                    reached_end = True
                    break

                temp_tree = temp_tree.next_tree

            if (reached_end == True):
                break

        SinglyLinkedList.forest_head = dummy_head.next_tree
                


if __name__ == "__main__":
    print("=== Chirpy's Trail – The Vanishing Forest ===")
    forest = SinglyLinkedList.create_alphabet_trail()
    print("\nInitial Trail:")
    forest.print_list()
# Ask user for energy scroll
    user_input = input("\nEnter energy values separated by spaces (e.g., 3 5 2): ").strip()
    if user_input:
        try:
            energy_scroll = [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input. Using default energy scroll [3, 5, 2].")
            energy_scroll = [3, 5, 2]
    else:
        print("No input provided. Using default energy scroll [3, 5, 2].")
        energy_scroll = [3, 5, 2]
    print(f"\nEnergy Scroll: {energy_scroll}")
    forest.chirpy_journey(energy_scroll)
    print("\nFinal Trail:")
    forest.print_list()
