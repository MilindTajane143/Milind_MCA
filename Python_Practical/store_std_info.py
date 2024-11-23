class Student:
    # Class Attribute
    total_students = 0

    # Constructor
    def __init__(self, student_id, name, marks):
        # Public Instance Attributes
        self.student_id = student_id
        self.name = name
        
        # Private Instance Attribute
        self.__marks = marks
        
        # Increment class attribute
        Student.total_students += 1
        print(f"Student {self.name} added successfully!")

    # Destructor
    def __del__(self):
        # Decrement class attribute
        Student.total_students -= 1
        print(f"Student {self.name} removed from records.")

    # Instance Method to Display Student Info
    def display_info(self):
        print("\n--- Student Information ---")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.__marks}")

    # Getter for Marks (Private Attribute)
    def get_marks(self):
        return self.__marks

    # Setter for Marks (Private Attribute)
    def set_marks(self, marks):
        if 0 <= marks <= 100:  # Validating marks range
            self.__marks = marks
            print(f"Marks updated for {self.name}.")
        else:
            print("Invalid marks! Must be between 0 and 100.")

    # Class Method to Display Total Students
    @classmethod
    def display_total_students(cls):
        print(f"\nTotal Students: {cls.total_students}")

    # Static Method Example: Validating Marks
    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100

# Main Program
def main():
    # Creating Student Instances
    student1 = Student(1, "Milind Tajane", 85)
    student2 = Student(2, "Gayatri Jadhav", 92)

    # Display Student Information
    student1.display_info()
    student2.display_info()

    # Using Getter and Setter for Marks
    print(f"\nMarks for {student1.name}: {student1.get_marks()}")
    student1.set_marks(95)
    print(f"Updated Marks for {student1.name}: {student1.get_marks()}")

    # Demonstrate Class Method
    Student.display_total_students()

    # Demonstrate Static Method
    print(f"Are 105 marks valid? {Student.is_valid_marks(105)}")
    print(f"Are 95 marks valid? {Student.is_valid_marks(95)}")

    # Delete a Student Instance
    del student1

    # Display Total Students After Deletion
    Student.display_total_students()

# Run the Program
if __name__ == "__main__":
    main()
