print("Welcome To  the Calculator")

print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

''')

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def floor_divide(a, b): return a // b
def modulus(a, b): return a % b
def exponentiation(a, b): return a ** b
def square_root(a): return a ** 0.5

continue_calculation = True
num1 = int(input("Enter First Number : "))

while continue_calculation:
    print('''
Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Floor Division (//)
6. Modulus (%)
7. Exponentiation (**)
8. Square Root (sqrt)
''')

    operation = input("Enter the operation you want to perform : ")

    if operation != 'sqrt':
        num2 = int(input("Enter Second Number : "))
    else:
        num2 = None

    def calculator(num1, num2, operation):
        if operation == '+':
            return add(num1, num2)
        elif operation == '-':
            return subtract(num1, num2)
        elif operation == '*':
            return multiply(num1, num2)
        elif operation == '/':
            return divide(num1, num2)
        elif operation == '//':
            return floor_divide(num1, num2)
        elif operation == '%':
            return modulus(num1, num2)
        elif operation == '**':
            return exponentiation(num1, num2)
        elif operation == 'sqrt':
            return square_root(num1)
        else:
            return "Invalid Input"

    result = calculator(num1, num2, operation)
    print("The Result is:", result)

    option = input("Do you want to continue with this result? Type 'yes' or 'no': ").lower()
    if option == "yes":
        num1 = result
    else:
        continue_calculation = False
