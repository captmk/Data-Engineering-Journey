print("Employee Data Validator")
employee_id = input("Enter Employee ID: ").isdigit()
employee_name = input("Enter Employee Name: ").isalpha()
employee_department = input("Enter Employee Department: ")
email = input("Enter Employee Email: ").endswith(".com")
skills = input("Enter Employee Skills (comma-separated): ").split(",")
print("\nEmployee Data Validation Results:")
print(f"Employee ID: {employee_id}")
print(f"Employee Name: {employee_name}")
print(f"Employee Department: {employee_department}")
print(f"Employee Email: {email}")
print(f"Employee Skills: {' | '.join(skills)}")

employee_code = input("Enter Employee Code: ").startswith("EMP")
if employee_code:

    print(f"Employee Code is Valid")  
else:   
    print("Invalid Employee Code")