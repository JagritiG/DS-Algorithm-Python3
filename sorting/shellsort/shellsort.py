def shellSort(data):
    sublist_count = len(data) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gapInsertionSort(data, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return data


def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):
        current_value = data[i]
        position = i

        while position >= gap and data[position-gap] > current_value:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = current_value
