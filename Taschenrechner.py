import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Taschenrechner")

        self.expression = ""
        self.entry = tk.Entry(master, width=20, font=("Arial", 18), borderwidth=2, relief="groove", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 14),
                                command=self.calculate)
            else:
                btn = tk.Button(master, text=text, width=5, height=2, font=("Arial", 14),
                                command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)

        clear_btn = tk.Button(master, text="C", width=5, height=2, font=("Arial", 14),
                              command=self.clear)
        clear_btn.grid(row=5, column=0, columnspan=4, sticky="we", padx=2, pady=2)

    def on_button_click(self, char):
        self.expression += str(char)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Fehler", "Ungültige Eingabe")
            self.clear()

def start_app():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_app()
def add(x, y):
    return x + y
    class CalculatorApp:
        def __init__(self, master):
            self.master = master
            master.title("Taschenrechner")

            self.label1 = tk.Label(master, text="Erste Zahl:")
            self.label1.grid(row=0, column=0)
            self.entry1 = tk.Entry(master)
            self.entry1.grid(row=0, column=1)

            self.label2 = tk.Label(master, text="Zweite Zahl:")
            self.label2.grid(row=1, column=0)
            self.entry2 = tk.Entry(master)
            self.entry2.grid(row=1, column=1)

            self.result_label = tk.Label(master, text="Ergebnis:")
            self.result_label.grid(row=2, column=0)
            self.result = tk.Label(master, text="")
            self.result.grid(row=2, column=1)

            self.add_button = tk.Button(master, text="Addieren", command=self.add)
            self.add_button.grid(row=3, column=0)
            self.sub_button = tk.Button(master, text="Subtrahieren", command=self.subtract)
            self.sub_button.grid(row=3, column=1)
            self.mul_button = tk.Button(master, text="Multiplizieren", command=self.multiply)
            self.mul_button.grid(row=4, column=0)
            self.div_button = tk.Button(master, text="Dividieren", command=self.divide)
            self.div_button.grid(row=4, column=1)

        def get_numbers(self):
            try:
                x = float(self.entry1.get())
                y = float(self.entry2.get())
                return x, y
            except ValueError:
                messagebox.showerror("Fehler", "Ungültige Eingabe. Bitte Zahlen eingeben.")
                return None, None

        def add(self):
            x, y = self.get_numbers()
            if x is not None:
                self.result.config(text=str(add(x, y)))

        def subtract(self):
            x, y = self.get_numbers()
            if x is not None:
                self.result.config(text=str(subtract(x, y)))

        def multiply(self):
            x, y = self.get_numbers()
            if x is not None:
                self.result.config(text=str(multiply(x, y)))

        def divide(self):
            x, y = self.get_numbers()
            if x is not None:
                res = divide(x, y)
                self.result.config(text=str(res))

    def start_app():
        root = tk.Tk()
        app = CalculatorApp(root)
        root.mainloop()
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Fehler: Division durch Null!"
    return x / y

def main():
    print("Einfacher Taschenrechner")
    print("Operationen:")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")

    choice = input("Wähle eine Operation (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Ungültige Auswahl")
        return

    try:
        num1 = float(input("Gib die erste Zahl ein: "))
        num2 = float(input("Gib die zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte Zahlen eingeben.")
        return

    if choice == '1':
        print("Ergebnis:", add(num1, num2))
    elif choice == '2':
        print("Ergebnis:", subtract(num1, num2))
    elif choice == '3':
        print("Ergebnis:", multiply(num1, num2))
    elif choice == '4':
        print("Ergebnis:", divide(num1, num2))

if __name__ == "__main__":
    main()