# Name : Taluba Aron Hopson
# Student ID : 101747537
# Date : 15th September 2023

'''
 The program  is designed to provide a user-friendly math practice experience,
 focusing on two control structures: selection and repetition. Upon execution, 
 the program starts by asking the user's name and greets them, informing them of its purpose.
 It then presents a menu with three options: 1 for addition, 2 for subtraction, and 3 to exit the program.
 
If the user selects option 1, the program generates two random numbers,
asks the user for their sum, and checks if the user's answer is correct.
If it is correct, the program congratulates the user and waits for an Enter key press to continue.

If the user selects option 2, the program generates two random numbers,
asks the user for their difference, and checks if the user's answer is correct.
If it is correct, the program congratulates the user and waits for an Enter key press to continue.
If the answer is incorrect, it provides the correct answer.

If the user selects option 3, the program simply prints "Thank you" and exits.

To ensure the program's functionality, it imports the random module and 
utilizes a loop to keep presenting the menu until the user chooses to exit. 
Additionally, it provides meaningful user interactions and includes comments for clarity and documentation. 
The program offers an engaging and educational math practice experience while
demonstrating the use of control structures in Python.
 '''

import random
# Function to generate random numbers for addition and subtraction


def generate_random_number():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    return random_number1, random_number2

# Function to display the menu


def display_menu():
    print("Menu:")
    print("1 - Addition")
    print("2 - Substraction")
    print("3 - Exit")


# Function to check the user's answer for addition

def check_addition_answer(random_number1, random_number2):
    correct_answer = random_number1 + random_number2
    user_answer = int(
        input(f"What is {random_number1} + {random_number2} ? = "))
    if user_answer == correct_answer:
        print("Well done!")
    else:
        print(f"Sorry, The correct answer is {correct_answer}.")

# Function to check the user's answer for subtraction


def check_subtraction_answer(random_number1, random_number2):

    if (random_number1 == random_number2):
        print("“both numbers are the same and the difference is 0")
        return    # Return early if the numbers are the same

    if random_number2 > random_number1:
        # It performs a variable swap when second random is greater than first.
        random_number1, random_number2 = random_number2, random_number1

    correct_answer = random_number1 - random_number2
    user_answer = int(
        input(f"What is {random_number1} - {random_number2}? = "))
    if user_answer == correct_answer:
        print("Well done!")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")


# Main program
def main():
    # Get the user's name
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}! Welcome to the Math Practice Program.")

    while True:  # We use True here to create infinite loop

        # Display the menu and get user's choice
        display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # Addition
            random_number1, random_number2 = generate_random_number()
            check_addition_answer(random_number1, random_number2)
            input("Press Enter to continue...")

        elif choice == "2":
            # Substraction
            random_number1, random_number2 = generate_random_number()
            check_subtraction_answer(random_number1, random_number2)
            input("Press Enter to continue...")

        elif choice == "3":
            print(
                f"Thank you {user_name}, for using the Math Practice Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
