# Name : Taluba Aron Hopson
# Date :
'''Designing and developing a program to calculate the Body Mass Index (BMI) for
the user. The user entering the input and getting the required results in output'''

# DEFINING THE CONSTANTS

BMI_LOWER_LIMIT_VALUE = 18.5
BMI_UPPER_LIMIT_VALUE = 24.5
BMI_EXTREME_LOWS_VALUE = 18.4
BMI_EXTREME_HIGHS_VALUE = 24.6


'''Calculating the BMI in a metric units'''


def introduction_page():  # Defining function for introduction and which BMI formula to use
    print(input("What is your name? : "))
    print("Welcome to the BMI Calculator")

    # Asking if user would like to use Metric or Imperial units
    print("Enter 1 calculate BMI in Matrics Units")
    print("Enter 2 calculate BMI in Imperial Units")

    option = input("Enter the Number. : ")

    if (option == "1"):
        print("Welcome to BMI Calculator!")
        return bmi_imperial()
    elif (option == "2"):
        print("Welcome to BMI Calculator!")
        return bmi_metric()

    else:
        print("Wrong input")


def bmi_imperial():  # Defining Function for calculating BMI in an Imperail Units
    heightIN = float(input('Input your height in Inches (in): '))
    weightLB = float(input('Input your weight in Pounds (lb): '))
    BMI_IMPERIAL = round(((weightLB/(heightIN*heightIN))*703), 2)

    if BMI_IMPERIAL >= BMI_EXTREME_LOWS_VALUE and BMI_IMPERIAL <= BMI_LOWER_LIMIT_VALUE:
        print('Your BMI is', BMI_IMPERIAL, 'healthy body!')

    elif BMI_IMPERIAL >= BMI_UPPER_LIMIT_VALUE and BMI_IMPERIAL <= BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI_IMPERIAL, 'unhealthy body')

    elif BMI_IMPERIAL > BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI_IMPERIAL,
              'IndicatE clinical issues, require medical attention.')

    elif BMI_IMPERIAL < BMI_EXTREME_LOWS_VALUE:
        print('Your BMI is', BMI_IMPERIAL, 'and extreme lows!')


def bmi_metric():  # Defining Function for calculating BMI in an Metric Units
    heightM = float(input('Input your height in Metre (M): '))
    weightKG = float(input('Input your weight in Kg (KG): '))
    BMI_METRIC = round(((weightKG/(heightM*heightM))), 2)
    print(BMI_METRIC, "BMI VALE")

    if BMI_METRIC >= BMI_EXTREME_LOWS_VALUE and BMI_METRIC <= BMI_LOWER_LIMIT_VALUE:
        print('Your BMI is', BMI_METRIC, 'healthy body!')

    elif BMI_METRIC >= BMI_UPPER_LIMIT_VALUE and BMI_METRIC <= BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI_METRIC, 'unhealthy body')

    elif BMI_METRIC > BMI_EXTREME_HIGHS_VALUE:
        print('Your BMI is', BMI_METRIC,
              'Indicate clinical issues, require medical attention.')

    elif BMI_METRIC < BMI_EXTREME_LOWS_VALUE:
        print('Your BMI is', BMI_METRIC, 'and extreme lows!')


introduction_page()
