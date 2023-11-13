# Name : Taluba Aron Hopson
# Date : 31st August 2023
'''Designing and developing a program to calculate the Body Mass Index (BMI) for
the user. The user entering the input and getting the required results in output'''

# DEFINING THE CONSTANTS

BMI_LOWER_LIMIT_VALUE = 18.5
BMI_UPPER_LIMIT_VALUE = 24.5
BMI_EXTREME_LOWS_VALUE = 18.4
BMI_EXTREME_HIGHS_VALUE = 24.6


def main():  # Defining function for introduction and which BMI formula to use
    print(input("What is your name? : "))
    print("Welcome to the BMI Calculator")

    # Asking if user would like to use Metric or Imperial units
    print("Enter 1 calculate BMI in Imperial Units")
    print("Enter 2 calculate BMI in Matrics Units")

    option = input("Enter the Number : ")

    if (option == "1"):
        return bmi_imperial()
    elif (option == "2"):
        return bmi_metric()
    else:
        print("Wrong input")


def bmi_imperial():  # Defining Function for calculating BMI in an Imperail Units
    heightIN = float(input('Input your height in Inches (in): '))
    weightLB = float(input('Input your weight in Pounds (lb): '))
    BMI = round(((weightLB/(heightIN*heightIN))*703), 2)

    if BMI >= BMI_EXTREME_HIGHS_VALUE and BMI <= BMI_LOWER_LIMIT_VALUE:
        print('Your BMI is', BMI, 'the lower end indicate a healthy body')

    elif BMI >= BMI_LOWER_LIMIT_VALUE and BMI <= BMI_UPPER_LIMIT_VALUE:
        print('Your BMI is', BMI, 'indicate healthy conditions')

    elif BMI >= BMI_UPPER_LIMIT_VALUE and BMI <= BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI,
              'Indicate clinical issues, require medical attention.')

    elif BMI > BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI, 'and unhealthy body!')

    elif BMI < BMI_EXTREME_LOWS_VALUE:
        print('Your BMI is', BMI, 'and extreme lows')


def bmi_metric():  # Defining Function for calculating BMI in an Metric Units
    heightM = float(input('Input your height in Metre (M): '))
    weightKG = float(input('Input your weight in Kilogram (KG): '))
    BMI = round(((weightKG/(heightM*heightM))), 2)

    if BMI >= BMI_EXTREME_HIGHS_VALUE and BMI <= BMI_LOWER_LIMIT_VALUE:
        print('Your BMI is', BMI, 'the lower end indicate a healthy body')

    elif BMI >= BMI_LOWER_LIMIT_VALUE and BMI <= BMI_UPPER_LIMIT_VALUE:
        print('Your BMI is', BMI, 'indicate healthy conditions')

    elif BMI >= BMI_UPPER_LIMIT_VALUE and BMI <= BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI,
              'Indicate clinical issues, require medical attention.')

    elif BMI > BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI, 'and unhealthy body!')

    elif BMI < BMI_EXTREME_LOWS_VALUE:
        print('Your BMI is', BMI, 'and extreme lows')


if __name__ == "__main__":
    main()
