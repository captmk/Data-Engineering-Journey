name = input("Enter your name: ")
salary = int(input("Enter your current salary: "))
year_experience = int(input("Enter your years of experience: "))
permanant = input("Are you a permanant employee? (yes/no): ")

if salary >= 50000:
    print("Senoior Employee")
elif salary >= 25000:
    print("Mid-level Employee")
else:
    print("Junior Employee")

if year_experience >= 5:
    print("You are eligible for promotion")
else:
    print("You are not eligible for promotion")

if permanant == "yes" and year_experience >= 5:
    print("Bonus Approved")
else:
    print("Bonus Not Approved")