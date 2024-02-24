# Keyon Bryant
# 2/23/24
# P1HW2
#Description: Calculates and displays travel expenses

# 1. Ask the user to enter their budget and store it in a variable.
# 2. Ask the user to enter the travel destination and store it in a variable.
# 3. Ask the user to enter the amount they will spend on gas and store it in a variable.
# 4. Ask the user to enter the amount they will spend on accommodation and store it in a variable.
# 5. Ask the user to enter the amount they will spend on food and store it in a variable.
# 6. Add the expenses (gas, accommodation, and food) to get the total expenses.
# 7. Subtract the total expenses from the budget to get the remaining budget.
# 8. Display the travel details, total expenses, and remaining budget.

# Get user input for budget
budget = float(input("Enter your budget: $"))

# Get user input for travel destination
destination = input("Enter your travel destination: ")

# Get user input for gas expenses
gas_expense = float(input("Enter the amount you will spend on gas: $"))

# Get user input for accommodation expenses
accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

# Get user input for food expenses
food_expense = float(input("Enter the amount you will spend on food: $"))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Display the results
print("\nTravel Details:")
print(f"Destination: {destination}")
print("\nExpenses:")
print(f"Gas: {gas_expense:.2f}")
print(f"Accommodation: {accommodation_expense:.2f}")
print(f"Food: ${food_expense:.2f}")
print(f"\nTotal Expenses: {total_expenses:.2f}")
print(f"Remaining Budget: {remaining_budget:.2f}")
