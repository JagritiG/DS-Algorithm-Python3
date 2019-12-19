# Reverse doubly linked list
from doublylinkedlist.doubly_linkedlist import Dll


def reverse_dll(current):
        """Reverse a linked list using recursion."""
        if current.next is None:
            dll.head = current
            return dll.head
        reverse_dll(current.next)
        temp = current.next
        temp.next = current
        current.next = None


if __name__ == "__main__":
    dll = Dll()
    dll.add_at_head(1)
    dll.add_at_head(3)
    dll.add_at_head(5)
    dll.add_at_head(7)
    print("Elements of linked list:")
    dll.print_dll()
    print("Head:")
    print(dll.head)
    print("Elements of reversed linked list:")
    reverse_dll(dll.head)
    dll.print_dll()
    print("Head after reversing:")
    print(dll.head)
