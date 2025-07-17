import tkinter as tk
from tkinter import messagebox
import math
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('tk', 'scaling', 2.0)  
        self.title("Taschenrechner")
        self.geometry("600x900")  
        self.resizable(False, False)
        self.configure(bg="#222")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self, bg="#222")
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(
            input_frame, font=('Arial', 32), textvariable=self.input_text,  
            bg="#333", fg="#b20000", bd=0, justify=tk.RIGHT  
        )
        input_field.pack(expand=True, fill="both", ipady=30)  

        btns_frame = tk.Frame(self, bg="#222")
        btns_frame.pack(expand=True, fill="both")

        buttons = [
            ['C', '(', ')', '/'],
            ['x²', 'x³', '√', '*'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['0', '.', '%', '']
        ]

        for row in buttons:
            row_frame = tk.Frame(btns_frame, bg="#222")
            row_frame.pack(expand=True, fill="both")
            for btn in row:
                if btn == '':
                    tk.Label(row_frame, bg="#222").pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
                    continue
                b = tk.Button(
                    row_frame, text=btn, font=('Arial', 24), fg="#fff", bg="#660000", 
                    bd=0, relief=tk.FLAT, activebackground="#990000", activeforeground="#fff",
                    command=lambda x=btn: self.on_button_click(x)
                )
                b.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                expr = self.expression.replace('%', '/100')
                result = str(eval(expr))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Fehler")
                self.expression = ""
        elif char == 'x²':
            try:
                value = eval(self.expression)
                result = str(value ** 2)
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Fehler")
                self.expression = ""
        elif char == 'x³':
            try:
                value = eval(self.expression)
                result = str(value ** 3)
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Fehler")
                self.expression = ""
        elif char == '√':
            try:
                value = eval(self.expression)
                result = str(math.sqrt(value))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Fehler")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()