num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
user_sign = input("Choose the operation (+, -, *, /): ")


if user_sign == "+":
    add = num1 + num2
    print(f"The result is {add}.")
elif user_sign == "-":
    add = num1 - num2
    print(f"The result is {add}.")
elif user_sign == "*":
    add = num1 * num2
    print(f"The result is {add}.")
elif user_sign == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        add = num1 / num2   
        print(f"The result is {add}.")
else:
    print("you enter the wrong input")