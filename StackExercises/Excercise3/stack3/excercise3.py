
def reverse_string(input_string):
    stack = []

    for char in input_string:
        stack.append(char)

    reversed_string = ""

    while stack:
        reversed_string += stack.pop()

    return reversed_string

input_string = "Hello world"
reversed_string = reverse_string(input_string)
print(reversed_string)
