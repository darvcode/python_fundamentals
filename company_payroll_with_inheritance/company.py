from employee import SalaryEmployee, HourlyEmployee, ComissionEmployee

class Company:
    def __init__(self):
        """
        Initialize a Company instance with an empty list of employees.
        """
        self.employees = []

    def add_employee(self, new_employee):
        """
        Add a new employee to the company's list of employees.
        """
        self.employees.append(new_employee)

    def display_employees(self):
        """
        Display the first name and last name of all current employees.
        """
        print('Current Employees')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------------------')
    
    def pay_employees(self):
        """
        Calculate and display the weekly paycheck for each employee.
        """
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('------------------------')

def main():
    """
    Main function to create a Company instance, add employees,
    display employee list, and calculate paychecks.
    """
    my_company = Company()

    # Add employees to the company
    employee1 = SalaryEmployee('Bob', 'H', 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Tom', 'G', 25, 50)
    my_company.add_employee(employee2)
    employee3 = ComissionEmployee('Rich', 'T', 35000, 5, 200)
    my_company.add_employee(employee3)

    # Display current employees
    my_company.display_employees()

    # Calculate and display paychecks
    my_company.pay_employees()

# Run the main function
main()