# Detect loop in singly linked list
from singlylinkedlist.singly_linkedlist import Sll


def detect_loop_llist(head):

    s = set()
    current = head
    while current:

        if current in s:
            return True

        # If first occurrence, store data in hash
        s.add(current)
        current = current.next

    return False


if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(3)
    sll.add_at_tail(4)

    # Create a loop for testing
    temp1 = sll.head.next
    temp2 = temp1.next.next
    temp2.next = temp1

    # If loop found print True, else print False
    print(detect_loop_llist(sll.head))


