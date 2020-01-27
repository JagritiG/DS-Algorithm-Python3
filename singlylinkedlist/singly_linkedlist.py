class SllNode:

        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return "{}".format(self.data)

        def get_data(self):
            return self.data

        def set_data(self, new_data):
            self.data = new_data

        def get_next(self):
            return self.next

        def set_next(self, new_next):
            self.next = new_next


class Sll:

    def __init__(self):
        self.head = None

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.head)

    def is_empty(self):
        return self.head is None

    def add_at_head(self, new_data):
        new_node = SllNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_nth_pos(self, data, n):

        # Create a node instance
        new_node = SllNode(data)

        # When given position is greater than size of list
        if n > self.list_size():
            return print("Invalid entry")

        # If list is empty
        if not self.head:
            self.head = new_node

        # when add at first position
        elif n == 0:
            self.add_at_head(data)

        # when add at last position
        elif n == self.list_size():
            self.add_at_tail(data)

        else:
            previous = None
            current_position = 0
            current = self.head
            while current_position < n and current.next:
                previous = current
                current = current.next
                current_position += 1
            previous.next = new_node
            new_node.next = current

        return self.head

    def add_at_tail(self, new_data):
        new_node = SllNode(new_data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_nth_node(self, n):
        size = self.list_size()

        # When given position is greater than size of list
        if n >= size:
            return print("Invalid entry")

        if not self.head:
            return print("List is Empty")

        # Delete first node
        elif n == 0:
            current = self.head
            temp = current.next
            self.head = temp

        # Delete last node
        elif n == size - 1:
            current = self.head
            position = 0
            while position < n-1 and current.next:
                current = current.next
                position += 1
            current.next = None

        # Delete nth node
        else:
            previous = None
            current = self.head
            position = 0
            while position < n and current.next:
                previous = current
                current = current.next
                position += 1
            previous.next = current.next

    # Search given data
    def search(self, data):
        if not self.head:
            return "Linked list is empty"

        current = self.head
        while current:
                if current.data == data:
                    return True
                else:
                    current = current.next

        return False

    # Remove given data by value
    def remove(self, data):
        # When linked list is empty
        if not self.head:
            return "Linked list is empty"
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current.data == data:
                    found = True
                else:

                    if not current.next:
                        return "A Node with given data is not present."
                    else:
                        previous = current
                        current = current.next

            if previous is None:
                self.head = current.next

            else:
                previous.next = current.next

        return self.head

    # Size of linked list
    def list_size(self):

        size = 0
        if not self.head:
            return 0
        else:
            current = self.head
            while current is not None:
                current = current.get_next()
                size += 1
        return size

    def print_list(self):
        current = self.head
        while current:
            print(current.data,)
            current = current.next

    def reverse_iter(self):
        """Reversing a singly linked list using iterative method."""
        if not self.head:
            return print("Linked list is empty")

        else:
            current = self.head
            prev_node = None
            while current:
                next_node = current.next
                current.next = prev_node
                prev_node = current
                current = next_node
            self.head = prev_node

        return self.head


if __name__ == "__main__":
        # node1 = SllNode(2)
        # print(node1.get_data())
        # node1.set_data(6)
        # print(node1.get_data())
        # node2 = SllNode(10)
        # print(node2.get_data())
        # print(node1.get_next())
        # node1.set_next(node2)
        # print(node1.get_next())

        s = Sll()
        s.add_at_head(11)
        s.add_at_head(12)
        s.add_at_head(8)
        s.add_at_head(9)
        s.insert_at_nth_pos(3, 4)
        # print(s.head)
        # print('Created linked list is:')
        # s.print_list()
        # s.add_at_tail(7)
        # s.add_at_tail(1)
        # print(s.head5
        # print('Created linked list is:')
        # s.print_list()
        # print("Delete nth node:")
        # s.delete_nth_node(4)
        # s.remove(8)
        print('Created linked list is:')
        s.print_list()
        # print(s.search(11))
        print("Head of the Linked List:")
        print(s.head)
        s.reverse_iter()
        print('Reversed linked list is:')
        s.print_list()
        print("Head of the Linked List:")
        print(s.head)

