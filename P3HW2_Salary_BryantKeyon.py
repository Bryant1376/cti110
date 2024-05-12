# Keyon Bryant
# 3/23/24
# P3HW2
# Description: Salary

# Ask the user to enter the name of the employee
employee_name = input("Enter employee's name: ")

# Ask the user to enter the number of hours the employee worked this week
hours_worked = float(input("Enter number of hours worked: "))

# Ask the user to enter the employee's pay rate
pay_rate = float(input("Enter employee's pay rate: "))

# Evaluate if the employee has worked overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate the amount owed to the employee for overtime hours
overtime_pay = 0
if overtime_hours > 0:
    overtime_pay = overtime_hours * (pay_rate * 1.5)

# Calculate the amount the employee should be paid for regular hours worked
regular_pay = regular_hours * pay_rate

# Calculate the gross pay (total amount that should be paid to the employee)
gross_pay = regular_pay + overtime_pay

# Display the employee's name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours, and gross pay
print("--------------------------------------")
print("Employee name:", employee_name)
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f'{hours_worked:<13.1f}  {pay_rate:<10.1f} {overtime_hours:<10.1f} {overtime_pay:<15.2f} {regular_pay:<13.2f} {gross_pay:<10.2f}')
