class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("\nEmployee Details")
        print("----------------")
        print("Name:", self.name)
        print("Salary:", self.salary)

    def annual_salary(self):
        annual = self.salary * 12
        print("Annual Salary:", annual)

    def increment_salary(self, amount):
        self.salary = self.salary + amount
        print("\nSalary incremented by:", amount)
        print("Updated Salary:", self.salary)


# Create Employee Objects
employee1 = Employee("Keerthi", 15000)
employee2 = Employee("Rahul", 25000)

# Display Initial Details
employee1.display()
employee2.display()

# Display Annual Salary
print()
employee1.annual_salary()
employee2.annual_salary()

# Increment Salary
print()
employee1.increment_salary(5000)

# Display Updated Details
employee1.display()