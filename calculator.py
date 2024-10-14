import tkinter as tk
from tkinter import messagebox


class CompoundInterestCalculator:
    def __init__(self, parent):
        self.root = parent
        self.root.title("Compound Interest Calculator")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')

        # Initialize instance variables
        self.principal_entry = None
        self.rate_entry = None
        self.time_entry = None
        self.compound_entry = None
        self.result_label = None
        self.reset_button = None

        # Initialize UI components
        self.create_widgets()

        #initialize UI components
        self.create_widgets()

    def create_widgets(self):
        # Initialize main tkinter window
        tk.Label(self.root, text="Principal amount: ").grid(row=0, column=0, padx=10, pady=10)
        self.principal_entry = tk.Entry(self.root)
        self.principal_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Rate of Interest (%): ").grid(row=1, column=0, padx=10, pady=10)
        self.rate_entry = tk.Entry(self.root)
        self.rate_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Time (Years): ").grid(row=2, column=0, padx=10, pady=10)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Times compounded (year)").grid(row=3, column=0, padx=10, pady=10)
        self.compound_entry = tk.Entry(self.root)
        self.compound_entry.grid(row=3, column=1)

        # Output label for result
        self.result_label = tk.Label(self.root, text="Compound Interest: ")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_fields)
        self.reset_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Add padding to widgets
        for widget in self.root.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    # Function to calculate compound interest
    def calculate(self):
        try:
            # Retrieve and validate inputs
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get()) / 100
            time = float(self.time_entry.get())
            compound = int(self.compound_entry.get())

            # Add validation to ensure positive values
            if principal <= 0 or rate <= 0 or time <= 0 or compound <= 0:
                raise ValueError("All values must be positive.")

            # Compound interest formula
            amount = principal * (1 + rate / compound) ** (compound * time)
            interest = amount - principal

            # Update result label
            self.result_label.config(text=f"Compound Interest = {interest:.2f}")

        except ValueError:
            messagebox.showerror("Invalid input!", "Please enter valid positive numbers.")

    def reset_fields(self):
        # Clear the input fields and result
        self.principal_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.compound_entry.delete(0, tk.END)
        self.result_label.config(text="Compound Interest: ")


# Create main window and start the application
root = tk.Tk()
app = CompoundInterestCalculator(root)
root.mainloop()

