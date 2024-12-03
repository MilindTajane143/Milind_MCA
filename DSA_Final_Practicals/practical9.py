class CircularQueue:
    """Circular Queue implementation using a list."""
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        """Add an element to the queue."""
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")
        elif self.front == -1:  # First element being added
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        """Remove an element from the queue."""
        if self.front == -1:
            print("Queue is empty!")
            return None
        elif self.front == self.rear:  # Only one element left
            value = self.queue[self.front]
            self.front = self.rear = -1
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.size
        return value

    def display(self):
        """Display the elements of the queue."""
        if self.front == -1:
            print("Queue is empty!")
            return
        print("Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front == -1

    def is_full(self):
        """Check if the queue is full."""
        return (self.rear + 1) % self.size == self.front

# Example usage
cq = CircularQueue(5)

# Enqueue elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

print("\nQueue after enqueues:")
cq.display()

# Dequeue elements
print("\nDequeue:", cq.dequeue())
print("Dequeue:", cq.dequeue())

print("\nQueue after dequeues:")
cq.display()

# Add more elements
cq.enqueue(50)
cq.enqueue(60)

print("\nQueue after adding more elements:")
cq.display()

# Try to add to a full queue
cq.enqueue(70)