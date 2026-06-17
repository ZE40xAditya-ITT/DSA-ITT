class stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    def is_empty(self):
        return len(self.stack) == 0
my_stack = stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print("Stack after pushing 10, 20, 30:", my_stack.stack)
print("Top element:", my_stack.peek())
print("Popped element:", my_stack.pop())
print("Top element after pop:", my_stack.peek())
print("Is stack empty?", my_stack.is_empty())
my_stack.pop()
my_stack.pop()
print("Is stack empty after popping all elements?", my_stack.is_empty())
