def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
input_string = "Hello"
reversed_string = reverse_string(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}")

