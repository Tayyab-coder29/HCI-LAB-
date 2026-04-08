#!/usr/bin/env python3
"""
CLI Calculator with Extended Operations
Includes: add, subtract, multiply, divide, exponentiation, and modulus
"""

def cli_calculator():
    print("=== CLI Calculator ===")
    print("Available operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  ** : Exponentiation")
    print("  % : Modulus")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("Enter calculation (e.g., 5 + 3): ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            # Handle exponentiation separately (two characters)
            if "**" in user_input:
                parts = user_input.split("**")
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 ** num2
                print(f"Result: {result}\n")
            # Handle other operations
            elif "+" in user_input:
                parts = user_input.split("+")
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 + num2
                print(f"Result: {result}\n")
            elif "-" in user_input:
                parts = user_input.split("-")
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 - num2
                print(f"Result: {result}\n")
            elif "*" in user_input:
                parts = user_input.split("*")
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 * num2
                print(f"Result: {result}\n")
            elif "/" in user_input:
                parts = user_input.split("/")
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                if num2 == 0:
                    print("Error: Division by zero\n")
                else:
                    result = num1 / num2
                    print(f"Result: {result}\n")
            elif "%" in user_input:
                parts = user_input.split("%")
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                if num2 == 0:
                    print("Error: Modulus by zero\n")
                else:
                    result = num1 % num2
                    print(f"Result: {result}\n")
            else:
                print("Invalid operation. Please use +, -, *, /, **, or %\n")
        except ValueError:
            print("Invalid input. Please enter numbers.\n")
        except IndexError:
            print("Invalid format. Use format: number operator number\n")

if __name__ == "__main__":
    cli_calculator()
