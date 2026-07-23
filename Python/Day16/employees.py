class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Keerthi", 15000)
employee2 = Employee("Rahul", 25000)

employee1.display()
print()
employee2.display()