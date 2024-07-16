import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Invalid operation"
        
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='lightgreen')  # Set the background color of the main window

# Create and place the widgets
tk.Label(root, text="Enter first number:", bg='lightgreen').grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:", bg='lightgreen').grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Select operation:", bg='lightgreen').grid(row=2, column=0, padx=10, pady=10)

operation_var = tk.StringVar(root)
operation_var.set("Add")  # default value

# Create radio buttons for each operation
radio_add = tk.Radiobutton(root, text="Add", variable=operation_var, value="Add", bg='lightgreen')
radio_subtract = tk.Radiobutton(root, text="Subtract", variable=operation_var, value="Subtract", bg='lightgreen')
radio_multiply = tk.Radiobutton(root, text="Multiply", variable=operation_var, value="Multiply", bg='lightgreen')
radio_divide = tk.Radiobutton(root, text="Divide", variable=operation_var, value="Divide", bg='lightgreen')

radio_add.grid(row=2, column=1, padx=10, pady=5, sticky="w")
radio_subtract.grid(row=3, column=1, padx=10, pady=5, sticky="w")
radio_multiply.grid(row=4, column=1, padx=10, pady=5, sticky="w")
radio_divide.grid(row=5, column=1, padx=10, pady=5, sticky="w")

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg='lightgrey')
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)

tk.Label(root, text="Result:", bg='lightgreen').grid(row=7, column=0, padx=10, pady=10)
result_entry = tk.Entry(root)
result_entry.grid(row=7, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
