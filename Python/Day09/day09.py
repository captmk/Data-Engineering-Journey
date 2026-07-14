print("Employee ID Card")
employee = (
    101,
    "Keerthi",
    "Oitro",
    "Engineering"
)
print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Employee Company:", employee[2])
print("Employee Department:", employee[3])

#Challenge 2
for i in range(len(employee)):
    print(f"Employee Detail {i+1}: {employee[i]}")

#Challenge 3
print(f"\nTotal Fields: {len(employee)}")

#Bonus Challenge 
employee[1] = "Keerthi Prasad"