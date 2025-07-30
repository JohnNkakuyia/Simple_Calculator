# ask for two nmbers
num1= float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# ask for operation
operation = input("Enter operation (+, -, *, /): ")
# perform calculation based on operation
if operation == '+':
    result = num1 + num2
    print(f"{num1}+{num2}= {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1}-{num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1}*{num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1}/{num2} = {result}")
    else:
        print("Error: undefined (division by zero)")
else:
    print("Error: Invalid operation. Please enter one of +, -, *, /.")