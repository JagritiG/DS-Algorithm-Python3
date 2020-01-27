# Implementing heapsort using MinHeap
import heapq


class MinHeap:

    # Create a heap
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.heap)

    # Inserting into heap
    def insert(self, val):
        heapq.heappush(self.heap, val)

    # Size of heap
    def size(self):
        return len(self.heap)

    # Removing element from min heap
    def remove(self):
        return heapq.heappop(self.heap)


def heap_sort(iterable):
    h = MinHeap()
    array_sorted = []
    for val in iterable:
        h.insert(val)
    while h.size() > 0:
        array_sorted.append(h.remove())
    return array_sorted


if __name__ == "__main__":

    min_heap = MinHeap()
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

