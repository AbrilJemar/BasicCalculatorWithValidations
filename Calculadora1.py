def check_user_input(x):
    try:
        # Convert it into integer
        val = int(x)
    except ValueError:
        try:
            # Convert it into float
            val = float(x)
        except ValueError:
            val = x

    return (val)


while True:
    print("""
    Tell me, what do you want to do?
    
    1) Add the two numbers
    2) Subtract the two numbers
    3) Multiply the two numbers
    4) Divide the two numbers
    5) Turn off the calculator

    """)
    option = input("Choose an option: ")    
    option = check_user_input(option)
    while(isinstance(option, str) or option not in [1,2,3,4,5]):
        option = input("Invalid option. Try again: ")
        option = check_user_input(option)
        
    match option:
        case 1:
            number_one = input("Enter first number: ")
            number_one = check_user_input(number_one)
            while(isinstance(number_one, str)):
                number_one = input("Invalid number. Try again: ")
                number_one = check_user_input(number_one)
    
            number_two = input("Enter second number: ")
            number_two = check_user_input(number_two)
            while(isinstance(number_two, str)):
                number_two = input("Invalid number. Try again: ")
                number_two = check_user_input(number_two)

            Operation_Sum = number_one + number_two
            print('The sum is: ' + str(Operation_Sum))
        
        case 2:
            number_one = input("Enter first number: ")
            number_one = check_user_input(number_one)
            while(isinstance(number_one, str)):
                number_one = input("Invalid number. Try again: ")
                number_one = check_user_input(number_one)
    
            number_two = input("Enter second number: ")
            number_two = check_user_input(number_two)
            while(isinstance(number_two, str) ):
                number_two = input("Invalid number. Try again: ")
                number_two = check_user_input(number_two)

            Operation_Subtra = number_one - number_two
            print('The subtraction is: ' + str(Operation_Sum))

        case 3:
            number_one = input("Enter first number: ")
            number_one = check_user_input(number_one)
            while(isinstance(number_one, str)):
                number_one = input("Invalid number. Try again: ")
                number_one = check_user_input(number_one)
    
            number_two = input("Enter second number: ")
            number_two = check_user_input(number_two)
            while(isinstance(number_two, str)):
                number_two = input("Invalid number. Try again: ")
                number_two = check_user_input(number_two)

            Operation_Multi = number_one * number_two
            print('The product is: ' + str(Operation_Sum))

        case 4:
            number_one = input("Enter first number: ")
            number_one = check_user_input(number_one)
            while(isinstance(number_one, str)):
                number_one = input("Invalid number. Try again: ")
                number_one = check_user_input(number_one)
    
            number_two = input("Enter second number: ")
            number_two = check_user_input(number_two)
            while(isinstance(number_two, str) or number_two == 0):
                number_two = input("Invalid number. Try again: ")
                number_two = check_user_input(number_two)

            Operation_Divide = number_one / number_two
            print('The division is: ' + str(Operation_Sum))

        case 5:
            break

print("OFF")
