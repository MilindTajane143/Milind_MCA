# Define the generator function
def square_generator():
    for num in range(1, 11):
        yield num ** 2

# Use the generator function
if __name__ == "__main__":
    for line_number, square in enumerate(square_generator(), start=1):
        print(f"Square Of {line_number} = {square}")
