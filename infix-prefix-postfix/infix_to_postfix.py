# Infix to postfix conversion using Stack
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        if self.items:
            return self.items[-1]

        return None

    def is_empty(self):
        return self.items == []


# When expression is without parenthesis
def _infix_to_postfix_without_paren(expr):

    stack = Stack()
    result = ""
    for i in range(len(expr)):

        # Append operand to the string
        if is_operand(expr[i]):
            result = result + str(expr[i])

        else:

            # Operator encountered
            while not stack.is_empty() and (prec_priority(stack.peek()) >= prec_priority(expr[i])):
                result = result + str(stack.peek())
                stack.pop()
            stack.push(expr[i])

    while not stack.is_empty():
        result = result + str(stack.peek())
        stack.pop()

    return result


# When expression is with parenthesis
def infix_to_postfix(expr):

    stack = Stack()
    result = ""
    for i in range(len(expr)):

        # Append operand to the string
        if is_operand(expr[i]):
            result = result + str(expr[i])

        # Operator encountered
        elif is_operator(expr[i]):
            while not stack.is_empty() and not opening_delimiter(stack.peek()) \
                    and (prec_priority(stack.peek()) >= prec_priority(expr[i])):
                result = result + str(stack.peek())
                stack.pop()
            stack.push(expr[i])

        elif opening_delimiter(expr[i]):
            stack.push(expr[i])

        elif closing_delimiter(expr[i]):
            while not stack.is_empty() and not opening_delimiter(stack.peek()):
                result = result + str(stack.peek())
                stack.pop()
            stack.pop()

    while not stack.is_empty():
        result = result + str(stack.peek())
        stack.pop()

    return result


def is_operand(char):
    """Checks for operand by checking If a given character
    is a digit/letter or not.
    """
    return char.isdigit() or char.isalpha()


def is_operator(char):
    """Checks for operator."""

    operator = '+-*/'
    if char in operator:
        return True
    else:
        return False


def prec_priority(op):
    """Finds priority of given operator."""
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def opening_delimiter(delimiter):

    opening_del = '({['
    if delimiter in opening_del:
        return True
    else:
        return False


def closing_delimiter(delimiter):

    closing_del = ')}]'
    if delimiter in closing_del:
        return True
    else:
        return False


if __name__ == "__main__":

    # test_expr = "3+4*5-2*9"
    # test_expr = "A+B*C-D/E"
    # test_expr = "2*(3+4)"
    # test_expr = "A*(B+C)"
    test_expr = "(A-B/C)*(D/E-C)"
    print(infix_to_postfix(test_expr))

# Infix: "3+4*5-2*9"
# Postfix: 345*+29*-

# Infix: A+B+C-D/E
# Postfix: ABC*+DE/-

# Infix: "3+4*5-2*9"
# Postfix: 345*+29*-

# Infix: "A*(B+C)"
# Postfix: ABC+*

# Infix: "(A-B/C)*(D/E-C)"
# Postfix: ABC/-DE/C-*
