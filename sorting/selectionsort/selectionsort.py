def selectionSort(data):
    # Start with the array length and decrement each time
    for i in range(len(data)-1, 0, -1):
       max_value_idx = 0
       for j in range(1, i+1):
           if data[j] > data[max_value_idx]:
               max_value_idx = j

       temp = data[i]
       data[i] = data[max_value_idx]
       data[max_value_idx] = temp

    return data
