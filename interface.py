import tkinter as tk
from tkinter import messagebox
from calculator import Calculator

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x200")
        self.calculator = Calculator()
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ("1", 1), ("2", 2), ("3", 3), ("+", "+"),
            ("4", 4), ("5", 5), ("6", 6), ("-", "-"),
            ("7", 7), ("8", 8), ("9", 9), ("*", "*"),
            ("C", "C"), ("0", 0), ("=", "="), ("/", "/")
        ]

        row = 1
        col = 0
        for (text, value) in buttons:
            if text == "=":
                btn = tk.Button(self, text=text, width=20, command=self.calculate)
                btn.grid(row=row, column=col, columnspan=2)
            elif text == "C":
                btn = tk.Button(self, text=text, width=20, command=self.clear)
                btn.grid(row=row, column=col, columnspan=2)
            else:
                btn = tk.Button(self, text=text, width=5, command=lambda v=value: self.add_to_display(v))
                btn.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_to_display(self, value):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + str(value))

    def clear(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        expression = self.display.get()
        self.calculator.equation = expression
        result = self.calculator.calculate_result()
        self.display.delete(0, tk.END)
        self.display.insert(0, result)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

