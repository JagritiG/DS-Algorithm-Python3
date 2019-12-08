# 1. Reversing data using stack
# 2. Matching delimiters and
# 3. Matching HTML Tags using stack
from stack.stack_using_pyList import PyListStack


# ToDo: Reverse the File data using stack
def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""

    stack = PyListStack()
    original_file = open(filename)
    for line in original_file:
        stack.push(line.rstrip('\n'))           # we will re-insert newlines when writing
    original_file.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')                # reopening file overwrites original
    while not stack.is_empty():
        output.write(stack.pop() + '\n')        # re-insert newline characters
    output.close()


# ToDo: Match delimiters using stack
def is_matched(expr):
    """Return True if all delimeters are properly match; False otherwise."""

    lefty = '({['                   # opening delimiters
    righty = ')}]'                  # respective closing delimiters
    stack = PyListStack()
    for c in expr:
        if c in lefty:
            stack.push(c)           # push left delimiter on stack
        elif c in righty:
            if stack.is_empty():
                return False        # nothing to match with
            if righty.index(c) != lefty.index(stack.pop()):
                return False        # mismatched

    return stack.is_empty()         # were all symbols matched?


# ToDo: Match HTML Tags using stack
def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    stack = PyListStack()
    j = raw.find('<')               # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j+1)      # find next '>' character
        if k == -1:
            return False            # invalid tag
        tag = raw[j+1:k]            # strip away <>
        if not tag.startswith('/'):     # this is opening tag
            stack.push(tag)
        else:
            if stack.is_empty():
                return False        # nothing to match with
            if tag[1:] != stack.pop():
                return False        # mismatched delimiter
        j = raw.find('<', k+1)      # find next '<' character (if any)
    return stack.is_empty()         # were all opening tags matched?


if __name__ == "__main__":
    # execute only if run as a script

    # ToDo: call function reverse_file()
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

    # ToDo: call function is_matched()
    expression = "{This a test code}. (Check delimeters)"
    print(is_matched(expression))

    # ToDo: call function is_matched_html()
    raw_html = """<body>
               <center>
               <h1> Example of matching html tags </h1>
               </center>
               </body>"""
    print(is_matched_html(raw_html))

