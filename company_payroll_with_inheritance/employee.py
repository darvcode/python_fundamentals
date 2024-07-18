class Employee:
    def __init__(self, fname, lname):
        """
        Initialize an Employee instance with first name and last name.
        """
        self.fname = fname
        self.lname = lname
    
class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        """
        Initialize a SalaryEmployee instance with first name, last name, and salary.
        """
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        """
        Calculate the weekly paycheck amount for a salaried employee.
        """
        return self.salary / 52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        """
        Initialize an HourlyEmployee instance with first name, last name, 
        weekly hours, and hourly rate.
        """
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        """
        Calculate the weekly paycheck amount for an hourly employee.
        """
        return self.weekly_hours * self.hourly_rate
    
class ComissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        """
        Initialize a CommissionEmployee instance with first name, last name,
        salary, number of sales, and commission rate.
        """
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    
    def calculate_paycheck(self):
        """
        Calculate the weekly paycheck amount for a commission employee.
        """
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_num * self.com_rate
        return regular_salary + total_commission
