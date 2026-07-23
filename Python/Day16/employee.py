class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


employee1 = Employee("Keerthi", 15000)

employee2 = Employee("Rahul", 25000)

print("emp 1 " , employee1.name, employee1.salary)
print("emp 1 ",employee2.name, employee2.salary)