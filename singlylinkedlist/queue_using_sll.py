# Implementing Queue using a singly linked list for storage.
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedQueue:
    """FIFO implementation using a singly linked list for storage."""

    # ---------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'           # streamline memory usage

        def __init__(self, element, next):        # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

    # ---------------- queue methods ----------------------------------

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0

    def first(self):
        """Return the element at the front of the queue without removing it.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element              # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                    # special case as queue is empty
            self._tail = None                  # removed head had been the tail
        return result

    def enqueue(self, e):
        """Add an element to the back of queue."""
        new = self._Node(e, None)              # node will be new tail node
        if self.is_empty():
            self._head = new                   # special case: previously empty
        else:
            self._tail._next = new
        self._tail = new                       # update reference to tail node
        self._size += 1


if __name__ == "__main__":
    que = LinkedQueue()
    print(que.is_empty())
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)
    print(que.dequeue())
    print(que.dequeue())
    print(que.first())

