# Function to calculate simple interest
def calculate_simple_interest(principal, duration, rate=5.0):
    """
    Calculate simple interest using the formula: (P * R * T) / 100
    :param principal: Principal amount (float)
    :param duration: Duration in years (float)
    :param rate: Rate of interest in % (float, default is 5.0)
    :return: Simple interest (float)
    """
    return (principal * rate * duration) / 100

# Prompt the user to enter the principal amount and convert it to a float
principal = float(input("Enter the principal amount: "))

# Prompt the user to enter the duration in years and convert it to a float
duration = float(input("Enter the duration (in years): "))

# Calculate simple interest using the user inputs and default rate
simple_interest = calculate_simple_interest(principal, duration)

# Print the calculated simple interest, formatted to two decimal places
print(f"The simple interest is: {simple_interest:.2f}")
