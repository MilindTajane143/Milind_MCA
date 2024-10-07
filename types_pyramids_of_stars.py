def print_pyramid(n, row=1):
    if row > n: return
    print(' ' * (n - row) + '💕' * (1 * row - 1))
    print_pyramid(n, row + 1)

print_pyramid(10)
