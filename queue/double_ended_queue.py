# Double ended queue
from collections import deque


class DoubleEndedQueue:

    def __init__(self):
        self.items = deque()

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.items)

    def add_first(self, item):
        """Add an item in the beginning of the queue.
        Returns nothing.
        """
        self.items.appendleft(item)

    def add_last(self, item):
        """Add an item in the end of the queue.
        Returns nothing.
        """
        self.items.append(item)

    def delete_first(self):
        """Remove and return an item in the beginning of the queue."""
        if self.items:
            return self.items.popleft()

        return None

    def delete_last(self):
        """Remove and return an item in the end of the queue."""
        if self.items:
            return self.items.pop()

        return None

    def first(self):
        """Return an item from the beginning of the queue without removing."""
        if self.items:
            return self.items[0]

        return None

    def last(self):
        """Return an item from the end of the queue without removing."""
        if self.items:
            return self.items[-1]

        return None

    def access_item(self, idx):
        """Return an arbitrary entry by index without removing."""
        if self.items:
            return self.items[idx]

        return None

    def modify_item(self, idx, val):
        """Modify arbitrary entry by index."""
        if self.items:
            self.items[idx] = val

        return None

    def remove_item(self, e):
        """Remove first match."""
        if self.items:
            self.items.remove(e)

        return None

    def rotate_queue(self, k_steps):
        """Circularly shift rightward k steps."""
        if self.items:
            self.items.rotate(k_steps)

        return None

    def count_item(self, e):
        """Count number of matches for e."""
        if self.items:
            return self.items.count(e)

        return None

    def clear_queue(self):
        """Clear all contents."""
        if self.items:
            self.items.clear()

        return None

    def size(self):
        """Returns the length of the list."""
        return len(self.items)

    def isEmpty(self):
        """Returns True if list is empty. Else, returns False."""
        return self.items == deque()


if __name__ == "__main__":
    q = DoubleEndedQueue()
    q.add_last("A")
    q.add_last("B")
    q.add_last("C")
    q.add_first("A")
    print(q)
    q.delete_last()
    print(q.modify_item(1, "B"))
    print(q.modify_item(2, "C"))
    print(q.last())
    q.remove_item("B")
    q.add_first("A")
    q.rotate_queue(1)
    print(q.count_item("A"))
    print(q)
    q.clear_queue()
    print(q)

