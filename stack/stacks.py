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

    def isEmpty(self):
        """Returns True if list is empty. Else, returns False."""
        return self.items == []
