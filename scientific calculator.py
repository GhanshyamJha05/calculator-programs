import math

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm_base_10(x):
    if x > 0:
        return math.log10(x)
    else:
        return "Error! Logarithm of non-positive number."

def natural_logarithm(x):
    if x > 0:
        return math.log(x)
    else:
        return "Error! Logarithm of non-positive number."

def main():
    print("Scientific Calculator (Advanced Functions Only)")
    print("Select operation:")
    print("1. Exponentiate")
    print("2. Square Root")
    print("3. Sine")
    print("4. Cosine")
    print("5. Tangent")
    print("6. Logarithm Base 10")
    print("7. Natural Logarithm")

    while True:
        choice = input("Enter choice (1-7) or 'q' to quit: ")

        if choice == 'q':
            break

        if choice in ['1']:
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

        elif choice in ['2', '3', '4', '5', '6', '7']:
            num = float(input("Enter the number: "))

            if choice == '2':
                print(f"√{num} = {square_root(num)}")
            elif choice == '3':
                print(f"sin({num}) = {sine(num)}")
            elif choice == '4':
                print(f"cos({num}) = {cosine(num)}")
            elif choice == '5':
                print(f"tan({num}) = {tangent(num)}")
            elif choice == '6':
                print(f"log10({num}) = {logarithm_base_10(num)}")
            elif choice == '7':
                print(f"ln({num}) = {natural_logarithm(num)}")

        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
