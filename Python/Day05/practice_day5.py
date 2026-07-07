name = input("Enter your name: ")
no_accounts = int(input("Enter the number of bank accounts you have: "))

for i in range(no_accounts):
    balance = float(input(f"Enter the balance for Account {i + 1}: "))
    total_balance += balance

avg_balance = total_balance / no_accounts

if avg_balance >= 100000:
    print("Premium Customer")
elif avg_balance >= 50000:
    print("Gold Customer")
    category = "Gold Customer"
elif avg_balance >= 10000:
    print("Silver Customer")
    category = "Silver Customer"
else:
    print("Basic Customer")
    category = "Basic Customer"

high_balance_account = 0

if balance > 50000:
    high_balance_account += 1

print(f"Customer: {name}")
print(f"Total Balance: {total_balance}")
print(f"Average Balance: {avg_balance}")
print(f"Customer Category: {category}")
print(f"Accounts above 50000: {high_balance_account}")
