from singlylinkedlist.singly_linkedlist import Sll


def print_forward_list(current):
        """Print all the elements of the linked list using recursion."""
        if current is None:
            return "Exit the linked list."
        print(current.data)
        print_forward_list(current.next)


def print_reverse_list(current):
        """Print all the elements of the linked list after reversing using recursion."""
        if current is None:
            return "Exit the linked list."
        print_reverse_list(current.next)
        print(current.data)


if __name__ == "__main__":
    sll = Sll()
    sll.add_at_head(1)
    sll.add_at_head(3)
    sll.add_at_head(5)
    sll.add_at_head(7)
    print("Elements of linked list:")
    print(sll.head)
    print("Head of linked list:")
    print_forward_list(sll.head)
    print("Elements of reversed linked list:")
    print_reverse_list(sll.head)


