# Implementing Queue using deque
from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Push an item in the end of the queue.
        Returns nothing.
        """
        self.items.append(item)

    def dequeue(self):
        """Pops an item off the front of the queue."""
        if self.items:
            return self.items.popleft()

        return None

    def size(self):
        """Returns the length of the list."""
        return len(self.items)

    def isEmpty(self):
        """Returns True if list is empty. Else, returns False."""
        return self.items == deque()
