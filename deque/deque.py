# Deque implementation using list
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


if __name__ == "__main__":

    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_front(3)
    deque.add_rear(2)
    deque.add_rear(3)
    print("Size: " + str(deque.size()))
    print(deque)
    deque.remove_front()
    deque.remove_rear()
    print("Size: " + str(deque.size()))
    print(deque)


