def calculate_salary(basic_salary, hra_percentage=20, tax_percentage=10):
    hra = (hra_percentage / 100) * basic_salary
    gross_salary = basic_salary + hra
    tax = (tax_percentage / 100) * gross_salary
    net_salary = gross_salary - tax
    return gross_salary, net_salary
