def print_right_angle_triangle(n):
    print("Right-Angle Triangle:")
    for i in range(1, n + 1):
        print('*' * i)
    print()

def print_isosceles_triangle(n):
    print("Isosceles Triangle:")
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    print()

def print_inverted_triangle(n):
    print("Inverted Triangle:")
    for i in range(n, 0, -1):
        print('*' * i)
    print()

def print_full_pyramid(n):
    print("Full Pyramid:")
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    print()

def print_diamond(n):
    print("Diamond Shape:")
    # Upper part
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    # Lower part
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    print()

# Set the height of the pyramids
n = 5
print_right_angle_triangle(n)
print_isosceles_triangle(n)
print_inverted_triangle(n)
print_full_pyramid(n)
print_diamond(n)
