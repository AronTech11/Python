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
            print("\nReport:")
            for i, op in enumerate(operations):
                print(f"{op}: Attempts - {successful_responses[i][0]}, Correct - {successful_responses[i][1]}")
            continue
        elif choice == '6':
            report_requested = False
            for i, op in successful_responses:
                if i[0] > 0:
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
            user_input = input(f"What is {num1} {'+' if operation_choice == 1 else '-' if operation_choice == 2 else '*' if operation_choice == 3 else '/'} {num2}? ")
            if user_input.isdigit():
                user_answer = int(user_input)
                if user_answer == result:
                    print(random.choice(["Excellent!", "Very Good!", "Well Done!", "Awesome!", "Good Job!", "Correct!"]))
                    successful_responses[operation_choice][0] += 1
                    successful_responses[operation_choice][1] += 1
                    break
                else:
                    print(random.choice(["Try Again.", "OOPS.", "Not Quite.", "Look at it Again.", "Sorry."]))
                    tries += 1
                    if tries == 2:
                        print(f"The correct answer is {result}.")
            else:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
