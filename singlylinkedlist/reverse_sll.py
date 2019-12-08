from singlylinkedlist.singly_linkedlist import Sll


def reverse_linked_list(current):
        """Reverse a linked list using recursion."""
        if current.next is None:
            sll.head = current
            return sll.head
        reverse_linked_list(current.next)
        temp = current.next
        temp.next = current
        current.next = None


if __name__ == "__main__":
    sll = Sll()
    sll.add_at_head(1)
    sll.add_at_head(3)
    sll.add_at_head(5)
    sll.add_at_head(7)
    print("Elements of linked list:")
    sll.print_list()
    print("Head:")
    print(sll.head)
    print("Elements of reversed linked list:")
    reverse_linked_list(sll.head)
    sll.print_list()
    print("Head after reversing:")
    print(sll.head)
