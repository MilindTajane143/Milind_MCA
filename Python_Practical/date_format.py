from datetime import datetime

def display_formatted_date(date_input):
    """
    Displays the date in the format: 'Friday, 23 April 2017'

    Parameters:
    date_input (str): Input date string in 'YYYY-MM-DD' format.
    """
    try:
        # Parse the input date string
        date_object = datetime.strptime(date_input, '%Y-%m-%d')
        # Format the date in the desired format
        formatted_date = date_object.strftime('%A, %d %B %Y')
        print(f"Formatted Date: {formatted_date}")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD' format.")

# Example usage
input_date = input("Enter a date (YYYY-MM-DD): ")
display_formatted_date(input_date)
