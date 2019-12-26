# Convert integer into binary number using stack
from stack.stack_using_pyList import PyListStack


def int_to_bin(int_num):
    """Converts integer into binary number using stack."""

    stack = PyListStack()

    while int_num > 0:
        remainder = int_num % 2
        stack.push(remainder)
        int_num = int_num // 2

    bin_num = ""
    while not stack.is_empty():
        bin_num += str(stack.pop())

    return bin_num


if __name__ == "__main__":

    print(int_to_bin(111))

