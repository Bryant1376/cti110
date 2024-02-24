# Keyon Bryant
# 2/23/24
# P1HW1
# Description: Basic output with variables

#Use the input function to get an integer from the user. Assign the integer to a variable
#Print the integer, the square of the integer, and the cube of the integer, each on a separate line
#Use the input function to get another integer from the user. Assign it to a variable
#Print both integers separated by a plus sign and then the sum of the integers
#Print both integers separated by a multiplication sign and then the product of the integers
#Do NOT hardcode the integers. The values should be able to change each time the program runs.

# Get an integer from the user and assign it to a variable
num1 = int(input("Enter an integer: "))

# Print the integer, the square, and the cube of the integer
print(f"The integer is: {num1}")
print(f"The square of the integer is: {num1 ** 2}")
print(f"The cube of the integer is: {num1 ** 3}")

# Get another integer from the user and assign it to a variable
num2 = int(input("Enter another integer: "))

# Print the sum and product of the two integers
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * {num2} = {num1 * num2}")
