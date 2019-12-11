# Min and max in a circular linked list
from circularlinkedlist.circular_singlylinkedlist import CSll


def find_min(cll):

    current = cll.head
    min_node = cll.head.data     # Initialize min node
    if cll.head is None:
        return "List is empty."
    else:
        while True:
            if min_node > current.data:
                min_node = current.data

            current = current.next
            if current is cll.head:
                break

    return min_node


def find_max(cll):
    current = cll.head
    max_node = cll.head.data     # Initialize min node
    if cll.head is None:
        return "List is empty."
    else:
        while True:
            if max_node < current.data:
                max_node = current.data

            current = current.next
            if current is cll.head:
                break

    return max_node


if __name__ == "__main__":

    cll = CSll()
    cll.add_at_first(11)
    cll.add_at_first(21)
    cll.add_at_first(3)
    cll.add_at_first(10)
    cll.add_at_first(20)
    cll.print_cll()
    print("Minimum: " + str(find_min(cll)))
    print("Maximum: " + str(find_max(cll)))

