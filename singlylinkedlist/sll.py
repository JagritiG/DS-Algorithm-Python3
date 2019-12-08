# Implement singly linked list
class SLLNode:

        def __init__(self, data):
                self.data = data
                self.next = None

        def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "{}".format(self.data)

        def get_data(self):
                """Return the self.data attribute."""
                return self.data

        def set_data(self, new_data):
                """Replace the existing value of the self.data attribute
                with the new_data parameter.
                """
                self.data = new_data

        def get_next(self):
                """Return the self.next attribute."""
                return self.next

        def set_next(self, new_next):
                """Replace the existing value of the self.next attribute
                with the new_next parameter.
                """
                self.next = new_next


class SLL:

        def __init__(self):
                self.head = None

        def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "{}".format(self.head)

        def is_empty(self):
                return self.head is None                    # self.head == None

        def add_node_at_head(self, new_data):
                """Add a Node to the front/head of the Linked List."""
                new_node = SLLNode(new_data)                # create new node instance storing reference to new data
                new_node.set_next(self.head)                # set new node's next to reference the old head node
                self.head = new_node                        # set variable head to reference the new node

        def add_node_at_tail(self, new_data):
                """Add a Node to the end/tail of the Linked List."""
                new_node = SLLNode(new_data)
                if self.head is None:
                        self.head = new_node
                else:
                        current = self.head
                        while current.get_next() is not None:
                                current = current.get_next()
                        current.set_next(new_node)

                return self.head

        def add_node_at_nth_pos(self, data, position):
                """Add a Node to the nth position of the Linked List."""
                node = SLLNode(data)
                if position >= self.size():
                        return print("Insert position is incorrect.")

                if not self.head:
                        self.head = node
                elif position == 0:
                        node.next = self.head
                        self.head = node
                else:
                        previous = None
                        current = self.head
                        current_position = 0
                        while current_position < position and current.next:
                                previous = current
                                current = current.next
                                current_position += 1
                        previous.next = node
                        node.next = current
                return self.head

        def size(self):
                """Traverses the Linked List and returns the number of nodes
                in the Linked List.
                """
                size = 0
                if self.head is None:
                        return 0

                current = self.head
                while current is not None:    # While there are still nodes left to count
                        size += 1
                        current = current.get_next()

                return size

        def search(self, data):
                """Traverses the Linked List and returns True if the the data searched
                for is present in one of the Nodes. Otherwise, it returns False."""
                if self.head is None:
                        return "Linked List is empty."

                current = self.head
                while current is not None:
                        if current.get_data() == data:
                                return True
                        else:
                                current = current.get_next()

                return False

        def remove(self, data):
                """Removes the first occurance of a Node that contains the data argument
                as its self.data variable. Returns nothing.
                """
                if self.head is None:
                        return "Linked List is empty. No Nodes to remove."
                current = self.head
                previous = None
                found = False
                while not found:
                        if current.get_data() == data:
                                found = True
                        else:
                                if current.get_next() is None:
                                        return "A Node with given data is not present."

                                else:
                                        previous = current
                                        current = current.get_next()
                if previous is None:
                        self.head = current.get_next()
                else:
                        previous.set_next(current.get_next())

        # Utility function to print the linked list
        def print_list(self):
                """Print all the elements of the Linked List."""
                temp = self.head
                while temp:
                        print(temp.data,)
                        temp = temp.next


if __name__ == "__main__":
        node1 = SLLNode(2)
        print(node1.get_data())
        node1.set_data(6)
        print(node1.get_data())
        node2 = SLLNode(10)
        print(node2.get_data())
        print(node1.get_next())
        node1.set_next(node2)
        print(node1.get_next())

        sll = SLL()
        sll.add_node_at_head(2)
        sll.add_node_at_head(3)
        sll.add_node_at_head(4)
        print(sll.head)
        print(sll.size())
        sll.add_node_at_nth_pos(5, 2)
        sll.remove(5)
        print('Created linked list is:')
        sll.print_list()



