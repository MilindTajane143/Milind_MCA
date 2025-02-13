def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    :param arr: Sorted list of elements
    :param target: Element to search for
    :return: Index of the target element or -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    return -1  # Target not found

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(sorted_list, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
