# Reverse circular doubly linked list
from circularlinkedlist.circular_doublylinkedlist import CDll


def reverse_cdll(head):

    if not head:
            return print("Linked list is empty")

    current = head
    temp = head
    while temp.next is not head:
            temp = temp.next
    prev_node = temp

    while current.next is not head:
        next_node = current.next
        current.next = prev_node
        prev_node.prev = current
        prev_node = current
        current = next_node
    current.next = prev_node
    prev_node.prev = current
    prev_node = current
    head.next = prev_node
    prev_node.prev = head
    cdll.head = prev_node


if __name__ == "__main__":
    cdll = CDll()
    cdll.add_at_first(1)
    cdll.add_at_first(2)
    cdll.add_at_first(3)
    cdll.add_at_first(4)
    print("Head:")
    print(cdll.head)
    print("Elements of linked list:")
    cdll.print_cdll()
    print("\n")
    print("Head after reversing:")
    reverse_cdll(cdll.head)
    print(cdll.head)
    print("Elements of reversed linked list:")
    cdll.print_cdll()

