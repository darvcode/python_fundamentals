from employee import Employee

class Company:
    def __init__(self):
        """
        Initialize a Company instance with an empty list of employees.
        """
        self.employees = []

    def add_employees(self, new_employee):
        """
        Add a new employee to the company's list of employees.
        """
        self.employees.append(new_employee)

    def display_employees(self):
        """
        Display the first name and last name of all current employees.
        """
        print('Current employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('--------------------------------')

    def pay_employee(self):
        """
        Calculate and display the weekly paycheck for each employee.
        """
        print('Salary per employee before taxes:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: {i.calculate_paycheck():,.2f}')
        print('--------------------------------')
        
def main():
    """
    Main function to create a Company instance, add employees,
    display employee list, and calculate paychecks.
    """
    my_company = Company()

    # Add employees to the company
    employee1 = Employee('Josh', 'R', 50000)
    my_company.add_employees(employee1)
    employee2 = Employee('Amy', 'G', 65000)
    my_company.add_employees(employee2)
    employee3 = Employee('Tom', 'A', 45000)
    my_company.add_employees(employee3)

    # Display current employees
    my_company.display_employees()

    # Calculate and display paychecks
    my_company.pay_employee()

# Run the main function
main()
