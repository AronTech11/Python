# import random

# def greet_user():
#     user_name = input("Please enter your name: ")
#     print(f"Hello, {user_name}! This program helps you practice math operations.")
#     return user_name

# def display_menu():
#     print("Menu:")
#     print("1 – Addition")
#     print("2 – Subtraction")
#     print("3 – Multiplication")
#     print("4 – Division")
#     print("5 – Present a Report")
#     print("6 – Exit")

# def get_user_choice():
#     while True:
#         try:
#             choice = int(input("Please enter your choice (1-6): "))
#             if 1 <= choice <= 6:
#                 return choice
#             else:
#                 print("Invalid choice. Please select a number from 1 to 6.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def get_operation_choice():
#     print("Choose the type of numbers:")
#     print("1 – Single digits")
#     print("2 – Double digits")
#     print("3 – Triple digits")
    
#     while True:
#         try:
#             choice = int(input("Please select the type of numbers (1-3): "))
#             if 1 <= choice <= 3:
#                 return choice
#             else:
#                 print("Invalid choice. Please select a number from 1 to 3.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def practice_math_operation(operator, operand_choice, num_of_practices):
#     successful_responses = 0
#     for _ in range(num_of_practices):
#         num1, num2 = generate_numbers(operand_choice)
#         result = calculate_result(num1, num2, operator)
        
#         user_answer = get_user_answer(num1, num2, operator)
        
#         if user_answer == result:
#             print(random.choice(["Excellent", "Very Good", "Well Done", "Awesome", "Good Job", "Correct"]))
#             successful_responses += 1
#         else:
#             print(random.choice(["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]))
#             print(f"The correct answer is: {result}")

#     return successful_responses

# def generate_numbers(operand_choice):
#     if operand_choice == 1:
#         return random.randint(1, 9), random.randint(1, 9)
#     elif operand_choice == 2:
#         return random.randint(10, 99), random.randint(10, 99)
#     else:
#         return random.randint(100, 999), random.randint(100, 999)

# def calculate_result(num1, num2, operator):
#     if operator == 1:
#         return num1 + num2
#     elif operator == 2:
#         return num1 - num2
#     elif operator == 3:
#         return num1 * num2
#     elif operator == 4:
#         return num1 / num2

# def get_user_answer(num1, num2, operator):
#     while True:
#         try:
#             user_answer = float(input(f"What is {num1} {'+' if operator == 1 else '-' if operator == 2 else '*' if operator == 3 else '/'} {num2}? "))
#             return user_answer
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def main():
#     user_name = greet_user()
#     successful_responses = []
#     operation_choices = ["Addition", "Subtraction", "Multiplication", "Division"]

#     while True:
#         display_menu()
#         choice = get_user_choice()

#         if choice == 6:
#             print("Thank you for using this program.")
#             break
#         elif choice == 5:
#             print(f"Report for {user_name}:")
#             for i, operation in enumerate(operation_choices, start=1):
#                 print(f"{i}. {operation} - Attempts: {len(successful_responses[i-1])}, Successful: {successful_responses[i-1]}")
#         else:
#             operand_choice = get_operation_choice()
#             num_of_practices = int(input("How many times would you like to practice this operation? "))

#             successful = practice_math_operation(choice, operand_choice, num_of_practices)
#             successful_responses.append(successful)

# if __name__ == "__main__":
#     main()


import random

def greet_user():
    while True:
        user_name = input("Please enter your name: ")
        if user_name.strip():  # Check if the name is not empty or just whitespace
            print(f"Hello, {user_name}! This program helps you practice math operations.")
            return user_name
        else:
            print("Invalid input. Please enter a valid name.")


def display_menu():
    print("Menu:")
    print("1 – Addition")
    print("2 – Subtraction")
    print("3 – Multiplication")
    print("4 – Division")
    print("5 – Present a Report")
    print("6 – Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Please enter your choice (1/2/3/4/5/6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please select a number from 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation_choice():
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
    successful_responses = 0
    for _ in range(num_of_practices):
        num1, num2 = generate_numbers(operand_choice)
        if operator == 2 and num1 < num2:
            num1, num2 = num2, num1  # Swap num1 and num2 for subtraction
        result = calculate_result(num1, num2, operator)
        
        user_answer = get_user_answer(num1, num2, operator)
        
        if operator == 4:
            # For division, format the result to show up to 2 decimal places
            result_str = f"{result:.2f}"
            user_answer_str = f"{user_answer:.2f}"
            if user_answer_str == result_str:
                print(random.choice(["Excellent", "Very Good", "Well Done", "Awesome", "Good Job", "Correct"]))
                successful_responses += 1
            else:
                print(random.choice(["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]))
                print(f"The correct answer is: {result_str}")
        else:
            if user_answer == result:
                print(random.choice(["Excellent", "Very Good", "Well Done", "Awesome", "Good Job", "Correct"]))
                successful_responses += 1
            else:
                print(random.choice(["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]))
                print(f"The correct answer is: {result}")

    return successful_responses

def generate_numbers(operand_choice):
    if operand_choice == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif operand_choice == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

def calculate_result(num1, num2, operator):
    if operator == 1:
        return num1 + num2
    elif operator == 2:
        return num1 - num2
    elif operator == 3:
        return num1 * num2
    elif operator == 4:
        return num1 / num2

def get_user_answer(num1, num2, operator):
    while True:
        try:
            user_answer = float(input(f"What is {num1} {'+' if operator == 1 else '-' if operator == 2 else '*' if operator == 3 else '/'} {num2}? "))
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    user_name = greet_user()
    successful_responses = [[], [], [], []]
    operation_choices = ["Addition", "Subtraction", "Multiplication", "Division"]

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 6:
            print("Thank you for using this program.")
            break
        elif choice == 5:
            print(f"Report for {user_name}:")
            for i, operation in enumerate(operation_choices, start=1):
                print(f"{i}. {operation} - Attempts: {sum(successful_responses[i-1])}, Successful: {successful_responses[i-1]}")
        else:
            operand_choice = get_operation_choice()
            num_of_practices = int(input("How many times would you like to practice this operation? "))

            successful = practice_math_operation(choice, operand_choice, num_of_practices)
            successful_responses[choice - 1].append(successful)

if __name__ == "__main__":
    main()

