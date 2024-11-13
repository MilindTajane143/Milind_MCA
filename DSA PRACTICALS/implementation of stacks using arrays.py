class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f" {item} pushed to stack.")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is Empty."
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is Empty."
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("Current stack:", self.stack)

stack = Stack ()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
print("Top element:", stack.peek())
print("Bottom element:", stack.pop())
stack.display()
