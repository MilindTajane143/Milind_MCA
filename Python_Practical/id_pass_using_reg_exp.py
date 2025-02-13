import re

# Function to validate an email ID
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Function to validate a password
def validate_password(password):
    """
    Password criteria:
    - At least 8 characters long
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

# Function to validate a URL
def validate_url(url):
    pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/\S*)?$'
    return re.match(pattern, url) is not None

# Function to validate a mobile number
def validate_mobile(mobile):
    """
    Mobile number criteria:
    - 10 digits
    - Starts with 7, 8, or 9
    """
    pattern = r'^[789]\d{9}$'
    return re.match(pattern, mobile) is not None

# Main Program
def main():
    # Validate email
    email = input("Enter email ID: ")
    if validate_email(email):
        print("Valid Email ID")
    else:
        print("Invalid Email ID")

    # Validate password
    password = input("Enter password: ")
    if validate_password(password):
        print("Valid Password")
    else:
        print("Invalid Password. Must contain at least 8 characters, one uppercase, one lowercase, one digit, and one special character.")

    # Validate URL
    url = input("Enter URL: ")
    if validate_url(url):
        print("Valid URL")
    else:
        print("Invalid URL")

    # Validate mobile number
    mobile = input("Enter mobile number: ")
    if validate_mobile(mobile):
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile Number. Must be 10 digits and start with 7, 8, or 9.")

if __name__ == "__main__":
    main()
