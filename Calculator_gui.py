import tkinter as tk  # Import the GUI module

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")  # Set the window title

# Entry widget to display input and output
entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to add text to the entry box
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear the entry box
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())  # Use eval to compute the result
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define the layout of calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        action = button_equal
    else:
        action = lambda x=text: button_click(x)
    tk.Button(root, text=text, width=6, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col)

# Clear button (separate row)
tk.Button(root, text="Clear", width=26, height=2, font=("Arial", 14),
          command=button_clear).grid(row=5, column=0, columnspan=4)

# Start the event loop
root.mainloop()
