# Basic calculator
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Get operator and input from the user
num1 = float(input("Enter first number: "))
operator = input("Enter operator(+ / - /* or /):")
num2 = float(input("Enter second number: "))

if operator == '+':
    print(num1, "+", num2, "=", add(num1, num2))

elif operator == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif operator == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif operator == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
