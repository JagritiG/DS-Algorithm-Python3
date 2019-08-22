def insertionSort(data):
    for i in range(1,len(data)):
        current_value = data[i]
        position = i

        while position > 0 and data[position-1] > current_value:
            data[position] = data[position-1]
            position = position-1

        data[position] = current_value

    return data
