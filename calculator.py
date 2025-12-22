# Python Calculator
# Using only if/else condition

operator = input("Enter an operator(+, -, *, /): ")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if operator == "+":
    result = num1 + num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} {operator} {num2} = {result}")
else:
    print(f"{operator} is not a valid operator.")
