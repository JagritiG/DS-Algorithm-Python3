# Merge two sorted singly linked lists
from singlylinkedlist.singly_linkedlist import Sll


def merge_two_sorted_llist(head1, head2):

    curr_1 = head1
    curr_2 = head2
    temp = None
    new_head = None

    if not curr_1:
        return curr_2
    if not curr_2:
        return curr_1

    # Set new head for merged lists
    if curr_1 and curr_2:
        if curr_1.data <= curr_2.data:
            temp = curr_1
            curr_1 = temp.next
        else:
            temp = curr_2
            curr_2 = temp.next
        new_head = temp

    # Traverse two lists, compare, and merge them
    while curr_1 and curr_2:
        if curr_1.data <= curr_2.data:
            temp.next = curr_1
            temp = curr_1
            curr_1 = temp.next
        else:
            temp.next = curr_2
            temp = curr_2
            curr_2 = temp.next

    if not curr_1:
        temp.next = curr_2
    if not curr_2:
        temp.next = curr_1
    return new_head


if __name__ == "__main__":

    sll1 = Sll()
    sll1.add_at_tail(3)
    sll1.add_at_tail(4)
    sll1.add_at_tail(6)
    sll1.add_at_tail(8)

    sll2 = Sll()
    sll2.add_at_tail(1)
    sll2.add_at_tail(2)
    sll2.add_at_tail(5)
    sll2.add_at_tail(7)
    print("List1: ")
    sll1.print_list()
    print("List2: ")
    sll2.print_list()
    print("\n")
    print("List after merging: ")
    new_head = merge_two_sorted_llist(sll1.head, sll2.head)
    if sll1.head == new_head:
        sll1.print_list()
    else:
        sll2.print_list()


