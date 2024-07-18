class Employee:
    def __init__(self, fname, lname, salary):
            """
            Initialize an Employee instance with first name, last name, and salary.
            """
            self.fname = fname
            self.lname = lname
            self.salary = salary

    def calculate_paycheck(self):
        """
        Calculate the weekly paycheck amount.
        """
        return self.salary / 52
    