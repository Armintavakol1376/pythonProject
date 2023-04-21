# Simple Calculator

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {'1': add, '2': subtract, '3': multiply, '4': divide}

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = operations[choice](num1, num2)
        print("Result:", result)

    else:
        print("Invalid input. Please try again.")
