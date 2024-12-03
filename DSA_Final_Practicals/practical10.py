def find_largest_and_smallest(arr):
    """Find the largest and smallest elements in the array."""
    if not arr:
        return None, None  # If the array is empty, return None
    
    largest = smallest = arr[0]  # Initialize both largest and smallest to the first element
    
    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return largest, smallest

# Example usage
arr = [5, 3, 8, 1, 9, 2, 6]

largest, smallest = find_largest_and_smallest(arr)

print(f"Largest element: {largest}")
print(f"Smallest element: {smallest}")