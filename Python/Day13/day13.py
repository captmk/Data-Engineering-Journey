print(f"\n.....Employee Records.....\n")
with open ("employees.txt", "r") as file:
    for line in file:
        print(line)


learning_log = input("\nWhat did you learn ?\n")
with open ("learning_log.txt","a") as file:
    file.write(learning_log + "\n")
