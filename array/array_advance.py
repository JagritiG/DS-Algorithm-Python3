# The below function checks if it is possible to advance from the start of the array to the end of the array


def array_advance(arr):
    farthest_reached = 0
    last_idx = len(arr) - 1
    i = 0
    while i <= farthest_reached < last_idx:
        farthest_reached = max(farthest_reached, arr[i]+i)
        i += 1

    return farthest_reached >= last_idx


if __name__ == "__main__":

    arr1 = [3, 3, 1, 0, 2, 0, 1]
    print(array_advance(arr1))
    arr2 = [3, 2, 0, 0, 2, 0, 1]
    print(array_advance(arr2))

