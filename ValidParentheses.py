def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

input_string = "{[()]}"
if is_valid(input_string):
    print(f"The string '{input_string}' has valid parentheses.")
else:
    print(f"The string '{input_string}' does not have valid parentheses.")
