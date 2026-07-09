
def calculate_bonus(salary,percentage):
    bonus = salary * (percentage / 100)
    return bonus

name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
print("\nName:", name)
print("\nSalary:", salary)   
print("\nBonus:", calculate_bonus(salary, 10))


def calculate_total_salary(salary, bonus):
    total_salary = salary + bonus
    return total_salary
print("\nTotal Salary:", calculate_total_salary(salary, calculate_bonus(salary, 10)))
