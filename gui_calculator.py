#!/usr/bin/env python3
"""
GUI Calculator with Extended Operations
Features: Add, Subtract, Multiply, Divide, Exponentiation, Modulus, and Clear button
"""

import tkinter as tk
from tkinter import ttk

def calculate():
    """Perform calculation based on selected operation"""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                result_label.config(text="Error: Division by zero", fg="red")
                return
            result = num1 / num2
        elif operation == "exponentiation":
            result = num1 ** num2
        elif operation == "modulus":
            if num2 == 0:
                result_label.config(text="Error: Modulus by zero", fg="red")
                return
            result = num1 % num2
        
        result_label.config(text=f"Result: {result}", fg="green")
    except ValueError:
        result_label.config(text="Error: Invalid input", fg="red")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

def clear_fields():
    """Clear all input fields and result"""
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ", fg="black")
    operation_var.set("add")

# Create the main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Configure style
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))

# Title label
title_label = tk.Label(root, text="GUI Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Frame for input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# First number input
label1 = tk.Label(input_frame, text="Number 1:", font=("Arial", 10))
label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry1 = tk.Entry(input_frame, width=20, font=("Arial", 11))
entry1.grid(row=0, column=1, padx=5, pady=5)

# Second number input
label2 = tk.Label(input_frame, text="Number 2:", font=("Arial", 10))
label2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry2 = tk.Entry(input_frame, width=20, font=("Arial", 11))
entry2.grid(row=1, column=1, padx=5, pady=5)

# Operation selection
operation_label = tk.Label(root, text="Select Operation:", font=("Arial", 10))
operation_label.pack(pady=5)

operation_var = tk.StringVar(value="add")
operations = [
    ("Addition (+)", "add"),
    ("Subtraction (-)", "subtract"),
    ("Multiplication (×)", "multiply"),
    ("Division (÷)", "divide"),
    ("Exponentiation (^)", "exponentiation"),
    ("Modulus (%)", "modulus")
]

operation_menu = tk.OptionMenu(root, operation_var, *[op[1] for op in operations])
operation_menu.config(width=20, font=("Arial", 10))
operation_menu.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Calculate button
calculate_button = tk.Button(
    button_frame, 
    text="Calculate", 
    command=calculate,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12,
    height=2
)
calculate_button.grid(row=0, column=0, padx=5)

# Clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#f44336",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12,
    height=2
)
clear_button.grid(row=0, column=1, padx=5)

# Result label
result_label = tk.Label(
    root, 
    text="Result: ", 
    font=("Arial", 14, "bold"),
    fg="black"
)
result_label.pack(pady=20)

# Run the application
if __name__ == "__main__":
    root.mainloop()
