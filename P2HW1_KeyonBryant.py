# Keyon Bryant
# 3/9/24
# P2HW1
#Description: Travel Expenses

def calculate_travel_expenses():
    # Input budget and travel destination
    budget = float(input("Enter Budget: "))
    destination = input("Enter your travel destination: ")

    # Input estimated expenses for gas, accommodation, and food
    gas_expense = float(input("How much do you think you will spend on gas? "))
    accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food_expense = float(input("Last, how much do you need for food? "))

    # Calculate the remaining balance
    remaining_balance = budget - (gas_expense + accommodation_expense + food_expense)
    
    # Display the summary of travel expenses
    print("\n------------Travel Expenses-------------")
    print(f"Location: {destination}")
    print(f"Initial Budget: ${budget:.2f}")
    print(f"Fuel: ${gas_expense:.2f}")
    print(f"Accommodation: ${accommodation_expense:.2f}")
    print(f"Food: ${food_expense:.2f}")
    print("----------------------------------------")
    print(f"Remaining Balance: ${remaining_balance:.2f}")

# Calculate and display travel expenses
calculate_travel_expenses()
