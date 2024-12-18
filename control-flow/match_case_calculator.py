num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sign = input("Choose the operation (+, -, *, /): ")


match sign:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        match num2:
            case 0: 
                print("Cannot divide by zero.")
            case _: 
                result = num1 / num2
                print(f"The result is {result}.")

