# Evaluation of postfix expression using Stack
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


def evaluate_postfix(expr):

    stack = Stack()
    for i in range(len(expr)):

        # Push operand to stack
        # To convert expr[i] to digit subtract
        # '0' from expr[i].
        if is_operand(expr[i]):
            stack.push(ord(expr[i]) - ord("0"))

        else:

            # Operator encountered
            # Pop two elements (operands) from stack
            # Perform operation and push result to stack
            op2 = stack.pop()
            op1 = stack.pop()
            result = perform(expr[i], op1, op2)
            stack.push(result)

    return stack.peek()


def is_operand(char):

    # Check for operand. If character is a digit
    # then it is an operand
    return char.isdigit()


def perform(operator, val1, val2):

    if operator == '+':
        return val1 + val2

    if operator == '-':
        return val1 - val2

    if operator == '*':
        return val1 * val2

    if operator == '/':
        return val1 / val2


if __name__ == "__main__":

    test_expr = "34*52*-9+"
    print(evaluate_postfix(test_expr))
