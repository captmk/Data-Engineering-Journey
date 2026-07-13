print("Employee Record Manager")
employee_name = input("Enter employee name: ")
employee_age = int(input("Enter employee age: "))
employee_salary = float(input("Enter employee salary: "))
employee_department = input("Enter employee department: ")
employee_record = {
    "name": employee_name  ,
    "age": employee_age,
    "salary": employee_salary,
    "department": employee_department
}
print("\nEmployee Record:")
print(employee_record) 
#Challenge 2
print("Do you want to update the salary? (y/n): ")
update_salary = input().lower()
if update_salary == 'y':
    new_salary = float(input("Enter new salary: "))
    employee_record["salary"] = new_salary
    print("Salary updated successfully.")
    print("\nUpdated Employee Record:")
    print(employee_record)
else:
    print(employee_record)
#Challenge 3
employee_record["employee_experience"] = int(input("Enter employee experience (in years): "))   
if employee_record["employee_experience"] >= 5:
    print("Senior Employee.")
else:
    print("Junior Employee.")