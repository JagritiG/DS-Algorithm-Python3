# Remove duplicates from doubly linked list
from doublylinkedlist.doubly_linkedlist import Dll


def remove_duplicates(head):

    current = head
    duplicates = dict()

    while current:
        if current.data in duplicates:
            next_node = current.next
            delete_node(head, current)
            current = next_node
        else:
            duplicates[current.data] = 1
            current = current.next


def delete_node(head, node):

    current = head
    while current:
        if current == node and current == head:
            # case 1: only one node, no next node
            if not current.next:
                current = None
                head = None
                return

            # case 2: if next node is present
            else:
                next_node = current.next
                current.next = None
                next_node.prev = None
                current = None
                head = next_node
                return

        elif current == node:
                # case 3:
                if current.next:
                    next_node = current.next
                    prev_node = current.prev
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    current.next = None
                    current.prev = None
                    current = None
                    return

                # case 4:
                else:
                    prev_node = current.prev
                    prev_node.next = None
                    current.prev = None
                    current = None
                    return
        current = current.next


if __name__ == "__main__":
    dll = Dll()
    dll.add_at_tail(1)
    dll.add_at_tail(2)
    dll.add_at_tail(3)
    dll.add_at_tail(2)
    dll.add_at_tail(1)
    dll.add_at_tail(4)
    dll.add_at_tail(2)
    dll.add_at_tail(1)
    print("List: ")
    dll.print_dll()
    print("\n")
    print("List after removing duplicates: ")
    remove_duplicates(dll.head)
    dll.print_dll()


