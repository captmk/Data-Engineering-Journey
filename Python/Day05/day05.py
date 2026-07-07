print("Student Marks Calculator")

name = input("Enter Student Name: ")
no_subjects = int(input("Enter the no of subjects: "))

total_marks = 0

for i in range(no_subjects):
    marks = int(input(f"Enter the marks for Subject {i + 1}: "))
    total_marks = total_marks + marks

average = total_marks / no_subjects

print("Total Marks:", total_marks)
print("Average Marks:", average)

if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 50:
    print("Grade C")
else:
    print("Fail")