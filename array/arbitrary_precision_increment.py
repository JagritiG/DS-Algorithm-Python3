# Adding one to number represented by digits
import math


# Method-1
# def increment_by_one(arr):
#
#     n = len(arr)
#
#     # Add 1 to last digit and find carry
#     arr[n-1] += 1
#     carry = arr[n-1]/10
#     arr[n-1] = arr[n-1] % 10
#
#     # Traverse from second last digit
#     for j in range(n-2, -1, -1):
#         if carry == 1:
#             arr[j] += 1
#             carry = arr[j]/10
#             arr[j] = arr[j] % 10
#
#     # If carry is 1, we need to add a 1 at the beginning of number
#     if carry == 1:
#         arr.insert(0, 1)

# Method-2
def increment_by_one(arr):
    arr[-1] += 1
    for j in reversed(range(1, len(arr))):
        if arr[j] != 10:
            break
        arr[j] = 0
        arr[j-1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr


if __name__ == "__main__":

    a1 = [1, 4, 9]
    a2 = [9, 9, 9]
    increment_by_one(a1)
    increment_by_one(a2)
    print(a1)
    for i in range(0, len(a1)):
            print(a1[i], end=" ")

    print("\n")
    print(a2)
    for j in range(0, len(a2)):
        print(a2[j], end=" ")

