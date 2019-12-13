# Find nth node from last in a singly linked list
from singlylinkedlist.singly_linkedlist import Sll


# Method-1: using size of list
# def nth_node_from_last(head, n):
#
#     size = sll.list_size()
#
#     current = head
#     while current:
#         if size == n:
#             print(current.data)
#             return current
#         size -= 1
#         current = current.next
#     if current is None:
#         return


# Method-2: using two pointers
def nth_node_from_last(head, n):

    p = head
    q = head

    count = 0
    while q and count < n:
        q = q.next
        count += 1

    if not q:
        print(str(n) + " is greater than the number of nodes in the list.")

    while p and q:
        p = p.next
        q = q.next
    return p.data


if __name__ == "__main__":

    sll = Sll()
    sll.add_at_tail(1)
    sll.add_at_tail(2)
    sll.add_at_tail(3)
    sll.add_at_tail(4)
    print("List: ")
    sll.print_list()
    print("\n")
    n = 5
    print("{}th node from last: ".format(n))
    print(nth_node_from_last(sll.head, n))

