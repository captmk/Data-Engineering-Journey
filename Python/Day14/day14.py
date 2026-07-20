print ("\n..... Safe Calculator .....")
input_1 = int(input("\nEnter the first number :"))
input_2 = int(input("\nEnter the second number :"))
print("\nAddition \nSubtraction \nMultiplication \nDivision")
operation = input("Choose the operation :")
if operation is "Addition":
    result=input_1 + input_2
    print("\n Result is :" result )
elif operation is "Subtraction":
    result=input_1 - input_2
    print(f"\n Result is :"result)
elif operation is "Multiplication":
    result=input_1 * input_2
    print(f"\n Result is :"result)
elif operation is "Division":
    result=input_1 / input_2
    print(f"\n Result is :"result)

try :
    with open("employees.txt","r") as file:
        print(read())
except FileNotFoundError
    print("file not found.")

finally:
    print("Program Finished.")

else 


