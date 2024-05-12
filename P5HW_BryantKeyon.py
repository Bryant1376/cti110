# Keyon Bryant
# 4/28/24
# P5HW2
#Description: Math Quiz

import random

def main_menu():
    print("Welcome to Math Quiz")
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def add_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"{num1} + {num2}")
    guess = int(input("Enter answer: "))
    num_of_guesses = 1
    while guess != correct_answer:
        if guess < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")
        guess = int(input("Try again: "))
        num_of_guesses += 1
    print(f"Congratulations!!!! Your answer is correct. Number of guesses: {num_of_guesses}")

def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    print(f"{num1} - {num2}")
    guess = int(input("Enter answer: "))
    num_of_guesses = 1
    while guess != correct_answer:
        if guess < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")
        guess = int(input("Try again: "))
        num_of_guesses += 1
    print(f"Congratulations!!!! Your answer is correct. Number of guesses: {num_of_guesses}")

def math_quiz():
    main_menu()
    choice = int(input("Please choose one of the menu options: "))
    while choice != 3:
        if choice == 1:
            add_random_numbers()
        elif choice == 2:
            subtract_random_numbers()
        else:
            print("Invalid choice. Please try again.")
        main_menu()
        choice = int(input("Please choose one of the menu options: "))
    print("Thank you for playing...")
    print("Bye!")

math_quiz()
