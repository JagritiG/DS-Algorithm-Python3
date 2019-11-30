# Implementing Queue using deque
from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.items)

    def enqueue(self, item):
        """Add an item in the end of the queue.
        Returns nothing.
        """
        self.items.append(item)

    def dequeue(self):
        """Remove and return an item off the front of the queue."""
        if self.items:
            return self.items.popleft()

        return None

    def size(self):
        """Returns the length of the list."""
        return len(self.items)

    def isEmpty(self):
        """Returns True if list is empty. Else, returns False."""
        return self.items == deque()


if __name__ == "__main__":
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(q)
    q.dequeue()
    print(q)
    print(q.size())
    print(q.isEmpty())
