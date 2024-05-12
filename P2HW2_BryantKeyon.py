# Keyon Bryant
# 3/9/24
# P2HW2
#Description: Write a program with a car's gas mileage


# Ask the user to enter grades for each module
grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Display the lowest grade, highest grade, sum of grades, and the average
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
