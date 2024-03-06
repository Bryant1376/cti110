# Keyon Bryant
# 3/3/24
# P2LAB1
#Description: Write a program with a car's gas mileage

# Get input values
mileage = float(input())
gas_cost = float(input())

# Calculate gas cost for 20 miles, 75 miles, and 500 miles
cost_20_miles = (20 / mileage) * gas_cost
cost_75_miles = (75 / mileage) * gas_cost
cost_500_miles = (500 / mileage) * gas_cost

# Print the results with two digits after the decimal point
print(f'{cost_20_miles:.2f} {cost_75_miles:.2f} {cost_500_miles:.2f}')
