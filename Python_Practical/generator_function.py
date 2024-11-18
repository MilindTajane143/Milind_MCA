# Define the generator function
def square_generator():
    for num in range(1, 11):
        yield num ** 2

# Use the generator function
if __name__ == "__main__":
    print("Squares of numbers from 1 to 10:")
    for square in square_generator():
        print(square)
