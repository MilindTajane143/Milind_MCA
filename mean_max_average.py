def calculate_statistics(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    maximum = max(numbers)
    mean = total_sum / count if count > 0 else 0

    return total_sum, mean, maximum
numbers = [10, 20, 30, 40, 50]
total_sum, mean, maximum = calculate_statistics(numbers)
print(f"Sum: {total_sum}")
print(f"Mean: {mean:.2f}")
print(f"Maximum: {maximum}")
