# Menu Input Function-----------------------------------------------
try:
    menu = int(input(""" 
    ========================MAIN DISPLAY============================
    Press 1 for using Calculator operations : 
    Press 0 for exiting the Calculator :
    Press 2 for printing Previous Operations :
    Press 3 for deleting History :
    ================================================================
    """))
    history = {}
    b = 0
    while menu != 0:
        if menu == 1:
            # Operand Input Function---------------------------------------------
            operand = input('''Select the operand you want to implement :
        +  for Addition
        -  for Subtraction
        *  for Multiplication
        /  for Division
        // for Division in decimal
        ^  for Power
        ^^ for Root Finding
         ''')

            if operand == '+' or operand == '-' or operand == '*' or operand == '/' or operand == '//':
                first = int(input("Please enter the first number: "))
                second = int(input("Please enter the other number: "))
                if operand == '+':
                    result = first+second
                    history[b] = [first, "+", second, "=", result]
                    print(f"sum is  {result}")
                elif operand == '-':
                    result = first-second
                    history[b] = [first, "-", second, "=", result]
                    print(f"Difference is  {result}")
                elif operand == '*':
                    result = first*second
                    history[b] = [first, "x", second, "=", result]
                    print(f"Product is  {result}")
                elif operand == '/':
                    result = first/second
                    history[b] = [first, "/", second, "=", result]
                    print(f"Divison in Int is  {result}")
                elif operand == '//':
                    result = first//second
                    history[b] = [first, "//", second, "=", result]
                    print(f"Divison in points is  {result}")
            elif operand == '%':
                first = int(input("Please enter the first number: "))
                second = int(input("Please enter the Percentage : "))
                result = first % second
                history[b] = [first, "^", second, "=", result]
                print(float(f"% of {first} is  {result}"))
            elif operand == '^':
                first = int(input("Please enter the number: "))
                second = int(input("Please enter the power: "))
                if second > 1:
                    first_1 = first * first  # Power function Code
                    a = 0
                    while a != second-2:
                        first_1 = first_1 * first
                        a += 1
                        history[b] = [first, "^", second, "=", first_1]
                    print(f"Power of {first} is  {first_1}")
                elif second == 1:
                    history[b] = [first, "^", second, "=", first]
                    print(f"Power of {first} is {first}")
                elif second == 0:
                    history[b] = [first, "^", second, "=", 0]
                    print("Power of {first} is 0")
                else:
                    print("Cannot give answer to negative powers")
            elif operand == "^^":
                first = int(input("Please enter the number: "))
                second = int(input("Please enter the root you want to find: "))
                root = 1/second
                res = first**root
                history[b] = [first, "root of", second, "=", res]
                print(f"root of {first} is {res}")
            else:
                print("Invalid Input")
            b += 1
        elif menu == 2:
            if history != {}:
                print("Previous Operations done uptill now: ")
                print(history)
            else:
                print("History is empty already")
        elif menu == 3:
            if history != {}:
                clear_history = history.clear()
                print(f"History is cleared {clear_history}")
            else:
                print("Its been empty already")
        else:
            print("Invalid Input")
        menu = int(input(""" 
    ========================MAIN DISPLAY============================
    Press 1 for using Calculator operations : 
    Press 0 for exiting the Calculator :
    Press 2 for printing Previous Operations :
    Press 3 for deleting History :
    ================================================================
    """))
    if menu == 0:
        print("Thank you for using calculator")
except ValueError:
    print("Invalid Key. Please enter correct command")
except ZeroDivisionError:
    print("Cant be divided by 0")
