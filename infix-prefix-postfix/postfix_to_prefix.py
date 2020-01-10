# Postfix to Prefix conversion

# Pseudo code:

# PostfixToPrefix(expr)
#   Create a stack
#   for i <-- o to length(expr)-1
#       if expr[i] is operand
#           stack.push(expr[i])
#
#       else if expr[i] is operator
#            op1 = stack.pop()
#            op2 = stack.pop()
#            result = expr[i] + op2 + op1
#            stack.push(result)
#   return stack.top()
# ==============================================================
# ==============================================================


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


# Function which converts infix to prefix expression
def postfix_to_prefix(expr):

    stack = Stack()
    for i in range(len(expr)):

        # If expr[i] is an operand, push it into stack
        if is_operand(expr[i]):
            stack.push(expr[i])

        # Operator encountered
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            result = expr[i] + op2 + op1
            stack.push(result)

    return stack.peek()


def is_operand(char):
    """Checks for operand by checking If a given character
    is a digit/letter or not.
    """
    return char.isdigit() or char.isalpha()


if __name__ == "__main__":

    # test_expr = "345*+29*-"
    test_expr = "ABC/-DE/C-*"
    print("Prefix: " + postfix_to_prefix(test_expr))

# Postfix: 345*+29*-
# Prefix: -+3*45*29

# Postfix: ABC/-DE/C-*
# Prefix: *-A/BC-/DEC
