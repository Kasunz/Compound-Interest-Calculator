import tkinter as tk
from tkinter import messagebox

# Function to calculate compound interest
def calculate():
    try:
        # Retrieve and validate inputs
        principal = float(principal_entry.get())
        rate = float(rate_entry.get()) / 100
        time = float(time_entry.get())
        compound = int(compound_entry.get())

        # compound interest formula
        amount = principal * (1 + rate / compound) ** (compound * time)
        interest = amount - principal

        # update result label
        result_label.config(text=f"Compound Interest = {interest:.2f}")

    except ValueError:
        messagebox.showerror("Invalid input! please enter valid numbers ")

# crate main window
root = tk.Tk()
root.title("Compound Interest Calculator")

# application window
root.geometry("400x300")


# initialize main tkinter window
tk.Label(root, text="Principal amount: ").grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Rate of Interest (%): " ).grid(row = 1, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1)

tk.Label(root, text="Time (Years): ").grid(row=2, column=0, padx= 10, pady=10)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

tk.Label(root, text="Times compound (year)").grid(row=3, column=0, padx=10, pady=10)
compound_entry = tk.Entry(root)
compound_entry.grid(row=3, column=1)

# output label for result
result_label = tk.Label(root, text="Compound Interest: ")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# calculate button
calculate_button = tk.Button(root, text="calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# adding padding to widgets
for widget in root.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# main loop
root.mainloop()

