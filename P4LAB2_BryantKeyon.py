# Keyon Bryant
# 4/5/24
# P4LAB2
# Description: Output range with increment

def print_increment_sequence(num1, num2):
    if num2 < num1:
        print("Second integer can't be less than the first.")
    else:
        for i in range(num1, num2 + 1, 5):
            print(i, end=" ")

# Taking input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Printing the sequence
print_increment_sequence(num1, num2)
