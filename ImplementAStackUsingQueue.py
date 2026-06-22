from collections import deque
class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            for _ in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
            return self.queue.popleft()
        else:
            raise IndexError("pop from an empty stack")

    def top(self):
        if not self.is_empty():
            for _ in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
            top_item = self.queue[0]
            self.queue.append(self.queue.popleft())  # Move the top item back to the end
            return top_item
        else:
            raise IndexError("top from an empty stack")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())    
    print(s.pop())    
    print(s.top())    
    print(s.size())   
    print(s.is_empty())
    