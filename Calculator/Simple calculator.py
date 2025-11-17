print("Simple Calculator")
print("Operations: +, -, *, /")
num1 = float(input("Enter the first number: "))
operator = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
result = None
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error! Cannot divide by zero.")
else:
    print("Invalid operator!")
if result is not None:
    print(f"Result: {result}")