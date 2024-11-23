def demonstrate_exceptions():
    print("\n--- Demonstrating Built-in Exceptions ---")

    # 1. ZeroDivisionError
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

    # 2. ValueError
    try:
        num = int("abc")  # Invalid conversion from string to int
    except ValueError as e:
        print(f"ValueError: {e}")

    # 3. IndexError
    try:
        lst = [1, 2, 3]
        print(lst[5])  # Index out of range
    except IndexError as e:
        print(f"IndexError: {e}")

    # 4. KeyError
    try:
        dictionary = {"a": 1, "b": 2}
        print(dictionary["c"])  # Accessing a non-existent key
    except KeyError as e:
        print(f"KeyError: {e}")

    # 5. FileNotFoundError
    try:
        with open("non_existent_file.txt", "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

    # 6. TypeError
    try:
        result = "10" + 5  # Adding string and integer
    except TypeError as e:
        print(f"TypeError: {e}")

    # 7. AttributeError
    try:
        num = 10
        num.append(5)  # `int` has no `append` method
    except AttributeError as e:
        print(f"AttributeError: {e}")

    # 8. ImportError
    try:
        from math import non_existent_function  # Non-existent import
    except ImportError as e:
        print(f"ImportError: {e}")

    # 9. NameError
    try:
        print(undefined_variable)  # Variable not defined
    except NameError as e:
        print(f"NameError: {e}")

    # 10. OverflowError
    try:
        import math
        print(math.exp(1000))  # Exceeds the limit of floating-point numbers
    except OverflowError as e:
        print(f"OverflowError: {e}")

    print("\n--- End of Demonstration ---")

# Main program
if __name__ == "__main__":
    demonstrate_exceptions()