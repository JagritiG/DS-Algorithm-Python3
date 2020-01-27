# heapify - This function converts a regular list to a heap.
#           In the resulting heap the smallest element gets pushed to the index position 0.
#           But rest of the data elements are not necessarily sorted.
# heappush – This function adds an element to the heap without altering the current heap.
# heappop - This function returns the smallest data element from the heap.
# heapreplace – This function replaces the smallest data element with a new value supplied in the function.

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

    # Replacing an element
    def replace_val(self, val):
        heapq.heapreplace(self.heap, val)

    # Get the minimum element from the heap without popping it
    def get_min(self):
        return self.heap[0]


# Get n largest values from given iterables
def get_nlargest(n, iterable):
    return heapq.nlargest(n, iterable)


# Get n smallest values from given iterables
def get_nsmallest(n, iterable):
    return heapq.nsmallest(n, iterable)


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
    print(min_heap)
    min_heap.insert(21)
    min_heap.insert(1)
    min_heap.insert(45)
    min_heap.insert(78)
    min_heap.insert(3)
    min_heap.insert(5)
    print(min_heap)
    min_heap.remove()
    print(min_heap)
    print(min_heap.get_min())
    min_heap.replace_val(6)
    print(min_heap)
    print(min_heap.size())
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print("3 largest: " + str(get_nlargest(3, [1, 3, 5, 7, 9, 2, 4, 6, 8, 0])))
    print("3 smallest" + str(get_nsmallest(3, [1, 3, 5, 7, 9, 2, 4, 6, 8, 0])))


