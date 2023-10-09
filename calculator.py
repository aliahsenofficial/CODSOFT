import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Invalid input (negative number)"
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

if __name__ == '__main__':
    print("Welcome to the Scientific Calculator")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Exit")

    while True:
        choice = input("Select operation (1/2/3/4/5/6/7/8/9/10): ")

        if choice == '10':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if choice != '6' and choice != '10':
                num1 = float(input("Enter first number: "))
            
            if choice != '10':
                if choice != '6':
                    num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    operation = '+'
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = '-'
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = '*'
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = '/'
                elif choice == '5':
                    result = exponentiate(num1, num2)
                    operation = '^'
                elif choice == '7':
                    result = sine(num1)
                    operation = 'sin'
                elif choice == '8':
                    result = cosine(num1)
                    operation = 'cos'
                elif choice == '9':
                    result = tangent(num1)
                    operation = 'tan'
                else:
                    result = square_root(num1)
                    operation = 'sqrt'
                
                print(f"{num1} {operation} {num2} = {result}\n")
            else:
                print("Exiting the calculator. Goodbye!")
                break
        else:
            print("Invalid input. Please choose a valid operation (1/2/3/4/5/6/7/8/9/10).\n")
