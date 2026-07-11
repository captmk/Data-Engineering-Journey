print("Student Marks Manager")
marks=[]
subjects=int(input("Enter number of subjects: "))
for i in range(subjects):
    marks.append(int(input(f"Enter marks of student {i+1}: ")))
for i in range(subjects):
    print(f"\nMarks of student {i+1}: {marks[i]}")

#step 5
total_marks = sum(marks)
average_marks = total_marks / subjects
print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average_marks}\n")
 
#step 6
highest_marks = max(marks)
lowest_marks = min(marks)
print(f"\nHighest marks: {highest_marks}")
print(f"Lowest marks: {lowest_marks}\n")

#Bonus Challenge 
marks.append(int(input("Enter marks of new student: ")))
print(f"\nUpdated Marks List: {marks}")

marks.remove = lowest_marks

print(f"\nUpdated Marks List after removing lowest marks: {marks}")