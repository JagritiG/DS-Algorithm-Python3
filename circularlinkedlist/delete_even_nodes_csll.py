# Delete even nodes from circular linked list
from circularlinkedlist.circular_singlylinkedlist import CSll


def delete_even_nodes(cll):

    current = cll.head

    # traverse list till the end
    # if the node is even then delete it
    while current:
        if current.data % 2 == 0:
            cll.remove(current.data)
            current = current.next
        current = current.next
        if current is cll.head:
            break


    return cll.head


if __name__ == "__main__":

    cll = CSll()
    # cll.add_at_first(12)
    # cll.add_at_first(23)
    # cll.add_at_first(32)
    # cll.add_at_first(40)
    # cll.add_at_first(51)
    cll.add_at_first(1)
    cll.add_at_first(2)
    cll.add_at_first(3)
    cll.add_at_first(4)
    cll.add_at_first(5)
    cll.add_at_first(7)
    cll.add_at_first(8)

    cll.print_cll()
    print("Linked list after even nodes deletion: ")
    delete_even_nodes(cll)
    cll.print_cll()

