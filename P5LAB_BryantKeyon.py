# Keyon Bryant
# 4/20/24
# P5LAB
#Description: Leap Year

#Create a loop for leap year
def days_in_feb(user_year):
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28

# Test the function
year = int(input("Enter a year: "))
days = days_in_feb(year)
print(f"{year} has {days} days in February.")
