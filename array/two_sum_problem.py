# Return the two numbers from a sorted array such that they add up to a specific target
# assume each input have exactly one solution and can not use same number twice


# Method-1: using brute force
# Time complexity: O(n^2)
# Space complexity: O(1)
# def two_sum(arr, sum_val):
#     for i in range(len(arr) - 1):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == sum_val:
#                 print((arr[i], arr[j]))
#                 return True
#
#     return False

# Method-2: using hash table
# Time complexity: O(n)
# Space complexity: O(n)
# def two_sum(arr, sum_val):
#
#     hast_table = dict()
#     for i in range(len(arr)):
#         if arr[i] in hast_table:
#             print(hast_table[arr[i]], arr[i])
#             return True
#         else:
#             hast_table[sum_val - arr[i]] = arr[i]
#             print(hast_table)
#
#     return False

# Method-3: traverse from both side towards middle
# Time complexity: O(n)
# Space complexity: O(1)
def two_sum(arr, sum_val):
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] + arr[j] == sum_val:
            print(arr[i], arr[j])
            return True
        elif arr[i] + arr[j] < sum_val:
            i += 1

        # arr[i] + arr[j] > sum_val
        else:
            j -= 1

    return False


if __name__ == "__main__":

    a = [2, 3, 4, 6, 7, 9]
    target = 10
    print(two_sum(a, target))
