# Convert an array into circular doubly linked list
import numpy as np
from circularlinkedlist.circular_doublylinkedlist import CDll


def convert_array_into_cdll(arr, list):

    i = 0
    n = arr.size
    print(n)
    while i < n:
        new_data = arr[i]
        list.add_at_first(new_data)
        i += 1

    return list.head


if __name__ == "__main__":

    cdll = CDll()
    x = np.array([1, 2, 3, 4])
    # n = x.size
    convert_array_into_cdll(x, cdll)
    cdll.print_cdll()

