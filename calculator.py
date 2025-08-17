import arts

def multiply(n1 , n2):
    return n1 * n2

def substract(n1 , n2):
    return n1 - n2

def divide(n1 , n2):
    return n1 / n2

def add(n1 , n2):
    return n1 + n2

def mod(n1 , n2):
    return n1 % n2

def square(n1 , n2):
    return n1 ** n2

def root(n1 , n2):
    return n1 ** (1 / n2)

def factorial(n1):
    answers = 1
    for i in range(1, n1 + 1):
        answers *= i
    return answers

operations = {
    "+" : add ,
    "-" : substract ,
    "x" : multiply ,
    "/" : divide ,
    "%" : mod ,
    "^" : square,
    "$" : root,
}
operations_include = operations.keys()
def calculator():
    print(arts.calculate_logo)
    should_continue = True
    print("welcome to calculator")
    print("PLEASE YOU FOLLOW THE RULES AND INSTRUCTIONS IF YOU DON'T WANT TO GET A ERROR !")
    print("if you want to use factorial , you should press 'f' ")
    fact = input("press 'f' for fact or 'c' for another calculator ")
    if fact == "f":
        print("\n" * 30)
        print("your answer is :" ,factorial(int(input("please enter a number "))))
        calculator()
    elif fact == "c":
        try:
            num1 = float(input("enter your first number:"))
        except ValueError:
            print("You have typed an invalid number. Please try again")
            num1 = float(input("enter your first number:"))
        while should_continue:
            for symbol in operations:
                print(symbol)
            print("pay attentıon!!This '%' operator divides the numbers we select and displays the remaining result.")
            operations_symbol = input("enter your operations symbol:")
            if operations_symbol == "$":
                print("PAY ATTENTION!!This symbol is used to obtain the root. The second number you enter increases the degree of the root.")
            if not operations_symbol in operations_include:
                print("you enter a invalid operations symbol!, Do it again!")
                for symbol in operations:
                    print(symbol)
                operations_symbol = input("enter your operations symbol:")
                if operations_symbol == "$" :
                    print("PAY ATTENTION!!This symbol is used to obtain the root. The second number you enter increases the degree of the root.")
                if not operations_symbol in operations_include:
                    should_wrong_1 = True
                    while should_wrong_1:
                        for symbol in operations:
                            print(symbol)
                        operations_symbol = input("enter your operations symbol:")
                        if not operations_symbol in operations_include:
                            print("you enter a lot of invalid operations symbol!")
                            restart = int(input("please restart the calculator or enter a valid symbol, please press '1' key to restart or '2' to continue..."))
                            if restart == 1:
                                should_wrong_1 = False
                                should_continue = False
                                calculator()
                            elif restart == 2:
                                for symbol in operations:
                                    print(symbol)
                                print("pay attentıon!!This '%' operator divides the numbers we select and displays the remaining result.")
                                operations_symbol = input("enter your operations symbol:")
                                if not operations_symbol in operations_include:
                                    print("calculator is restarted because of invalid inputs! ")
                                    should_continue = False
                                    calculator()
                                print("enter a valid number!")
                                should_wrong_1 = False
                            else:
                                print("process is cancelled because of several invalid input!")
                                should_wrong_1 = False
                                should_continue = False
                                calculator()

                        else:
                            should_wrong_1 = False
                            should_continue = False

            num2 = float(input("enter your second number:"))
            answer = operations[operations_symbol](num1, num2)
            print(f"{num1} {operations_symbol} {num2} = {answer}")
            choice_1 = input(f" type :'y' to continue with {answer} or 'n' to exit:").lower()
            should_wrong = False,
            if choice_1 != "n" and choice_1 != "y":
                should_wrong = True
            if choice_1 == "y":
                should_wrong = False
                num1 = answer
            if choice_1 == "n":
                print("\n" * 30)
                print(f"your final number is {answer}")
                print("thank you for using calculator , TAKE CARE YOURSELF :)")
                should_continue = False
                should_wrong = False
            while should_wrong:
                print("you enter a invalid operation symbol!, Do it again!")
                choice = input(f" type :'y' to continue with {answer} or 'n' to exit:").lower()
                if choice != "n" and choice != "y":
                    should_wrong = True
                if choice == "y":
                    should_wrong = False
                    num1 = answer
                if choice == "n":
                    print("\n" * 30)
                    print(f"your final number is {answer}")
                    should_continue = False
                    should_wrong = False
    else:
        print("\n" * 30)
        print("you enter invalid input!!")
        print("please follow the rules of sentences , TRY AGAIN!!")
        calculator()
calculator()
