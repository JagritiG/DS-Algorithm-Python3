# Delete odd nodes from circular linked list
from circularlinkedlist.circular_singlylinkedlist import CSll


def delete_odd_nodes(cll):

    current = cll.head

    # traverse list till the end
    # if the node is odd then delete it
    while current:
        if current.data % 2 != 0:
            cll.remove(current.data)
            # current = current.next
        current = current.next
        if current is cll.head:
            break

    return cll.head


if __name__ == "__main__":

    cll = CSll()
    cll.add_at_first(12)
    cll.add_at_first(23)
    cll.add_at_first(32)
    cll.add_at_first(40)
    cll.add_at_first(51)
    cll.add_at_first(58)

    cll.print_cll()
    print("Linked list after odd nodes deletion: ")
    delete_odd_nodes(cll)
    cll.print_cll()

