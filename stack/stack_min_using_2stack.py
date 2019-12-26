# Design a stack that has O(1) push, pop and min functions
from stack.stacks import Stack

# Method-1: using two stacks, one to store actual stack elements
# and an auxiliary stack to store minimum values.
# This approach uses O(1) time and O(n) extra space.


class SpecialStack:

    def __init__(self):
        self.stack = Stack()
        self.aux_stack = Stack()

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.
        """
        if self.stack.is_empty():
            self.stack.push(item)
            self.aux_stack.push(item)

        else:
            self.stack.push(item)
            top = self.aux_stack.pop()
            self.aux_stack.push(top)
            if item < top:
                self.aux_stack.push(item)
            else:
                self.aux_stack.push(top)

    def pop(self):
        """Removes and returns the last item or top item from the list."""

        top_item = self.stack.pop()
        self.aux_stack.pop()
        return top_item

    def peek(self):
        """Returns the last or top item in th list."""
        return self.stack.peek()

    def get_min(self):
        """Returns the top item from the list."""
        top_aux_stack = self.aux_stack.pop()
        self.aux_stack.push(top_aux_stack)
        return top_aux_stack


if __name__ == "__main__":

    s = SpecialStack()
    s.push(8)
    # print(s.get_min())
    # print(s.peek())
    s.push(10)
    # print(s.get_min())
    # print(s.peek())
    s.push(12)
    # print(s.get_min())
    # print(s.peek())
    s.pop()
    print(s.get_min())
    print(s.peek())



# Method-2: This approach uses O(1) time and O(1) extra space.


