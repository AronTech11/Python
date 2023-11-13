# Name : Taluba Aron Hopson
# Student ID : 101747537
# Date : 20th October 2023

'''This program is an interactive math practice program that extends a previous assignment.
It greets users, offers the opportunity to practice various math operations, and provides performance reports.
Users select from a menu of six choices, including addition, subtraction, multiplication, division,
viewing a performance report, and exiting. The program lets users customize their practice by choosing 
the difficulty level and the number of attempts. It generates random math problems, offers positive feedback 
for correct answers, and keeps track of performance data. If the response is incorrect, it provides supportive
feedback and reveals the correct answer after the second try. Users can request a performance report or choose to exit,
with the program ensuring a report is generated. It's well-documented and user-friendly, designed to improve math skills.'''

import random

# Function to greet the user and get their name
def greet_user():
    """
    Purpose: Greet the user, retrieve their name, and inform them about the program.
    
    Input: user input through the console.
    
    Output: The user's name (string).
    """
    while True:
        user_name = input("Please enter your name: ")
        if user_name.strip():  # Check if the name is not empty or just whitespace
            print(f"Hello, {user_name}! This program helps you practice math operations.")
            return user_name

# Function to display the program menu
def display_menu():
    """
    Purpose: Display the program menu with math operation choices.
    
    Input: None.
    
    Output: The menu is displayed on the screen.
    """
    print("Menu:")
    print("1 – Addition")
    print("2 – Subtraction")
    print("3 – Multiplication")
    print("4 – Division")
    print("5 – Present a Report")
    print("6 – Exit")

# Function to get the user's choice from the menu
def get_user_choice():
    """
    Purpose: Obtain the user's choice from the menu.

    This function interacts with the user to get their choice from a menu of options.
    Input: user input through the console.

    Returns:
        int: The user's choice (integer) within the range of 1 to 6 (inclusive).
    """
    while True:
        try:
            choice = int(input("Please enter your choice (1/2/3/4/5/6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please select a number from 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the user's choice for the type of numbers
def get_operation_choice():
    """
    Purpose: Allow the user to choose the type of numbers for practice (single, double, or triple digits).
    
    Input: user input through the console.
    
    Returns:
        int: User's choice of number type (1 for single digits, 2 for double digits, or 3 for triple digits).
    """
    print("Choose the type of numbers:")
    print("1 – Single digits")
    print("2 – Double digits")
    print("3 – Triple digits")
    
    while True:
        try:
            choice = int(input("Please select the type of numbers (1/2/3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please select a number from 1 to 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def practice_math_operation(operator, operand_choice, num_of_practices):
    """
    Allows the user to practice a math operation interactively and provides feedback.

    Arguments:
        operator (int): The type of math operation (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division).
        operand_choice (int): The type of numbers (1 for single digits, 2 for double digits, 3 for triple digits).
        num_of_practices (int): The number of practice exercises.

    Returns:
        int: The number of successful responses.
    """
    correct_responses = 0
    max_attempts = 2  # Maximum number of attempts allowed
    for _ in range(num_of_practices):
        num1, num2 = generate_random_numbers(operand_choice)
        if operator == 2 and num1 < num2:
            num1, num2 = num2, num1  # Swap num1 and num2 for subtraction
        result = calculate_result(num1, num2, operator)
        
        incorrect_attempts = 0  # Counter for incorrect attempts
        
        while incorrect_attempts < max_attempts:
            user_answer = get_user_answer(num1, num2, operator)
            
            if operator == 4:
                # For division, format the result to show up to 2 decimal places
                result_str = f"{result:.2f}"
                user_answer_str = f"{user_answer:.2f}"
                if user_answer_str == result_str:
                    print(random.choice(["Excellent", "Very Good", "Well Done", "Awesome", "Good Job", "Correct"]))
                    correct_responses += 1
                    break  # Break the inner while loop if the answer is correct
                else:
                    incorrect_attempts += 1
                    if incorrect_attempts == max_attempts:
                        print("Sorry, you have reached the maximum number of attempts.")
                        print(f"The correct answer is: {result_str}")
                    else:
                        print(random.choice(["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]))
            else:
                if user_answer == result:
                    print(random.choice(["Excellent", "Very Good", "Well Done", "Awesome", "Good Job", "Correct"]))
                    correct_responses += 1
                    break  # Break the inner while loop if the answer is correct
                else:
                    incorrect_attempts += 1
                    if incorrect_attempts == max_attempts:
                        print("Sorry, you have reached the maximum number of attempts.")
                        print(f"The correct answer is: {result}")
                    else:
                        print(random.choice(["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]))

    return correct_responses

# Function to generate random numbers based on the user's choice
def generate_random_numbers(operand_choice):
    """
    Generates random numbers based on the user's choice.

    Arguments:
        operand_choice (int): The type of numbers (1 for single digits, 2 for double digits, 3 for triple digits).

    Returns:
        tuple: A tuple of two random numbers.
    """
    if operand_choice == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif operand_choice == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

# Function to calculate the result of a math operation
def calculate_result(num1, num2, operator):
    """
    Calculates the result of a math operation.

    Arguments:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operator (int): The type of math operation (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division).

    Returns:
        float: The calculated result.
    """
    if operator == 1:
        return num1 + num2
    elif operator == 2:
        return num1 - num2
    elif operator == 3:
        return num1 * num2
    elif operator == 4:
        return num1 / num2

# Function to get the user's answer to a math question
def get_user_answer(num1, num2, operator):
    """
    Retrieves the user's answer to a math question.

    Arguments:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operator (int): The type of math operation (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division).

    Returns:
        float: The user's answer.
    """
    while True:
        try:
            user_answer = float(input(f"What is {num1} {'+' if operator == 1 else '-' if operator == 2 else '*' if operator == 3 else '/'} {num2}? "))
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a number.")

# The main program that orchestrates user interactions and calls the above functions
def main():
    user_name = greet_user()
    total_attempts = [0, 0, 0, 0]  # Initialize a list for total attempts
    correct_responses = [0, 0, 0, 0]  # Initialize a list for successful responses
    operation_choices = ["Addition", "Subtraction", "Multiplication", "Division"]

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 6:
            generate_report = input("Would you like to generate a performance report (yes/no)? ").strip().lower()
            if generate_report == 'yes':
                print(f"Report for {user_name}:")
                for i, operation in enumerate(operation_choices, start=1):
                    total_attempts_i = total_attempts[i-1]
                    correct_attempts = correct_responses[i-1]
                    incorrect_attempts = total_attempts_i - correct_attempts
                    print(f"{i}. {operation} - Total Attempts: {total_attempts_i}, Successful: {correct_attempts}, Error: {incorrect_attempts}")
            else:
                print("No record will be maintained.")
            print("Thank you for using this program.")
            break
        elif choice == 5:
            print(f"Report for {user_name}:")
            for i, operation in enumerate(operation_choices, start=1):
                total_attempts_i = total_attempts[i-1]
                correct_attempts = correct_responses[i-1]
                incorrect_attempts = total_attempts_i - correct_attempts
                print(f"{i}. {operation} - Total Attempts: {total_attempts_i}, Successful: {correct_attempts}, Error: {incorrect_attempts}")
        else:
            operand_choice = get_operation_choice()
            num_of_practices = int(input("How many times would you like to practice this operation? "))

            successful = practice_math_operation(choice, operand_choice, num_of_practices)
            total_attempts[choice - 1] += num_of_practices  # Increment total attempts
            correct_responses[choice - 1] += successful

if __name__ == "__main__":
    main()
