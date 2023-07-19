def calculator():
    reset= True
    while reset:
        reset = False
        print("What operation would you like to preform? (+, -, *, /)")
        operation = input("> ")
        input1 = input("First Number> ")
        input2 = input("Second Number> ")
    
        num1 = int(input1)
        num2 = int(input2)
    
        if operation == "+":
            print(num1 + num2)
            prompt = input("Would you like to preform another calculation? (Y/N) ")
            if prompt.lower() == "y":
                reset = True
            if prompt.lower() == "n":
                print("listen its a work in progress")
                break
        if operation == "-":
            print(num1 - num2)
            prompt = input("Would you like to preform another calculation? (Y/N) ")
            if prompt.lower() == "y":
                reset = True
            if prompt.lower() == "n":
                print("listen its a work in progress")
        if operation == "*":
            print(num1 * num2)
            prompt = input("Would you like to preform another calculation? (Y/N) ")
            if prompt.lower() == "y":
                reset = True
            if prompt.lower() == "n":
                print("listen its a work in progress")
        if operation == "/":
            print(num1 / num2)
            prompt = input("Would you like to preform another calculation? (Y/N) ")
            if prompt.lower() == "y":
                reset = True
            if prompt.lower() == "n":
                print("listen its a work in progress")


class Calculator:
    pass


Calculator()