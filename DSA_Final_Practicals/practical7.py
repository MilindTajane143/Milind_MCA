import heapq

class PriorityQueue:
    """Priority Queue implemented using a heap (min-heap)."""
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        """Insert an item with a given priority into the priority queue."""
        heapq.heappush(self.heap, (priority, item))  # Push as a tuple (priority, item)

    def pop(self):
        """Remove and return the item with the highest priority (lowest value)."""
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]  # Return only the item
        raise IndexError("Pop from an empty priority queue")

    def peek(self):
        """Return the item with the highest priority without removing it."""
        if not self.is_empty():
            return self.heap[0][1]  # Return only the item
        raise IndexError("Peek from an empty priority queue")

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0

    def display(self):
        """Display the contents of the priority queue."""
        print("Priority Queue contents:", self.heap)

# Example usage
pq = PriorityQueue()

# Insert items with priorities
pq.push("Task A", 3)
pq.push("Task B", 1)
pq.push("Task C", 2)

print("After adding tasks:")
pq.display()

# Get the item with the highest priority (lowest value)
print("\nPeek:", pq.peek())

# Remove items based on priority
print("\nPop:", pq.pop())
print("Pop:", pq.pop())

print("\nAfter popping tasks:")
pq.display()

# Check if the queue is empty
print("\nIs empty?", pq.is_empty())