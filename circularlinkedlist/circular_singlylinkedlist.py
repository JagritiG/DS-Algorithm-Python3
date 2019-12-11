# Implementing circular linked list
class CSllNode:

    def __init__(self, data):
        """Construct node for circular linked list."""
        self.data = data
        self.next = None

    def __repr__(self):
            return "{}".format(self.data)


class CSll:

    def __init__(self):
        self.head = None

    def __repr__(self):
                """Returns a printable representation of object we call it on."""
                return "{}".format(self.head)

    def list_size(self):

        size = 0
        if not self.head:
            return 0
        else:
            current = self.head
            while current:
                current = current.next
                size += 1
                if current == self.head:
                    break

        return size

    def add_at_first(self, new_data):
        """Add node at the beginning of the list."""
        new_node = CSllNode(new_data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node

        first_node = self.head
        current = self.head
        while current:
            current = current.next
            if current.next == self.head:
                break
        new_node.next = first_node
        self.head = new_node
        current.next = new_node

    def add_at_last(self, new_data):
        """Add node at the beginning of the list."""
        new_node = CSllNode(new_data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current:
                current = current.next
                if current.next == self.head:
                    break
            current.next = new_node
            new_node.next = self.head

    def insert_at_nth_pos(self, data, n):

        # Create a node instance
        new_node = CSllNode(data)

        # When given position is greater than size of list
        if n > self.list_size():
            return print("Invalid entry")

        # If list is empty
        if self.head is None:
            self.head = new_node
            new_node.next = new_node

        # when add at first position
        elif n == 0:
            self.add_at_first(data)

        # when add at last position
        elif n == self.list_size():
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
            while current:
                current = current.next
                if current.next == self.head:
                    break
            current.next = temp
            self.head = temp

        # Delete last node
        elif n == size - 1:
            current = self.head
            position = 0
            while position < n-1 and current.next:
                current = current.next
                position += 1
            current.next = self.head

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

        # Other than the first element
        else:
            current = self.head
            previous = None
            while current.next is not self.head:
                previous = current
                current = current.next
                if current.data == data:
                    previous.next = current.next
                    current = current.next

    def print_cll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def split_list(self):

        if self.list_size() == 0:
            return None
        if self.list_size() == 1:
            return self.head

        mid = self.list_size()//2
        count = 0

        previous = None
        current = self.head

        while current and count < mid:
            count += 1
            previous = current
            current = current.next
        previous.next = self.head

        split_clist = CSll()
        while current.next is not self.head:
            split_clist.add_at_first(current.data)
            current = current.next
        split_clist.add_at_first(current.data)

        self.print_cll()
        print("\n")
        split_clist.print_cll()

    # Remove given node
    def remove_node(self, node):

        # If first node is the given node to be deleted
        if self.head == node:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

        # Other than the first element
        else:
            current = self.head
            previous = None
            while current.next is not self.head:
                previous = current
                current = current.next
                if current == node:
                    previous.next = current.next
                    current = current.next

    # Josephus circle
    def josephus_circle(self, step):
        current = self.head

        while self.list_size() > 1:
            count = 1
            while count is not step:
                current = current.next
                count += 1
            print("Removed: " + str(current.data))
            self.remove_node(current)
            current = current.next




if __name__ == "__main__":

    cll = CSll()
    cll.add_at_first(1)
    cll.add_at_first(2)
    cll.add_at_first(3)
    cll.add_at_last(4)
    # cll.insert_at_nth_pos(5, 4)
    # print("Size:")
    # print(cll.list_size())
    # print("Head:")
    # print(cll.head)
    # print("Elements of the list:")
    # cll.print_cll()
    # cll.delete_nth_node(4)
    print("Elements of the list:")
    cll.print_cll()
    # print(cll.search(2))
    # # cll.remove(2)
    # cll.remove_node(cll.head)
    cll.josephus_circle(3)
    print("Elements of the list:")
    cll.print_cll()
    # print("Split lists' elements:")
    # cll.split_list()




