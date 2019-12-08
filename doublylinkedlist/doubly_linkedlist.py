# Implement doubly linked list
class DllNode:

    def __init__(self, data):           # initialize node's fields
        self.data = data
        self.next = None                # next node reference
        self.prev = None                # previous node reference

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

    def get_previous(self):
        """Return the self.prev attribute."""
        return self.prev

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute
        with the new_previous parameter.
        """
        self.prev = new_previous


class Dll:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "Dll object: head=".format(self.head)

    def is_empty(self):
        """Return True if list is empty."""
        return self.head is None

    def size_dll(self):
        """Traverses the Linked List and returns the number of nodes
        in the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        current.prev = None
        while current is not None:
            current = current.next
            size += 1
        return size

    def add_at_head(self, new_data):

        new_node = DllNode(new_data)
        current = self.head
        new_node.next = None

        # If linked list is empty, make new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # If linked list is not empty
        new_node.prev = None
        new_node.next = current
        current.prev = new_node
        self.head = new_node

    def add_at_tail(self, new_data):

        new_node = DllNode(new_data)
        current = self.head
        new_node.next = None

        # If linked list is empty, make new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # If linked list is not empty, traverse till the end
        while current.next is not None:
                current = current.next

        current.next = new_node
        new_node.prev = current

    def add_at_nth_position(self, new_data, n):

        # Create a node instance
        new_node = DllNode(new_data)

        # When given position is greater than size of list
        if n >= self.size_dll():
            return print("Invalid entry")

        # If list is empty
        if not self.head:
            new_node.prev = None
            self.head = new_node
            return

        elif n == 0:                    # when add at first position
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
            new_node.prev = None

        else:
            previous = 0
            current_position = 0
            current = self.head
            while current_position <= n and current.next:
                previous = current
                current = current.next
                current_position += 1
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node

        return self.head

    def delete_nth_node(self, n):
        size = self.size_dll()

        # When given position is greater than size of list
        if n >= size:
            return print("Invalid entry")

        if not self.head:
            return print("List is Empty")

        # Delete first node
        elif n == 0:
            current = self.head
            self.head = current.next
            current.next.prev = None

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
            current.prev = previous.prev

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

    def remove(self, data):
        """Delete node by value."""
        # When linked list is empty
        if not self.head:
            return "Linked list is empty"
        else:
            current = self.head
            found = False
            while not found:
                if current.data == data:
                    found = True
                else:

                    if not current.next:
                        return "A Node with given data is not present."
                    else:
                        current = current.next

            if current.prev is None:
                self.head = current.next
                current.next.prev = None

            else:
                current.prev.next = current.next
                current.next.prev = current.prev

        return self.head

    def print_dll(self):
        current = self.head
        while current:
            print(current.data,)
            current = current.next


if __name__ == "__main__":

    d = Dll()
    d.add_at_head(1)
    d.add_at_head(2)
    d.add_at_head(3)
    d.add_at_tail(4)
    d.add_at_tail(5)
    d.add_at_nth_position(6, 2)
    print("Size of list:")
    print(d.size_dll())
    print("Elements of the list:")
    d.print_dll()
    d.delete_nth_node(2)
    print("Elements of the list:")
    d.print_dll()
    print("Head of the list:")
    print(d.head)
    print(d.search(4))
    d.remove(3)
    print("Elements of the list:")
    d.print_dll()
