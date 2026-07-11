# Day 7
# Program: Student Marks Manager
# Author: Keerthi
# Purpose: Store student marks using lists and perform basic analysis.

print("===== Student Marks Manager =====")

marks = []

subjects = int(input("Enter the number of subjects: "))

for i in range(subjects):
    mark = int(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)

print("\nEntered Marks:")

for mark in marks:
    print(mark)

total_marks = sum(marks)
average_marks = total_marks / len(marks)

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

highest_mark = max(marks)
lowest_mark = min(marks)

print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")

# Bonus Challenge
new_mark = int(input("\nEnter one more mark: "))
marks.append(new_mark)

print(f"\nUpdated Marks List: {marks}")

lowest_mark = min(marks)
marks.remove(lowest_mark)

print(f"Final Marks List: {marks}")