# Remove duplicates from a singly linked list
from singlylinkedlist.singly_linkedlist import Sll


def remove_duplicates(head):

    current = head
    previous = None

    duplicates = dict()

    while current:
        if current.data in duplicates:
            # Remove
            previous.next = current.next
            current = None
        else:
            # If first occurrence, store data in a dictionary
            duplicates[current.data] = 1
            previous = current
        current = previous.next



if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(3)
    sll.add_at_tail(2)
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(1)
    sll.add_at_tail(4)
    print("List: ")
    sll.print_list()
    print("\n")
    print("List after removing duplicates: ")
    remove_duplicates(sll.head)
    sll.print_list()
