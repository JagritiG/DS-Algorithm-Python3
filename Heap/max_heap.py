# MaxHeap implementing
# heappush – This function adds an element to the heap without altering the current heap.
# heappop - This function returns the smallest data element from the heap.
# heapreplace – This function replaces the smallest data element with a new value supplied in the function.

import heapq


class MaxHeap:
    def __init__(self, iterable=None):
        self.heap = []

        if iterable is not None:
            for i in iterable:
                self.insert(i)

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.heap)

    def insert(self, val):
        self.heap.append(val)
        _move_up(self.heap, self.size() - 1)

    def remove(self):
        _swap(self.heap, self.size() - 1, 0)
        val = self.heap.pop()
        _move_down(self.heap, 0)
        return val

    # Get the maximum element from the heap without popping it
    def get_max(self):
        return self.heap[0]

    def size(self):
        return len(self.heap)

    # Replacing an element
    def replace_val(self, val):
        heapq.heapreplace(self.heap, val)


# Helper functions
def _swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def _move_up(heap, idx):
    parent = (idx - 1) // 2
    # If we've hit the root node, there's nothing left to do
    if parent < 0:
        return

    # If the current node is larger than the parent node, swap them
    if heap[idx] > heap[parent]:
        _swap(heap, idx, parent)
        _move_up(heap, parent)


def _move_down(heap, idx):
    child = 2 * idx + 1
    # case 1: If end of the heap encountered, return
    if child >= len(heap):
        return

    # case 2: If the node has both children, swap with the larger one
    if child + 1 < len(heap) and heap[child] < heap[child + 1]:
        child += 1

    # case 3: If the child node is smaller than the current node, swap them
    if heap[child] > heap[idx]:
        _swap(heap, child, idx)
        _move_down(heap, child)


# Get n largest values from given iterables
def get_nlargest(n, iterable):
    return heapq.nlargest(n, iterable)


# Get n smallest values from given iterables
def get_nsmallest(n, iterable):
    return heapq.nsmallest(n, iterable)


def heap_sort(iterable):
    h = MaxHeap()
    array_sorted = []
    for val in iterable:
        h.insert(val)
    while h.size() > 0:
        array_sorted.append(h.remove())
    return array_sorted


if __name__ == "__main__":

    max_heap = MaxHeap()
    print(max_heap)
    max_heap.insert(21)
    max_heap.insert(1)
    max_heap.insert(45)
    max_heap.insert(78)
    max_heap.insert(3)
    max_heap.insert(5)
    print(max_heap)
    max_heap.remove()
    print(max_heap)
    print("Max: " + str(max_heap.get_max()))
    max_heap.replace_val(22)
    print(max_heap)
    print(max_heap.size())
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print("3 largest: " + str(get_nlargest(3, [1, 3, 5, 7, 9, 2, 4, 6, 8, 0])))
    print("3 smallest" + str(get_nsmallest(3, [1, 3, 5, 7, 9, 2, 4, 6, 8, 0])))
