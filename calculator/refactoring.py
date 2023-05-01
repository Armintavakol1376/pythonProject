# This is refactoring of previous code names "simple calculator".

# first operation
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Error: division by zero")
        return None
    else:
        return num1 / num2

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result:", result)

elif choice == '2':
    result = subtract(num1, num2)
    print("Result:", result)

elif choice == '3':
    result = multiply(num1, num2)
    print("Result:", result)

elif choice == '4':
    result = divide(num1, num2)
    if result is not None:
        print("Result:", result)

else:
    print("Invalid input. Please try again.")
