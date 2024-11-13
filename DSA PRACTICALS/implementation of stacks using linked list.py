class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        print(f"{item} pushed to stack.")

    def pop(self):
        if not self.is_empty():
            popped_value = self.top.value
            self.top = self.top.next
            return popped_value
        else:
            return "Stack is empty."
        
    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            return "Stack is empty."
        
    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Current stack:", elements)

stack_11 = StackLinkedList()
stack_11.push(10)
stack_11.push(20)
stack_11.push(30)
print("Top element:", stack_11.peek())
print("Popped element:", stack_11.pop())
stack_11.display()
