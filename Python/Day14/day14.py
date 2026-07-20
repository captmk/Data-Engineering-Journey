print("\n===== Safe Calculator =====")

try:
    # Get input from the user
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))

    # Display available operations
    print("\nChoose an Operation:")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

    operation = input("Enter operation: ").lower()

    # Perform the selected operation
    if operation == "addition":
        result = number_1 + number_2
        print("Result:", result)

    elif operation == "subtraction":
        result = number_1 - number_2
        print("Result:", result)

    elif operation == "multiplication":
        result = number_1 * number_2
        print("Result:", result)

    elif operation == "division":
        result = number_1 / number_2
        print("Result:", result)

    else:
        print("Invalid operation selected.")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Calculation completed successfully.")

finally:
    print("Thank you for using Safe Calculator.")