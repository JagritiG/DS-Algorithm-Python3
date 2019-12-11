# Convert single linked list into circular linked list
class Node:

    def __init__(self, data):
            self.data = data
            self.next = None

    def __repr__(self):
            return "{}".format(self.data)


class Sll:

    def __init__(self):
        self.head = None

    def add_node(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data,)
            current = current.next


def circular(head):
    current = head

    while current.next is not None:
        current = current.next

    current.next = head
    return head


def display_list(head):
        current = head
        while current.next is not head:
            print(current.data,)
            current = current.next
        print(current.data)


if __name__ == "__main__":

        lst = Sll()
        lst.add_node(1)
        lst.add_node(2)
        lst.add_node(3)
        lst.add_node(4)
        print("Singled linked list: ")
        lst.print_list()
        print("\n")
        print("Circular single linked list: ")
        circular(lst.head)          # call circular() function
        display_list(lst.head)
