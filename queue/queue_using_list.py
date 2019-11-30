# Queue implementation using a Python list as underlying storage.
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class PyListQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    Default_capacity = 10               # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * PyListQueue.Default_capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "PyListQueue object: data={}".format(self._data)

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return the element at the front of the queue without removing the element.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2*len(self._data))          # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        """Remove and return the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        first_element = self._data[self._front]
        self._data[self._front] = None              # help garbage collection
        self._size -= 1
        return first_element

    def _resize(self, cap):                         # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                            # keep track of existing list
        self._data = [None] * cap                   # allocate list with new capacity
        walk = self._front
        for k in range(self._size):                 # only consider existing elements
            self._data[k] = old[walk]               # intentionally shift indices
            walk = (1 + walk) % len(old)            # use old size as modulus
        self._front = 0                             # front has been realigned


if __name__ == "__main__":

   q = PyListQueue()
   q.enqueue("Red")
   q.enqueue("Red")
   q.enqueue("Red")
   q.enqueue("Red")
   q.enqueue("Red")
   print(q)
   q.enqueue("Red")
   print(q)


