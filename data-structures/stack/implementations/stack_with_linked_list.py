class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, data):
        curr_node = Node(data)
        if not curr_node:
            return "Stack Is Full"
        curr_node.next = self.head
        self.size += 1
        self.head = curr_node
    def is_empty(self):
        return self.head is None
    def pop(self):
        if self.is_empty():
            return "Stack Is Empty"
        popped_value = self.head.data
        self.size -= 1
        self.head = self.head.next
        return popped_value
    def peek(self):
        if self.is_empty():
            return "Stack Is Empty"
        return self.head.data
    def length(self):
        return self.size
    
    
    
    
    
stack = Stack()
print(stack.peek())
stack.push(1)
stack.push(5)
stack.push(10)
stack.push(20)
print(stack.length())

