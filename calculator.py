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
        amount = principal * (1 + rate / compound ** (compound * time))
        interest = amount - principal

        # update result label
        result_label.config(text=f"Compound Interest = {interest : .2f}")

    except ValueError:
        messagebox.showerror("Invalid input! please enter valid numbers ")

# crate main window
root = tk.Tk()
root.title("Compound Interest Calculater")

# application window
root.geometry("400x300")

# main loop
root.mainloop()

