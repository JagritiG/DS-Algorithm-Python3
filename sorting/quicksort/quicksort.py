def quickSort(data, first, last):
    if first < last:
        # Calculate the split point
        pivot_index = partition(data, first, last)

        # Sort the two partitions
        quickSort(data, first, pivot_index-1)
        quickSort(data, pivot_index+1, last)

    return data


def partition(datavalues, first, last):
    # Choose the upper and lower indexes
    pivot_value = datavalues[first]
    # Set the upper and lower indexes
    lower_index = first + 1
    upper_index = last

    # Start searching for the crossing point
    found = False
    while not found:
        # Advance the lower_index
        while lower_index <= upper_index and datavalues[lower_index] <= pivot_value:
            lower_index += 1
        # Advance the upper_index
        while datavalues[upper_index] >= pivot_value and upper_index >= lower_index:
            upper_index -= 1

        # If the two indexes cross, we have found the split point
        if upper_index < lower_index:
            found = True
        else:
            temp = datavalues[lower_index]
            datavalues[lower_index] = datavalues[upper_index]
            datavalues[upper_index] = temp

    # When the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper_index]
    datavalues[upper_index] = temp

    # Return the split point index
    return upper_index


