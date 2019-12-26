# Reversing data using stack
from stack.stack_using_pyList import PyListStack


# ToDo: Reverse the File data using stack
def reverse_file(fl_name):
    """Overwrite given file with its contents line-by-line reversed."""

    stack = PyListStack()
    original_file = open(fl_name)
    for line in original_file:
        stack.push(line.rstrip('\n'))           # re-insert newlines when writing
    original_file.close()

    # Overwrite with contents in LIFO order
    reversed_file = open(fl_name, 'w')                # reopening file overwrites original
    while not stack.is_empty():
        reversed_file.write(stack.pop() + '\n')       # re-insert newline characters
    reversed_file.close()


if __name__ == "__main__":

    filename = "/Users/santanusarma/Dropbox/Jagriti/Programming/Python3/DS and Algorithm/stack/example_reversing_stack.txt"
    f_before = open(filename)
    for line_before in f_before:
       print(line_before)
    f_before.close()
    print("Lines after reversing: \n")
    reverse_file(filename)
    f_after = open(filename)
    for line_after in f_after:
       print(line_after)
    f_after.close()

