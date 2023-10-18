"""My first calculator"""

import tkinter as tk
from tkinter import Entry, Label
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Калькулятор ПЛЮС")

        self.e = Entry(root, width=35, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('%', 4, 0), ('π', 4, 2),
            ('√', 5, 0), ('^', 5, 1), ('log', 5, 2), ('cos', 5, 3),
            ('sin', 6, 0), ('DMS', 6, 1),
            ('C', 6, 2), ('=', 6, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, width=10, height=2, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        current = str(self.e.get())
        if char in '0123456789':
            self.e.delete(0, tk.END)
            self.e.insert(0, current + char)
        elif char in '+-*/%^':
            self.e.delete(0, tk.END)
            self.e.insert(0, current + char)
        elif char == 'π':
            self.e.delete(0, tk.END)
            self.e.insert(0, math.pi)
        elif char == 'DMS':
            deg = int(float(current))
            min = int((float(current) - deg) * 60)
            sec = (float(current) - deg - min/60) * 3600
            self.e.delete(0, tk.END)
            self.e.insert(0, f'{deg}°{min}\'{sec}"')
        elif char == '√':
            self.e.delete(0, tk.END)
            self.e.insert(0, math.sqrt(float(current)))
        elif char == '^':
            self.e.delete(0, tk.END)
            self.e.insert(0, current + '**')
        elif char == 'log':
            self.e.delete(0, tk.END)
            self.e.insert(0, math.log(float(current)))
        elif char == 'cos':
            self.e.delete(0, tk.END)
            self.e.insert(0, math.cos(math.radians(float(current))))
        elif char == 'sin':
            self.e.delete(0, tk.END)
            self.e.insert(0, math.sin(math.radians(float(current))))
        elif char == 'C':
            self.e.delete(0, tk.END)
        elif char == '=':
            self.e.delete(0, tk.END)
            self.e.insert(0, str(eval(current.replace('^', '**'))))

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
