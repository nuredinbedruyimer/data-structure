from collections import deque


class Stack:
    def __init__(self):
        self.new_queue = deque([])
        self.all_queue = deque([])
    def push(self, data):
        self.new_queue.append(data)
        
        while self.all_queue:
            self.new_queue.append(self.all_queue.popleft())
        self.new_queue , self.all_queue = self.all_queue, self.new_queue
    def pop(self):
        return self.all_queue.popleft()
    def peek(self):
        return self.all_queue[0]
    def is_empty(self):
        return len(self.all_queue) == 0


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.is_empty())

    
