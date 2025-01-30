class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def peek(self): #function for peeking
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]

    def display(self):
        print("Stack:", self.stack)

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.display()
print("Popped element:", stack.pop())
stack.display()
print("Font element:", stack.peek())
