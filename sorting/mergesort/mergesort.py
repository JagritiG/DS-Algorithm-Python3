def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_list = data[:mid]
        right_list = data[mid:]

        # Recursively breakdown the list
        mergeSort(left_list)
        mergeSort(right_list)

        # Perform the merging
        i = 0 # index into the left_list
        j = 0 # index into the right_list
        k = 0 # index into the merge list

        # While both lists have content
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                data[k] = left_list[i]
                i += 1
            else:
                data[k] = right_list[j]
                j += 1
            k += 1

        # If the left_list still has values, add them
        while i < len(left_list):
            data[k] = left_list[i]
            i += 1
            k += 1

        # If the right_list still has values, add them
        while j < len(right_list):
            data[k] = right_list[j]
            j += 1
            k += 1

    return data
