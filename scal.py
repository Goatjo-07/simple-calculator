num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Select the operation (+, -, *, /, **, //, %): ")

if operation == "+":
    answer = num1 + num2
elif operation == "-":
    answer = num1 - num2 
elif operation == "*":
    answer = num1 * num2
elif operation == "/":
    if num2 != 0:
        answer = num1 / num2
    else:
        answer = "Error: Division by zero"
elif operation == '**':
    answer = num1 ** num2
elif operation == '//':
    if num2 != 0:
        answer = num1 // num2
    else:
        answer = "Error: Division by zero"
elif operation == '%':
    if num2 != 0:
        answer = num1 % num2
    else:
        answer = "Error: Division by zero"
else:
    answer = "Error: Invalid operation"

print("Answer: ", answer)
