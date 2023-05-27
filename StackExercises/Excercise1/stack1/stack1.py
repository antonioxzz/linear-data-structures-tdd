
def are_parentheses_balanced(expression):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if not stack or stack.pop() != matching[char]:
                return False

    return len(stack) == 0
