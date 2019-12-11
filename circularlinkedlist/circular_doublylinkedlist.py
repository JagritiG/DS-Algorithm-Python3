# Implement circular doubly linked list
class CDllNode:

    def __init__(self, data):           # initialize node's fields
        self.data = data
        self.next = None                # next node reference
        self.prev = None                # previous node reference

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.data)


class CDll:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "Dll object: head=".format(self.head)

    # Check if list is empty
    def is_empty(self):
        """Return True if list is empty."""
        return self.head is None

    # Return size of the list
    def size_cdll(self):
        """Traverses the Linked List and returns the number of nodes
        in the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current:
            current = current.next
            size += 1
            if current is self.head:
                break
        return size

    # Add node at beginning
    def add_at_first(self, new_data):
        """Add node at the beginning of the list."""
        new_node = CDllNode(new_data)

        # If linked list is empty, make new node as head
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node

        # If linked list is not empty
        first_node = self.head
        current = self.head
        while current:
            current = current.next
            if current.next == self.head:
                break
        new_node.next = first_node
        self.head = new_node
        current.next = new_node
        new_node.prev = current

    # Add node at the end
    def add_at_last(self, new_data):
        """Add node at the beginning of the list."""
        new_node = CDllNode(new_data)
        first_node = self.head

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            current = self.head
            while current:
                current = current.next
                if current.next == self.head:
                    break
            current.next = new_node
            new_node.next = self.head
            first_node.prev = new_node

    # Add node at given nth position
    def insert_at_nth_pos(self, data, n):

        # Create a node instance
        new_node = CDllNode(data)

        # When given position is greater than size of list
        if n > self.size_cdll():
            return print("Invalid entry")

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node

        # when add at first position
        elif n == 0:
            self.add_at_first(data)

        # when add at last position
        elif n == self.size_cdll():
            self.add_at_last(data)

        else:
            current = self.head
            previous = None
            current_position = 0
            while current_position < n and current.next:
                previous = current
                current = current.next
                current_position += 1
                if current.next == self.head:
                    break
            previous.next = new_node
            new_node.next = current

        return self.head

    # Delete nth node
    def delete_nth_node(self, n):
        size = self.size_cdll()

        # When given position is greater than size of list
        if n >= size:
            return print("Invalid entry")

        if not self.head:
            return print("List is Empty")

        # Delete first node
        elif n == 0:
            current = self.head
            temp = current.next
            while current:
                current = current.next
                if current.next == self.head:
                    break
            current.next = temp
            temp.prev = current
            self.head = temp

        # Delete last node
        elif n == size - 1:
            current = self.head
            position = 0
            while position < n-1 and current.next:
                current = current.next
                position += 1
            current.next = self.head
            self.head.prev = current

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
            current.next.prev = previous

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
                    if current == self.head:
                        break

        return False

    # Remove given data by value
    def remove(self, data):
        # When linked list is empty
        if not self.head:
            return "Linked list is empty"

        # If first element is the given data
        if self.head.data == data:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            self.head.next.prev = current

        # Other than the first element
        current = self.head
        while current.next is not self.head:
            previous = current
            current = current.next
            if current.data == data:
                previous.next = current.next
                current.next.prev = previous
                current = current.next

    def print_cdll(self):
        current = self.head
        while current:
            print(current.data,)
            current = current.next
            if current == self.head:
                break


if __name__ == "__main__":

    cdll = CDll()
    cdll.add_at_first(1)
    cdll.add_at_first(2)
    cdll.add_at_first(3)
    cdll.add_at_last(4)
    cdll.add_at_last(5)
    cdll.insert_at_nth_pos(6, 3)
    print("Size of the list:")
    print(cdll.size_cdll())
    print("Elements of the list:")
    cdll.print_cdll()
    print("\n")
    cdll.delete_nth_node(3)
    print("Size of the list:")
    print(cdll.size_cdll())
    print("Elements of the list:")
    cdll.print_cdll()
    print("Search 8: " + str(cdll.search(3)))
    print("\n")
    cdll.remove(5)
    print("Size of the list:")
    print(cdll.size_cdll())
    print("Elements of the list:")
    cdll.print_cdll()

