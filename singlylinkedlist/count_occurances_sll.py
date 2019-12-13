# Count occurrences in singly linked list
from singlylinkedlist.singly_linkedlist import Sll


def count_occurrences_iter(sll, data):

    current = sll.head
    count = 0
    while current:
        if current.data == data:
            count += 1
        current = current.next

    return count


def count_occurrences_recur(current, data):

    if not current:
        return 0

    if current.data == data:
        return 1 + count_occurrences_recur(current.next, data)

    else:
        return count_occurrences_recur(current.next, data)


if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(3)
    sll.add_at_tail(2)
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(1)
    sll.add_at_tail(4)
    print("List: ")
    sll.print_list()
    print("\n")
    data = 2
    print("Number of {}: ".format(data) + str(count_occurrences_iter(sll, data)))
    print("Number of {}: ".format(data) + str(count_occurrences_recur(sll.head, data)))
