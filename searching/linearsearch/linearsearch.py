def linearSearch(data_list, val):
    """Returns True if value is found in the list. Otherwise returns False"""
    index = 0
    found = False
    while index < len(data_list) and not found:
        if data_list[index] == val:
            found = True
        else:
            index += 1

    return found

