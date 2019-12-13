# Concatenate two singly linked lists
from singlylinkedlist.singly_linkedlist import Sll


def concatenate_two_llist(head1, head2):

    curr_1 = head1
    curr_2 = head2
    while curr_1.next is not None:
        curr_1 = curr_1.next
    curr_1.next = curr_2
    return curr_1


if __name__ == "__main__":

    sll1 = Sll()
    sll1.add_at_tail(1)
    sll1.add_at_tail(2)
    sll1.add_at_tail(3)
    sll1.add_at_tail(4)

    sll2 = Sll()
    sll2.add_at_tail(5)
    sll2.add_at_tail(6)
    sll2.add_at_tail(7)
    sll2.add_at_tail(8)
    print("List1: ")
    sll1.print_list()
    print("List2: ")
    sll2.print_list()
    print("\n")
    print("List after concatenation: ")
    concatenate_two_llist(sll1.head, sll2.head)
    sll1.print_list()
