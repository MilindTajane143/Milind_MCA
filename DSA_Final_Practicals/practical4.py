# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        # Find the minimum element in the remaining unsorted portion
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
unsorted_list = [64, 25, 12, 22, 11]

print("Original List:", unsorted_list)

print("Insertion Sort:", insertion_sort(unsorted_list.copy()))
print("Selection Sort:", selection_sort(unsorted_list.copy()))
print("Bubble Sort:", bubble_sort(unsorted_list.copy()))
