# write a calculator program that has a menu system where it is asks for a choice from a user (+ - / * !)
#it should display the output until explicitly terminated the program by writing exit
#add , sub , div , multip, div , fac, enter input, enter one number , enter second number

while True:
    choice = input("\nEnter choice (+, -, /, *, !) or 'exit': ")

    if choice == "exit":
        break

    elif choice == "!":
        num = int(input("Enter one number: "))

        fact = 1
        for i in range(1, num + 1):
            fact = fact * i

        print("Factorial =", fact)

    elif choice in ["+", "-", "*", "/"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "+":
            print("Addition =", num1 + num2)

        elif choice == "-":
            print("Subtraction =", num1 - num2)

        elif choice == "*":
            print("Multiplication =", num1 * num2)

        elif choice == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Division =", num1 / num2)

    else:
        print("Invalid choice.")