data_engineering = {"Python","SQL", "Azure", "Python","Git","SQL","Docker"}
print(data_engineering)

data_engineering.add("Spark")
print(data_engineering)

data_engineering.remove("Git")
print(data_engineering)

total_unique_skills = len(data_engineering)
print(f"\nTotal Unique Skills: {total_unique_skills}")

new_skill = input("Enter a new skill to add: ")
if new_skill in data_engineering:
    print(f"{new_skill} is already in the set.")
else:
    data_engineering.add(new_skill)

print("\nUpdated Skills Set:")
print(data_engineering)
