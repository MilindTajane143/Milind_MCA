def calculate_simple_interest(principal, rate, duration):
    return (principal * rate * duration) / 100
principal = float(input("Enter the principal amount: "))
duration = float(input("Enter the duration (in years): "))
rate = float(input("Enter the rate of interest (in %): "))
simple_interest = calculate_simple_interest(principal, rate, duration)
print(f"The simple interest is: {simple_interest:.2f}")
