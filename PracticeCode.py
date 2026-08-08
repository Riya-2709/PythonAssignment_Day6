#1 Write a Python program that takes two numbers as input and performs division.
#Handle the ZeroDivisionError if the second number is zero.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Division =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")

#2 Write a Python program that asks the user for a filename and displays its contents. 
#Handle the FileNotFoundError if the file does not exist.
try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

except FileNotFoundError:
    print("Error: File not found.")


#3 Write a Python program that accepts a number from the user. If the user enters invalid input (e.g., text instead of a number),
#display an appropriate error message using exception handling.

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")