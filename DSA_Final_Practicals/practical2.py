# Singly Linked List Implementation Started
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print("Element not found.")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Singly Linked List Implementation End

# Doubly Linked List Implementation Started
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current and current.data != data:
            current = current.next
        if current:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
        else:
            print("Element not found.")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
# Doubly linked List Implementation End

# Circular Linked List Implementation Started
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == data:
            if self.head.next == self.head:  # Only one element
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        while current.next != self.head and current.next.data != data:
            current = current.next
        if current.next.data == data:
            current.next = current.next.next
        else:
            print("Element not found.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")
# Circular Linked List Implementation End

# Singly Linked List
print("Singly Linked List:")
sll = SinglyLinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.display()
sll.delete(2)
sll.display()

# Doubly Linked List
print("\nDoubly Linked List:")
dll = DoublyLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
dll.display()
dll.delete(2)
dll.display()

# Circular Linked List
print("\nCircular Linked List:")
cll = CircularLinkedList()
cll.add(1)
cll.add(2)
cll.add(3)
cll.display()
cll.delete(2)
cll.display()