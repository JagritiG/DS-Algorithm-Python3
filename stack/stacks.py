class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item or top item from the list."""

        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """Returns the last or top item in th list."""
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """Returns the length of the list."""
        return len(self.items)

    def is_empty(self):
        """Returns True if list is empty. Else, returns False."""
        return self.items == []

    def pop_all(self):
        """Remove all the elements from a stack recursively."""
        if self.items:
            self.pop()
            return self.pop_all()


if __name__ == "__main__":

    s = Stack()
    print(s.is_empty())
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")
    print(s.is_empty())
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop_all()
    print(s.peek())
    s.push("A")
    print(s.peek())
