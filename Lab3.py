
import math
'''Printing a natural number from 1 to 100'''


def natural_number():
    for natural_no in range(1, 101):
        print(natural_no)


'''Printing a even number from 1 to 100'''


def even_numbers():
    for even_no in range(2, 100, 2):
        print(even_no)


'''Printing a odd number from 1 to 100'''


def odd_numbers():
    for odd_no in range(1, 101, 2):
        print(odd_no)


'''Printing sequence of number using collatz conjecture'''


def collatz_conjecture(num):
    sequence = [num]
    while (num != 1):
        if ((num % 2) == 0):
            num = num // 2
        else:
            num = (num*3) + 1
        sequence.append(num)
    print("value", sequence)


'''Printing a odd number from 1 to 100'''


def Waves(n):
    for x in range(n):
        print("Sine wave =", x, "PI")
    for y in range(n):
        print("Cos wave =", 2*y+1, "PI/2")


def main():  # Defining main function
    # Asking if user
    print("Enter 1 Natural number")
    print("Enter 2 Even number")
    print("Enter 3 Odd number")
    print("Enter 4 Collatz")
    print("Enter 5 Waves")
    print("Enter 6 to exit")

    option = input("Enter the Number : ")

    if (option == "1"):
        return natural_number()
    elif (option == "2"):
        return even_numbers()
    elif (option == "3"):
        return odd_numbers()
    elif (option == "4"):
        num = int(input('Enter a number: '))
        return collatz_conjecture(num)
    elif (option == "5"):
        num = int(input('Enter a number: '))
        return Waves(num)

    elif (option == "6"):
        return exit()
    else:
        print("wrong input")


if __name__ == "__main__":
    main()
