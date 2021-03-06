# Stack implementation using a Python list
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class PyListStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty Stack."""
        self._data = []                     # non public list instance
        self.temp_list = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if Stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)                    # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                   # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()                 # remove last item from list

    def pop_all(self):
        """Remove all the elements from a stack recursively."""
        if self._data:
            self.pop()
            return self.pop_all()

    # def min_item(self):
    #     """Returns the minimum element of the stack."""
    #     if self._data:
    #         item = self.top()
    #         self.temp_list.append(item)
    #         self.pop()
    #         return self.min_item()
    #
    #     return min(self.temp_list)

