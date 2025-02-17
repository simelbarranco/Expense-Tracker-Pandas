# Separate file to write all of the functions related to getting information from the user.
from datetime import datetime

date_format = "$d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

# We may be asking for the dates for different reasons. 
def get_date(prompt, allow_default=False): # User can just hit enter and by default it will select the current date.
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format) # Takes the date and applies this format.
    
    try:
        valid_date  = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default) # Recursive case running until we get a valid date.

# Input for the amount, validating its not 0 or negative.
def get_amount():
    try:
        amount = float(input("Enter the amount: ")) # Converting amount to float in case we
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-sezo value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount() # Recursive case running until we get a valid amount.

def get_category():
    category = input("Enter the category ('I' for Income, 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income, 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")