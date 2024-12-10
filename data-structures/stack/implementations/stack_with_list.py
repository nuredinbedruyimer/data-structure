class Stack:
    def __init__(self, arr = [], capacity = 100000):
        self.stack = arr
        self.top = len(arr) - 1 if arr else -1
        self.capacity = capacity
    def peek(self):
        return "Stack is Empty" if self.top == -1  else self.top
    def is_empty(self):
        return self.top == -1
    def length(self):
        return self.top + 1
    def is_full(self):
        return self.capacity - 1 == self.top
    def pop(self):
        if self.is_empty():
            return "Stack Is Empty"
        else:
            self.top -= 1
            return self.stack.pop()
 
            
    def push(self, value):
        if self.is_full():
            return "Stack Is Full"
        else:
            self.stack.append(value)
            self.top += 1
        return True


stk = Stack([1, 5])

stk.push(10)
stk.push(20)

print(stk.length())
    