def binarySearch(data, val):
    """Search items from an ordered list and returns True if
    item is found. Otherwise returns False.
    """
    first = 0
    last = len(data) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if data[mid] == val:
            found = True
        else:
            if val > data[mid]:
                first = mid + 1
            else:
                last = mid - 1

    return found
