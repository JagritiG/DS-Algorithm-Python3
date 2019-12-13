# Rotate singly linked list
from singlylinkedlist.singly_linkedlist import Sll


def rotate_linkedlist(head, n):
    curr_1 = head
    curr_2 = head
    prev = None
    count = 0

    while curr_1 and count < n:
        prev = curr_1
        curr_1 = curr_1.next
        count += 1
    curr_1 = prev

    while curr_2.next is not None:
        curr_2 = curr_2.next

    curr_2.next = head
    sll.head = curr_1.next
    curr_1.next = None
    return sll.head


if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(3)
    sll.add_at_tail(4)
    sll.add_at_tail(5)
    sll.add_at_tail(6)
    print("List: ")
    sll.print_list()
    print("\n")
    print("List after rotation: ")
    n = 4
    rotate_linkedlist(sll.head, n)
    sll.print_list()
