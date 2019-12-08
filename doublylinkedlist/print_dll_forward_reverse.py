from doublylinkedlist.doubly_linkedlist import Dll


def print_forward(current):
        """Print all the elements of the linked list using recursion."""
        if current is None:
            return "Exit the linked list."
        print(current.data)
        print_forward(current.next)


def print_reverse(current):
        """Print all the elements of the linked list after reversing using recursion."""
        if current is None:
            return "Exit the linked list."
        print_reverse(current.next)
        print(current.data)


if __name__ == "__main__":
    dll = Dll()
    dll.add_at_head(1)
    dll.add_at_head(3)
    dll.add_at_head(5)
    dll.add_at_head(7)
    print("Elements of linked list:")
    print_forward(dll.head)
    print("Head of linked list:")
    print(dll.head)
    print("Elements of reversed linked list:")
    print_reverse(dll.head)
    print("Head of linked list:")
    print(dll.head)
