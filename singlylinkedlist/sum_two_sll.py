# Sum of two singly linked lists
from singlylinkedlist.singly_linkedlist import Sll


def sum_two_llist(head1, head2):

    curr_1 = head1
    curr_2 = head2

    # Create a new linked list
    new_llist = Sll()
    carry = 0

    while curr_1 and curr_2:
        if not curr_1:
            i = 0
        else:
            i = curr_1.data
        if not curr_2:
            j = 0
        else:
            j = curr_2.data

        sum_of_lists = i + j + carry
        if sum_of_lists >= 10:
            carry = 1
            remainder = sum_of_lists % 10
            new_llist.add_at_tail(remainder)
        else:
            carry = 0
            new_llist.add_at_tail(sum_of_lists)

        if curr_1:
            curr_1 = curr_1.next
        if curr_2:
            curr_2 = curr_2.next

    if carry > 0:
        new_llist.add_at_tail(carry)

    new_llist.print_list()


if __name__ == "__main__":

    sll1 = Sll()
    sll1.add_at_tail(4)
    sll1.add_at_tail(7)
    sll1.add_at_tail(3)

    sll2 = Sll()
    sll2.add_at_tail(7)
    sll2.add_at_tail(8)
    sll2.add_at_tail(7)
    print("List1: ")
    sll1.print_list()
    print("List2: ")
    sll2.print_list()
    print("\n")
    print("Sum of two lists: ")
    sum_two_llist(sll1.head, sll2.head)
