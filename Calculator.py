
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
        exit()
    result = num1 / num2
else:
    print("Error: Invalid operation. Please use +, -, *, or /")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")
