# Check if a list is circular linked list or not
from circularlinkedlist.circular_singlylinkedlist import CSll
from singlylinkedlist.singly_linkedlist import Sll


def is_circular_linkedlist(input_list):
    current = input_list.head
    while current.next:
        current = current.next
        if current.next == input_list.head:
            return True
    return False


if __name__ == "__main__":

    s = Sll()
    s.add_at_head(1)
    s.add_at_head(2)
    s.add_at_head(3)
    s.add_at_head(4)

    cll = CSll()
    cll.add_at_first(1)
    cll.add_at_first(2)
    cll.add_at_first(3)
    cll.add_at_first(4)

    print(is_circular_linkedlist(s))
    print(is_circular_linkedlist(cll))


