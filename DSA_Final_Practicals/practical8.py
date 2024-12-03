class HashTable:
    """Hash Table implementation with chaining for collision handling."""
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Compute the hash value of a key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if the key already exists in the chain
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        # If not, append a new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        """Search for a value by its key."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  # Key not found

    def display(self):
        """Display the contents of the hash table."""
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

# Example usage
hash_table = HashTable(5)

# Insert key-value pairs
hash_table.insert("Alice", 25)
hash_table.insert("Bob", 30)
hash_table.insert("Charlie", 35)
hash_table.insert("David", 40)
hash_table.insert("Eve", 45)  # May collide with another key

print("Hash Table after insertion:")
hash_table.display()

# Search for keys
print("\nSearch results:")
print("Alice:", hash_table.search("Alice"))
print("Bob:", hash_table.search("Bob"))
print("Zara:", hash_table.search("Zara"))  # Key not present

# Delete a key
print("\nDeleting 'Charlie'...")
hash_table.delete("Charlie")

print("\nHash Table after deletion:")
hash_table.display()