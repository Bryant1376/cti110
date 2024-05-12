# Keyon Bryant
# 3/9/24
# P3HW1
# Description: Correct the program

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
grades= []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))
# determine lowest, highest , sum and average for grades
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)
print("\n------------Results-------------")
print("Lowest Grade:", format(lowest_grade, '.1f'))
print("Highest Grade:", format(highest_grade, '.1f'))
print("Sum of Grades:", sum_of_grades)
print("Average:", format(average_grade, '.2f'))
print("----------------------------------------")

# determine letter grade for average
if average_grade >= 90:
 print('Your grade is: A')
elif average_grade >= 80:
 print('Your grade is: B')
elif average_grade >= 70:
 print('Your grade is: C')
elif average_grade >= 60:
 print('Your grade is: D')
else:
 print('Your grade is: F')
