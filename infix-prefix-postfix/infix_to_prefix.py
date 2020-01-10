# Infix to prefix conversion using two Stack
# Pseudo code:
# InfixToPrefix(expr)
#
#   Create a stack S1 for operand
#   Create another stack S2 for operator
#   result <-- empty string
#   for i <-- o to length(expr)-1
#   {
#
#       # If current character is an operand
#       # then push it into operands stack.
#
#       if expr[i] is operand
#           result <-- result + expr[i]
#           s1.push(result)
#
#       # If current character is an operator,
#       # then push it into operator stack after
#       # popping high priority operator from
#       # operator stack and pushing result in operand stack.
#
#       else if expr[i] is operator
#       {
#           while (!s2.empty() && !OpeningParenthesis(s2.top) &&
#                       (precedence(expr[i] <= precedence(s2.top()))
#           {
#               op1 = s1.pop()
#               op2 = s1.pop()
#               result <-- expr[i] + op1 + op2
#               s1.push(result)
#            }
#            s2.push(expr[i])
#
#       }
#
#       # If current character is an opening parenthesis,
#       # then push into the operators stack.
#
#       else if expr[i] is OpeningParenthesis:
#       {
#           s2.push(expr[i])
#       }
#
#       # If current character is a closing bracket, then pop from
#       # both stacks and push result in operand stack until
#       # matching opening bracket is not found.
#       else if (expr[i] is ClosingParenthesis):
#       {
#           while (!s2.empty() && !OpeningParenthesis(s2.top)):
#           {
#               op1 = s1.pop()
#               op2 = s1.pop()
#               operator = s2.pop()
#               result <-- operator + op1 + op2
#               s1.push(result)
#           }
#           # Pop opening parenthesis from stack
#           s2.pop()
#       }
#
#      # Pop operators from operator stack
#      # until it is empty and add result
#      # of each pop operation in operand stack.
#
#      while (!s2.empty)
#      {
#          op1 = s1.pop()
#          op2 = s1.pop()
#          operator = s2.pop()
#          result <-- operator + op1 +op2
#          s1.push(result)
#      }
#
#      # Final prefix expression is
#      # present in operand stack.
#
#       return s1.top()
#
# ========================================================================
# ========================================================================


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
def infix_to_prefix(expr):

    operand_stack = Stack()
    operator_stack = Stack()
    for i in range(len(expr)):

        # Append operand to the string and push it into operand stack
        if is_operand(expr[i]):
            result = str(expr[i])
            operand_stack.push(result)

        # Operator encountered
        elif is_operator(expr[i]):
            while not operator_stack.is_empty() and not opening_delimiter(operator_stack.peek()) \
                    and (prec_priority(expr[i]) <= prec_priority(operator_stack.peek())):

                op1 = operand_stack.pop()
                op2 = operand_stack.pop()
                operator = operator_stack.pop()
                result = operator + op2 + op1
                operand_stack.push(result)

            operator_stack.push(expr[i])

        elif opening_delimiter(expr[i]):
            operator_stack.push(expr[i])

        elif closing_delimiter(expr[i]):
            while not operator_stack.is_empty() and not opening_delimiter(operator_stack.peek()):
                op1 = operand_stack.pop()
                op2 = operand_stack.pop()
                operator = operator_stack.pop()
                result = operator + op2 + op1
                operand_stack.push(result)

            operator_stack.pop()

    while not operator_stack.is_empty():
        op1 = operand_stack.pop()
        op2 = operand_stack.pop()
        operator = operator_stack.pop()
        result = operator + op2 + op1
        operand_stack.push(result)

    return operand_stack.peek()


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

    test_expr = "3+4*5-2*9"
    # test_expr = "(A-B/C)*(D/E-C)"
    # test_expr = "2*(3+4)"
    # test_expr = "A+(B*C)"
    print(infix_to_prefix(test_expr))

# Infix: 3+4*5-2*9
# Prefix: -+3*45*29

# Infix: (A-B/C)*(D/E-C)
# Prefix: *-A/BC-/DEC

# Infix: "A+(B*C)"
# Prefix: +A*BC

