class Node:
    """Node class for Binary Search Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, current, key):
        if current is None:
            return current
        if key < current.key:
            current.left = self._delete(current.left, key)
        elif key > current.key:
            current.right = self._delete(current.right, key)
        else:
            # Node with only one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._find_min(current.right)
            current.key = min_larger_node.key
            current.right = self._delete(current.right, min_larger_node.key)
        return current

    def _find_min(self, node):
        """Find the node with the smallest key."""
        while node.left is not None:
            node = node.left
        return node

    def in_order_traversal(self):
        """Perform in-order traversal of the BST."""
        return self._in_order_traversal(self.root, [])

    def _in_order_traversal(self, current, result):
        if current is not None:
            self._in_order_traversal(current.left, result)
            result.append(current.key)
            self._in_order_traversal(current.right, result)
        return result

# Example usage
bst = BinarySearchTree()
# Insert elements
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("In-order traversal after insertion:", bst.in_order_traversal())

# Delete elements
bst.delete(20)
print("In-order traversal after deleting 20:", bst.in_order_traversal())

bst.delete(30)
print("In-order traversal after deleting 30:", bst.in_order_traversal())

bst.delete(50)
print("In-order traversal after deleting 50:", bst.in_order_traversal())
