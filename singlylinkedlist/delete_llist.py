# Delete singly linked list
from singlylinkedlist.singly_linkedlist import Sll


def delete_llist(head):

    current = head

    while current:
            prev = current.next
            del current.data
            current = prev


if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(3)
    sll.add_at_tail(4)

    print("List1: ")
    sll.print_list()
    print("\n")
    print("Delete linked list: ")
    delete_llist(sll.head)
    print("Linked list deleted")
