from collections import Counter

def calculate_statistics(numbers):
    if not numbers:
        return None, None, None, None, None
    
    # Calculate sum
    total_sum = sum(numbers)
    
    # Calculate minimum
    minimum = min(numbers)
    
    # Calculate maximum
    maximum = max(numbers)
    
    # Calculate mean
    mean = total_sum / len(numbers)
    
    # Calculate mode
    frequency = Counter(numbers)
    mode_data = frequency.most_common()
    mode = [num for num, freq in mode_data if freq == mode_data[0][1]]
    
    return total_sum, minimum, maximum, mean, mode

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
total_sum, minimum, maximum, mean, mode = calculate_statistics(numbers)

print(f"Sum: {total_sum}")
print(f"Min: {minimum}")
print(f"Max: {maximum}")
print(f"Mean: {mean}")
print(f"Mode: {mode}")
