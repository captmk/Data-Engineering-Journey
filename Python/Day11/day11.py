print("Customer Data Cleaner")
customer_name = input("Enter the customer name: ")
company_name = input("Enter the company name: ")
email = input("Enter the email address: ")
invoice_number = input("Enter the invoice number: ")
print(f"Customer Name: {customer_name}")
print(f"Company Name: {company_name}")
print(f"Email Address: {email}")
print(f"Invoice Number: {invoice_number}")
invoice_number_cleaned = {invoice_number.replace("2025", "2026")}

print("\nCleaned Data:")
print(f"Customer Name: {customer_name.strip().title()} ")    
print(f"Company Name: {company_name.strip().upper()}")
print(f"Email Address: {email.strip().lower()}")
print(f"Invoice Number: {invoice_number_cleaned}")

