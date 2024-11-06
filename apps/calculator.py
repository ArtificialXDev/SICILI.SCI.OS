import os
import subprocess
import sys

def calculator():
    while True:
        # Print options for the user
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 'quit' to end the program and run kernel script")

        # Get user input
        user_input = input(": ").lower()

        # Check if the user wants to quit
        if user_input in ["quit", "q"]:
            kernel_script = os.path.join(os.getcwd(), 'KERNEL', '(link unavailable)')
            if os.path.isfile(kernel_script):
                try:
                    subprocess.run([sys.executable, kernel_script], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing kernel script: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")
            else:
                print("Yay! Success!")
            break

        # Check if the user input is a valid operator
        elif user_input in ["+", "-", "*", "/"]:
            # Get first number
            num1 = float(input("Enter a number: "))

            # Get second number
            num2 = float(input("Enter another number: "))

            # Perform operation
            if user_input == "+":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif user_input == "-":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif user_input == "*":
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif user_input == "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero.")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()
