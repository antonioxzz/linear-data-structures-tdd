
def evaluate_postfix(expression):
    stack = []

    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b
    }

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            operator = operators[token]
            result = operator(operand1, operand2)
            stack.append(result)
        else:
            raise ValueError("Invalid token")

    return stack[0]  
