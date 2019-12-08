from doublylinkedlist.doubly_linkedlist import Dll


def printForward(current):
    """Print all the elements of the list."""
    if current is None:
        return

    while current:
        print(current.data)
        current = current.next


def printReverse(current):
    """Print all the elements of the list in reverse."""
    temp = current
    if current is None:
        return

    # Traverse to the end
    while current.next:
        current = current.next

    # Traverse backward
    while current:
        print(current.data)
        current = current.prev


if __name__ == "__main__":
    dll = Dll()
    dll.add_at_head(1)
    dll.add_at_head(3)
    dll.add_at_tail(5)
    dll.add_at_tail(7)
    print("Head of linked list:")
    print(dll.head)
    print("Forward:")
    printForward(dll.head)
    print("Reverse:")
    printReverse(dll.head)
