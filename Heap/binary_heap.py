# Binary Heap implementation
class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def __repr__(self):
        """Returns a printable representation of object we call it on."""
        return "{}".format(self.heap_list)

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size = self.current_size + 1
        self.shift_up(self.current_size)

    def shift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.swap(self.heap_list[i], self.heap_list[i // 2])
            i = i // 2

    def shift_down(self, i):
        while i * 2 <= self.current_size:
            min_ch = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_ch]:
                self.swap(self.heap_list[i], self.heap_list[min_ch])
            i = min_ch

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def swap(self, a, b):
        a, b = b, a

    def del_min(self):
        ret_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.shift_down(1)   # ?????
        return ret_value

    def size(self):
        return len(self.heap_list)

    # Building heap with entire list
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.shift_down(i)
            i -= 1


def heap_sort(iterable):
    h = BinHeap()
    array_sorted = []
    for val in iterable:
        h.insert(val)
    while h.size() > 0:
        array_sorted.append(h.del_min())
    return array_sorted


if __name__ == "__main__":

    bin_heap = BinHeap()
    # bin_heap.insert(4)
    # bin_heap.insert(2)
    # bin_heap.insert(5)
    # bin_heap.insert(8)
    # print(bin_heap)
    # bin_heap.build_heap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    # print(bin_heap)
    print(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
