import math
import random

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def main():
    operations = {
        1: {"name": "Addition", "function": add, "symbol": "+"},
        2: {"name": "Subtraction", "function": subtract, "symbol": "-"},
        3: {"name": "Multiplication", "function": multiply, "symbol": "*"},
        4: {"name": "Division", "function": divide, "symbol": "/"},
        5: {"name": "Power", "function": power, "symbol": "^"},
    }

    print("Select operation:")
    for key, value in operations.items():
        print(f"{key}. {value['name']}")

    while True:
        try:
            choice = int(input("Choose the operation (1-5): "))
            if choice in operations:
                break
            else:
                print("Invalid input. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = operations[choice]["function"](num1, num2)
        print(f"{num1} {operations[choice]['symbol']} {num2} = {result}")
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()