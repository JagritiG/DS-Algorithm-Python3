#  Prefix to Infix conversion

# Pseudo code:

# PrefixToInfix(expr)
#   Create a stack
#   for i <-- length(expr)-1 to 0
#       if expr[i] is operand
#           stack.push(expr[i])
#
#       else if expr[i] is operator
#            op1 = stack.pop()
#            op2 = stack.pop()
#            result = opening_parenthesis + op1 + expr[i] + op2 + closing_parenthesis
#            stack.push(result)
#   return stack.top()
# ====================================================================================
# ====================================================================================


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
def prefix_to_infix(expr):

    stack = Stack()
    for i in range(len(expr) - 1, -1, -1):

        # If expr[i] is an operand, push it into stack
        if is_operand(expr[i]):
            stack.push(expr[i])

        # Operator encountered
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            result = "(" + op1 + expr[i] + op2 + ")"
            stack.push(result)

    return stack.peek()


def is_operand(char):
    """Checks for operand by checking If a given character
    is a digit/letter or not.
    """
    return char.isdigit() or char.isalpha()


if __name__ == "__main__":

    test_expr = "-+3*45*29"
    # test_expr = "*-A/BC-/DEC"
    print("Infix: " + prefix_to_infix(test_expr))

# Prefix: -+3*45*29
# Infix: ((3+(4*5))-(2*9))

# Prefix: *-A/BC-/DEC
# Infix: ((A-(B/C))*((D/E)-C))




