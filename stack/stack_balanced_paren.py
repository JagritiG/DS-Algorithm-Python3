# Matching delimiters
from stack.stack_using_pyList import PyListStack


def is_paren_matched(input_string):
    """Return True if all delimiters are properly match; False otherwise."""

    opening_del = '({['             # opening delimiters
    closing_del = ')}]'             # respective closing delimiters
    stack = PyListStack()
    for c in input_string:
        if c in opening_del:
            stack.push(c)           # push opening delimiter on stack
        elif c in closing_del:
            if stack.is_empty():
                return False        # nothing to match with
            else:
                top = stack.pop()
                if closing_del.index(c) != opening_del.index(top):
                    return False        # mismatched

    return stack.is_empty()         # were all symbols matched?


if __name__ == "__main__":

    print(is_paren_matched("{This a test code}. (Check delimiters)"))
    print(is_paren_matched("{This a test code}. (Check delimiters}]"))

