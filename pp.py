# # import random

# # def get_user_name():
# #     name = input("Please enter your name: ")
# #     print(f"Hello, {name}! Welcome to the Math Practice Program.")

# # def display_menu():
# #     print("\nMenu:")
# #     print("1 – Addition")
# #     print("2 – Subtraction")
# #     print("3 – Multiplication")
# #     print("4 – Division")
# #     print("5 – Present a Report")
# #     print("6 – Exit")
# #     choice = input("Please choose an option (1-6): ")
# #     return choice

# # def perform_operation(operation_choice, num1, num2):
# #     if operation_choice == 1:
# #         return num1 + num2
# #     elif operation_choice == 2:
# #         return num1 - num2
# #     elif operation_choice == 3:
# #         return num1 * num2
# #     elif operation_choice == 4:
# #         return num1 / num2 if num2 != 0 else None

# # def get_number_digits():
# #     num_choice = input("Choose number digits (1 for single, 2 for double, 3 for triple): ")
# #     num_digits = int(num_choice)
# #     return num_digits

# # def generate_random_numbers(num_digits):
# #     num1 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
# #     num2 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
# #     return num1, num2

# # def main():
# #     get_user_name()
    
# #     operations = ["Addition", "Subtraction", "Multiplication", "Division"]
# #     successful_responses = [[0, 0], [0, 0], [0, 0], [0, 0]]
    
# #     while True:
# #         choice = display_menu()
        
# #         if choice == '5':
# #             print_report(operations, successful_responses)
# #         elif choice == '6':
# #             if not report_requested(successful_responses):
# #                 user_input = input("No report will be maintained. Do you still want to exit? (yes/no): ")
# #                 if user_input.lower() == 'yes':
# #                     print("Thank you for using the Math Practice Program. Goodbye!")
# #                     break
# #                 else:
# #                     continue
        
# #         num_digits = get_number_digits()
# #         num1, num2 = generate_random_numbers(num_digits)
        
# #         operation_choice = int(choice)
# #         result = perform_operation(operation_choice, num1, num2)
        
# #         tries = 0
# #         while tries < 2:
# #             user_input = input(f"What is {num1} {get_operator(operation_choice)} {num2}? ")
# #             if is_valid_input(user_input):
# #                 user_answer = int(user_input)
# #                 if user_answer == result:
# #                     print_positive_feedback()
# #                     successful_responses[operation_choice - 1][0] += 1
# #                     successful_responses[operation_choice - 1][1] += 1
# #                     break
# #                 else:
# #                     print_supportive_feedback(tries, result)
# #                     tries += 1
# #             else:
# #                 print("Invalid input. Please enter a number.")

# # def report_requested(successful_responses):
# #     for op in successful_responses:
# #         if op[0] > 0:
# #             return True
# #     return False

# # def get_operator(operation_choice):
# #     operators = ["+", "-", "*", "/"]
# #     return operators[operation_choice - 1]

# # def is_valid_input(user_input):
# #     return user_input.isdigit()

# # def print_positive_feedback():
# #     positive_feedback = ["Excellent!", "Very Good!", "Well Done!", "Awesome!", "Good Job!", "Correct!"]
# #     print(random.choice(positive_feedback))

# # def print_supportive_feedback(tries, result):
# #     if tries == 1:
# #         print("Try Again.")
# #     elif tries == 2:
# #         print(f"The correct answer is {result}.")

# # def print_report(operations, successful_responses):
# #     print("\nReport:")
# #     for i, op in enumerate(operations):
# #         attempts, correct = successful_responses[i]
# #         print(f"{op}: Attempts - {attempts}, Correct - {correct}")

# # if __name__ == "__main__":
# #     main()


# import random

# # Initialize variables to keep track of the user's performance
# attempts = [[0, 0, 0] for _ in range(4)]  # [operation_choice, total_attempts, correct_attempts]

# # Positive and supportive reinforcers
# positive_reinforcers = ["Excellent", "Very Good", "Well Done", "Awesome", "Good Job", "Correct"]
# supportive_reinforcers = ["Try Again", "OOPS", "Not Quite", "Look at it Again", "Sorry"]


# def display_menu():
#     while True:
#         print("\nMenu:")
#         print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Present a Report\n6 - Exit")
#         choice = input("Enter your choice (1/2/3/4/5/6): ")
#         if choice.isdigit() and 1 <= int(choice) <= 6:
#             return int(choice)
#         else:
#             print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")

# def generate_number(num_type):
#     if num_type == "single":
#         return random.randint(1, 9)
#     elif num_type == "double":
#         return random.randint(10, 99)
#     elif num_type == "triple":
#         return random.randint(100, 999)

# def create_question(num1, num2, operation_choice):
#     operations = {1: '+', 2: '-', 3: '*', 4: '/'}
#     return f"{num1} {operations[operation_choice]} {num2}"

# def check_answer(num1, num2, user_answer, operation_choice):
#     correct_answer = get_correct_answer(num1, num2, operation_choice)
#     return user_answer == correct_answer

# def get_correct_answer(num1, num2, operation_choice):
#     if operation_choice == 1:
#         return str(num1 + num2)
#     elif operation_choice == 2:
#         return str(num1 - num2)
#     elif operation_choice == 3:
#         return str(num1 * num2)
#     elif operation_choice == 4:
#         return str(round(num1 / num2, 2))

# def practice_operation(operation_choice, num_type, num_attempts):
#     while num_attempts > 0:
#         num1 = generate_number(num_type)
#         num2 = generate_number(num_type)
#         question = create_question(num1, num2, operation_choice)
#         user_answer = input(f"What is {question}? ")

#         if check_answer(num1, num2, user_answer, operation_choice):
#             print(random.choice(positive_reinforcers))
#             attempts[operation_choice - 1][2] += 1
#         else:
#             print(random.choice(supportive_reinforcers))
#             attempts[operation_choice - 1][1] += 1
#             if attempts[operation_choice - 1][1] == 2:
#                 print(f"Sorry, the correct answer is {get_correct_answer(num1, num2, operation_choice)}")
#         attempts[operation_choice - 1][0] += 1
#         num_attempts -= 1

# def present_report():
#     print("\nReport of Your Performance:")
#     operations = ["Addition", "Subtraction", "Multiplication", "Division"]
#     for i, operation in enumerate(operations):
#         total_attempts, correct_attempts = attempts[i][1], attempts[i][2]
#         if total_attempts > 0:
#             success_rate = (correct_attempts / total_attempts) * 100
#             print(f"{operation}: Attempted {total_attempts} times, Correct {correct_attempts} times, Success Rate: {success_rate:.2f}%")

# def main():
#     user_name = input("Enter your name: ")
#     print(f"Hello, {user_name}! Welcome to the Math Practice Program.")

#     while True:
#         choice = display_menu()
#         if choice == 6:
#             if not any(sum(attempts[i]) for i in range(4)):
#                 print("No records will be maintained since no activities have been performed.")
#                 exit_choice = input("Would you still like to exit? (yes/no): ").lower()
#                 if exit_choice != "yes":
#                     continue
#             print("Thank you. Goodbye!")
#             break
#         elif choice == 5:
#             present_report()
#         else:
#             operation_choice = choice
#             num_type = input("Choose the number type (single, double, triple): ").lower()
#             if num_type not in ["single", "double", "triple"]:
#                 print("Invalid number type. Please choose 'single', 'double', or 'triple'.")
#                 continue
#             num_attempts = int(input("How many times would you like to practice this operation? "))
#             practice_operation(operation_choice, num_type, num_attempts)



# if __name__ == "__main__":
#     main()


import random

# Function to get user's name and greet them
def get_user_name():
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Welcome to the Math Practice Program.")

# Function to display the menu and get the user's choice
def display_menu():
    print("\nMenu:")
    print("1 – Addition")
    print("2 – Subtraction")
    print("3 – Multiplication")
    print("4 – Division")
    print("5 – Present a Report")
    print("6 – Exit")
    choice = input("Please choose an option (1-6): ")
    return choice

# Function to perform math operation with random numbers
def perform_operation(operation, num1, num2):
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        if num1 < num2:
            num1, num2 = num2, num1  # Ensure num1 is greater than or equal to num2
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 == 0:
            return None  # Avoid division by zero
        return num1 / num2

# Function to present a report of the user's performance
def print_report(operations, successful_responses):
    print("\nReport:")
    for i, op in enumerate(operations):
        attempts, correct = successful_responses[i]
        print(f"{op}: Attempts - {attempts}, Correct - {correct}")

# Main function
def main():
    get_user_name()

    operations = ["Addition", "Subtraction", "Multiplication", "Division"]
    successful_responses = [[0, 0], [0, 0], [0, 0], [0, 0]]

    while True:
        choice = display_menu()

        if choice == '1':
            operation_choice = 0
        elif choice == '2':
            operation_choice = 1
        elif choice == '3':
            operation_choice = 2
        elif choice == '4':
            operation_choice = 3
        elif choice == '5':
            print_report(operations, successful_responses)
            continue
        elif choice == '6':
            report_requested = False
            for op in successful_responses:
                if op[0] > 0:
                    report_requested = True
                    break
            if not report_requested:
                user_input = input("No report will be maintained. Do you still want to exit? (yes/no): ")
                if user_input.lower() == 'yes':
                    print("Thank you for using the Math Practice Program. Goodbye!")
                    break
                else:
                    continue

        num_choice = input("Choose number digits (1 for single, 2 for double, 3 for triple): ")
        num_digits = int(num_choice)

        num1 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        num2 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)

        result = perform_operation(operation_choice, num1, num2)

        tries = 0
        while tries < 2:
            user_input = input(f"What is {num1} {'+' if operation_choice == 0 else '-' if operation_choice == 1 else '*' if operation_choice == 2 else '/'} {num2}? ")
            if user_input.isdigit():
                user_answer = int(user_input)
                if user_answer == result:
                    positive_feedback = ["Excellent!", "Very Good!", "Well Done!", "Awesome!", "Good Job!", "Correct!"]
                    print(random.choice(positive_feedback))
                    successful_responses[operation_choice][0] += 1
                    successful_responses[operation_choice][1] += 1
                    break
                else:
                    supportive_feedback = ["Try Again.", "OOPS.", "Not Quite.", "Look at it Again.", "Sorry."]
                    print(random.choice(supportive_feedback))
                    tries += 1
                    if tries == 2:
                        print(f"The correct answer is {result}.")
            else:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
