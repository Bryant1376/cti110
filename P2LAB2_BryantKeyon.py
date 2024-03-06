# Keyon Bryant
# 3/3/24
# P2LAB2
#Description: Rounding integer

# Get input values
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculate product and average
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Output as rounded integers and floating-point numbers
print(f'{product:.0f} {average:.0f}')
print(f'{product:.3f} {average:.3f}')
