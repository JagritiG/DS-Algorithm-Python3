# Palindrome check using deque
class Deque:

    def __init__(self):
        self.items = []

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.items)

    def is_empty(self):
        return self.items == []

    def add_front(self, data):
        self.items.append(data)

    def add_rear(self, data):
        self.items.insert(0, data)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palindrome_check(input_string):

    deque = Deque()

    for ch in input_string:
        deque.add_rear(ch)

    equal = True
    while deque.size() > 1 and equal:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first is not last:
            equal = False

    return equal


if __name__ == "__main__":

    print(palindrome_check("RADAR"))


