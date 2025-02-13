# Define the decorator
def cube_decorator(func):
    def wrapper(num):
        result = func(num)
        print(f"The cube of {num} is {result}")
        return result
    return wrapper

# Use the decorator on a function
@cube_decorator
def cube(num):
    return num ** 3

# Test the function
if __name__ == "__main__":
    number = int(input("Enter a number: "))
cube(number)
