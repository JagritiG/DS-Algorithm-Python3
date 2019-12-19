# Find pairs which gives specific sum value
from doublylinkedlist.doubly_linkedlist import Dll


def pairs_with_sum(head, sum_val):

    # Create empty list
    pairs = list()
    p = head
    q = None
    while p:
        q = p.next
        while q:
            if p.data + q.data == sum_val:
                pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
            q = q.next
        p = p.next

    return pairs


if __name__ == "__main__":
    dll = Dll()
    dll.add_at_head(1)
    dll.add_at_head(2)
    dll.add_at_head(3)
    dll.add_at_head(4)
    dll.add_at_head(5)
    print("Elements of linked list: ")
    dll.print_dll()
    print("\n")
    sum_value = 6
    print("The pairs which gives sum value {} are: ".format(sum_value))
    print(pairs_with_sum(dll.head, sum_value))


