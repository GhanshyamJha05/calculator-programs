#simple calcultaor with all kind of operations
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

# Scientific functions
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive numbers is undefined."
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error! Factorial of negative numbers is undefined."
    return math.factorial(int(x))

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. Logarithm (base 10)")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")
    print("13. Factorial")

    while True:
        choice = input("Enter choice (1-13): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")

            elif choice == '6':
                print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")

            elif choice == '7':
                print(f"{num1} // {num2} = {floor_divide(num1, num2)}")

        elif choice in ['8', '9', '10', '11', '12', '13']:
            num1 = float(input("Enter number: "))

            if choice == '8':
                print(f"Square root of {num1} = {square_root(num1)}")

            elif choice == '9':
                base_choice = input("Enter base (default is 10): ")
                base = 10 if base_choice == '' else float(base_choice)
                print(f"Logarithm of {num1} (base {base}) = {logarithm(num1, base)}")

            elif choice == '10':
                print(f"Sine of {num1} degrees = {sine(num1)}")

            elif choice == '11':
                print(f"Cosine of {num1} degrees = {cosine(num1)}")

            elif choice == '12':
                print(f"Tangent of {num1} degrees = {tangent(num1)}")

            elif choice == '13':
                print(f"Factorial of {num1} = {factorial(num1)}")

        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
        print("thanks for using!!")

if __name__ == "__main__":
   calculator()
