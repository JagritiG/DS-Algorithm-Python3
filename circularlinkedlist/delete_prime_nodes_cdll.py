# Delete prime nodes from circular linked list
from circularlinkedlist.circular_doublylinkedlist import CDll


def delete_prime_nodes(cll):

    current = cll.head
    while current:
        if is_prime(current.data):
            cll.remove(current.data)
            current = current.next
        current = current.next
        if current is cll.head:
            break
    return cll.head


def is_prime(val):

    if val <= 1:
        return False

    for i in range(2, val):
        if val % i == 0:
            return False

    return True


if __name__ == "__main__":

    cll = CDll()
    cll.add_at_first(22)
    cll.add_at_first(23)
    cll.add_at_first(30)
    cll.add_at_first(37)
    cll.add_at_first(49)
    cll.add_at_first(53)

    cll.print_cdll()
    print("Linked list after prime nodes deletion: ")
    delete_prime_nodes(cll)
    cll.print_cdll()
