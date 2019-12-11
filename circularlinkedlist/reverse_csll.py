# Reverse circular singly linked list
from circularlinkedlist.circular_singlylinkedlist import CSll


def reverse_csll(head):

    if not head:
            return print("Linked list is empty")

    current = head
    prev_node = None
    while current.next is not head:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
    current.next = prev_node
    prev_node = current
    head.next = prev_node
    csll.head = prev_node


if __name__ == "__main__":
    csll = CSll()
    csll.add_at_last(1)
    csll.add_at_last(2)
    csll.add_at_last(3)
    csll.add_at_last(4)
    print("Elements of linked list:")
    csll.print_cll()
    print("Head:")
    print(csll.head)
    print("Elements of reversed linked list:")
    reverse_csll(csll.head)
    csll.print_cll()
    print("Head after reversing:")
    print(csll)
