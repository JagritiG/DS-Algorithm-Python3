# Swap nodes in singly linked list
from singlylinkedlist.singly_linkedlist import Sll


def swap_nodes(sll, key_1, key_2):

    # If both keys are of same value
    if key_1 == key_2:
        return

    # Traverse the list and find both keys
    curr_1 = sll.head
    prev_1 = None
    while curr_1 and curr_1.data != key_1:
        prev_1 = curr_1
        curr_1 = curr_1.next

    curr_2 = sll.head
    prev_2 = None
    while curr_2 and curr_2.data != key_2:
        prev_2 = curr_2
        curr_2 = curr_2.next

    # If both or one of the keys are not present
    if not key_1 or not key_2:
        return

    # If both keys are present
    if prev_1:               # If not head node
        prev_1.next = curr_2
    else:                    # If head node
        sll.head = curr_2

    if prev_2:               # If not head node
        prev_2.next = curr_1
    else:                    # If head node
        sll.head = curr_1

    curr_1.next, curr_2.next = curr_2.next, curr_1.next


if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail("A")
    sll.add_at_tail("B")
    sll.add_at_tail("C")
    sll.add_at_tail("D")
    print("List: ")
    sll.print_list()
    print("\n")
    print("List after swaping: ")
    swap_nodes(sll, "A", "C")
    sll.print_list()

