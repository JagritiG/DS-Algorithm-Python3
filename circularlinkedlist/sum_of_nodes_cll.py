# Sum of all the elements of the list
from circularlinkedlist.circular_singlylinkedlist import CSll


def sum_of_nodes(head):
    current = head
    sum = 0
    while current:
        sum += current.data
        current = current.next
        if current == head:
            break

    return sum


if __name__ == "__main__":
    csll = CSll()
    csll.add_at_last(1)
    csll.add_at_last(2)
    csll.add_at_last(3)
    csll.add_at_last(4)
    print("Elements of linked list:")
    csll.print_cll()
    print("\n")
    print("Sum of all the elements: " + str(sum_of_nodes(csll.head)))

