from Employeemgmt.empsalary import calculate_salary
from Employeemgmt.emphrinfo import display_employee_info

def main():
    print("Welcome to Employee Management System")

    # Input for employee information
    name = input("Enter employee's name: ")
    designation = input("Enter employee's designation: ")
    dept = input("Enter employee's department: ")
    qualification = input("Enter employee's qualification: ")
    experience = int(input("Enter employee's experience (in years): "))

    # Display employee information
    display_employee_info(name, designation, dept, qualification, experience)

    # Input for salary calculation
    basic_salary = float(input("\nEnter employee's basic salary: "))
    hra_percentage = float(input("Enter HRA percentage (default is 20): ") or 20)
    tax_percentage = float(input("Enter tax percentage (default is 10): ") or 10)

    # Calculate and display salary details
    gross_salary, net_salary = calculate_salary(basic_salary, hra_percentage, tax_percentage)
    print("\n--- Salary Details ---")
    print(f"Gross Salary: {gross_salary:.2f}")
    print(f"Net Salary: {net_salary:.2f}")

if __name__ == "__main__":
    main()
