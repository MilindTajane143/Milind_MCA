# Dictionary to store student records
student_records = {}

# Function to add a new record
def add_record(roll_number, marks):
    if roll_number in student_records:
        print("Roll number already exists!")
    else:
        student_records[roll_number] = marks
        print("Record added successfully!")

# Function to delete a record
def delete_record(roll_number):
    if roll_number in student_records:
        del student_records[roll_number]
        print("Record deleted successfully!")
    else:
        print("Roll number not found!")

# Function to update marks
def update_marks(roll_number, marks):
    if roll_number in student_records:
        student_records[roll_number] = marks
        print("Marks updated successfully!")
    else:
        print("Roll number not found!")

# Function to search for a roll number and display marks
def search_roll_number(roll_number):
    if roll_number in student_records:
        print(f"Roll Number: {roll_number}, Marks: {student_records[roll_number]}")
    else:
        print("Roll number not found!")

# Function to display all records sorted in ascending order
def display_sorted_ascending():
    sorted_records = sorted(student_records.items())
    print("Records in ascending order:")
    for roll, marks in sorted_records:
        print(f"Roll Number: {roll}, Marks: {marks}")

# Function to display all records sorted in descending order
def display_sorted_descending():
    sorted_records = sorted(student_records.items(), reverse=True)
    print("Records in descending order:")
    for roll, marks in sorted_records:
        print(f"Roll Number: {roll}, Marks: {marks}")

# Function to display the student with the highest marks
def display_highest_marks():
    if student_records:
        highest = max(student_records.items(), key=lambda x: x[1])
        print(f"Student with highest marks: Roll Number: {highest[0]}, Marks: {highest[1]}")
    else:
        print("No records available!")

# Menu-driven program
def menu():
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Update marks")
        print("4. Search a roll number")
        print("5. Display records in ascending order")
        print("6. Display records in descending order")
        print("7. Display student with highest marks")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            roll = input("Enter roll number: ")
            marks = float(input("Enter marks: "))
            add_record(roll, marks)
        elif choice == "2":
            roll = input("Enter roll number to delete: ")
            delete_record(roll)
        elif choice == "3":
            roll = input("Enter roll number to update: ")
            marks = float(input("Enter new marks: "))
            update_marks(roll, marks)
        elif choice == "4":
            roll = input("Enter roll number to search: ")
            search_roll_number(roll)
        elif choice == "5":
            display_sorted_ascending()
        elif choice == "6":
            display_sorted_descending()
        elif choice == "7":
            display_highest_marks()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
menu()
