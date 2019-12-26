# Matching HTML Tags using stack
from stack.stack_using_pyList import PyListStack


# ToDo: Match HTML Tags using stack
def is_html_matched(raw):
    """Return True if all HTML tags are properly matched; False otherwise."""
    stack = PyListStack()
    c1 = raw.find('<')                # find first '<' character (if any)
    while c1 != -1:
        c2 = raw.find('>', c1+1)      # find next '>' character
        if c2 == -1:
            return False              # invalid tag
        tag = raw[c1+1:c2]            # strip away <>
        if not tag.startswith('/'):   # this is opening tag
            stack.push(tag)
        else:
            if stack.is_empty():
                return False          # nothing to match with
            if tag[1:] != stack.pop():
                return False          # mismatched delimiter
        c1 = raw.find('<', c2+1)      # find next '<' character (if any)
    return stack.is_empty()           # were all opening tags matched?


if __name__ == "__main__":

    raw_html1 = """<body>
               <center>
               <h1> Example of matching html tags </h1>
               </center>
               </body>"""
    print(is_html_matched(raw_html1))

    raw_html2 = """<body>
               <center>
               <h1> Example of matching html tags </h1>
               </body>"""
    print(is_html_matched(raw_html2))

