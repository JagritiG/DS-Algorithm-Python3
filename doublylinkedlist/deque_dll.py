# Implementing Deque using a doubly linked list for storage.
from doublylinkedlist.doubly_linkedlist import Dll


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedDeque(Dll):
    """Double-ended queue implementation based on a doubly linked list."""

    def first_element(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.head

    def last_element(self):
        """Return (but do not remove) the element at the end of the queue."""
        if self.is_empty():
            raise Empty("Deque is empty")

        current = self.head
        while current.next:
            current = current.next

        return current

    def add_first(self, data):
        """Add an element to the front of the queue."""
        self.add_at_head(data)

    def add_last(self, data):
        """Add an element to the end of the queue."""
        self.add_at_tail(data)

    def delete_first(self):
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Deque is empty")
        n = 0
        self.delete_nth_node(n)

    def delete_last(self):
        """Remove and return the element at the end of the queue."""
        if self.is_empty():
            raise Empty("Deque is empty")
        n = self.size_dll() - 1
        self.delete_nth_node(n)


if __name__ == "__main__":

    pass
    ld = LinkedDeque()
    ld.add_first(5)
    ld.add_first(2)
    ld.add_first(3)
    ld.add_last(4)
    ld.add_last(7)
    ld.delete_first()
    ld.delete_last()
    print(ld.first_element())
    print(ld.last_element())

