operands = ['+', '-', '*', '/', '//']
history = {}
b = 0
result = None


def print_messages(menu, history, result):
    if menu == 0:
        print("Thank you for using Calculator. ")
    elif menu == 2:
        if history == {} and result == None:
            print("No Operation performed uptill now")
        else:
            print("Previously Performed Operations :-")
    elif menu == 3:
        if history == {}:
            print("Nothing is available in History")
        else:
            print("History is cleared")
    elif menu == 1:
        print("Invalid command. Please enter the correct Command")


def other_error_messages():
    if NameError or ValueError is True:
        print("Invalid command. Please enter the correct one. ")
    if ZeroDivisionError is True:
        print("Can't be divided by zero")


def addition(first, second):
    return first+second


def subtraction(first, second):
    return first-second


def multiplication(first, second):
    return first*second


def division(first, second):
    return first/second


def divison_decimal(first, second):
    return first//second


def power(first, second):
    if second > 1:
        first_1 = first * first
        for _ in range(second-2):
            first_1 = first_1 * first
        return first_1

    elif second == 1:
        return first

    elif second == 0:
        return 0

    else:
        return None


def under_root(first, second):
    root = 1/second
    return first**root


def percentage(first, second):
    return first % second


def print_result(result):
    if result != None:
        print(f"Answer is: {result}")
    return result


def formulate_history(first, second, operand, result):
    if result != None:
        history[b] = [f"{first} {operand} {second} = {result}"]
        return history[b]


def print_history(history):
    if history != {}:
        print(history)
    else:
        pass


def clear_history(history):
    if history != {}:
        history.clear()
        return history
    else:
        pass


def main_menu():
    main = int(input(""" 
    ========================MAIN DISPLAY============================
    Press 1 for using Calculator operations : 
    Press 0 for exiting the Calculator :
    Press 2 for printing Previous Operations :
    Press 3 for deleting History :
    ================================================================
    """))
    return main


def operand_function():
    symbol = input('''Select the operand you want to implement :
        +  for Addition
        -  for Subtraction
        *  for Multiplication
        /  for Division
        // for Division in decimal
        ^  for Power
        ^^ for Root Finding
         ''')
    return symbol


def num_input(operand):
    if operand in operands:
        first_input = int(input("Please enter the first number: "))
        second_input = int(input("Please enter the other number: "))
    elif operand == '^':
        first_input = int(input("Please enter the number: "))
        second_input = int(input("Please enter the power: "))
    elif operand == '^^':
        first_input = int(input("Please enter the number: "))
        second_input = int(input("Please enter the root you want to find: "))
    elif operand == '%':
        first_input = int(input("Please enter the number: "))
        second_input = int(input("Please enter the percentage: "))
    else:
        first_input = None
        second_input = None
    return first_input, second_input


try:
    menu = main_menu()
    while menu != 0:
        if menu == 1:
            operand = operand_function()
            first, second = num_input(operand)
            if operand == '+':
                result = addition(first, second)
            elif operand == '-':
                result = subtraction(first, second)
            elif operand == '*':
                result = multiplication(first, second)
            elif operand == '/':
                result = division(first, second)
            elif operand == '//':
                result = divison_decimal(first, second)
            elif operand == '^':
                result = power(first, second)
            elif operand == '^^':
                result = under_root(first, second)
            elif operand == '%':
                result = percentage(first, second)
            else:
                print_messages(menu, history, result)
            print_result(result)
            formulate_history(first, second, operand, result)
            b += 1
        elif menu == 2:
            print_messages(menu, history, result)
            print_history(history)
        elif menu == 3:
            print_messages(menu, history, result)
            clear_history(history)
        menu = main_menu()
    if menu == 0:
        print_messages(menu, history, result)
except ValueError:
    other_error_messages()
except ZeroDivisionError:
    other_error_messages()
