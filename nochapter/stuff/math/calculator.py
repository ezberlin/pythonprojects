import ezmath as ez
import tkinter as tk
import sympy as sy

calculation = ""
result = 0

def addToCalculation(element):
    global calculation
    calculation = calculation + element
    calcelement.config(text=calculation)

def calculate(calculation):
    global result
    result = int(sy.sympify(calculation).evalf())
    resultelement.config(text = result)
    
def deleteAll():
    result = 0
    calculation = ""

fenster = tk.Tk()
fenster.geometry("600x200")
fenster.title("ezcalc")

calcelement = tk.Label(fenster, text = calculation,
                       font = ("Arial Rounded MT Bold", 24))
calcelement.grid(row = 1, column = 1)

add = tk.Button(fenster, text = "+",
                command = lambda: addToCalculation("+"),
                font = ("Arial Rounded MT Bold", 24))
add.grid(row = 2, column = 2)

sub = tk.Button(fenster, text = "-",
                command = lambda: addToCalculation("-"),
                font = ("Arial Rounded MT Bold", 24))
sub.grid(row = 2, column = 3)

mul = tk.Button(fenster, text = "x",
                command = lambda: addToCalculation("*"),
                font = ("Arial Rounded MT Bold", 24))
mul.grid(row = 2, column = 4)

equals = tk.Button(fenster, text = "=",
                command = lambda: calculate(calculation),
                font = ("Arial Rounded MT Bold", 24))
equals.grid(row = 2, column = 6)

resultelement = tk.Label(fenster, font = ("Arial Rounded MT Bold", 24))
resultelement.grid(row = 4, column = 1)

num1 = tk.Button(fenster, text = "1",
                command = lambda: addToCalculation("1"),
                font = ("Arial Rounded MT Bold", 24))
num1.grid(row = 3, column = 1)

num2 = tk.Button(fenster, text = "2",
                command = lambda: addToCalculation("2"),
                font = ("Arial Rounded MT Bold", 24))
num2.grid(row = 3, column = 2)

num3 = tk.Button(fenster, text = "3",
                command = lambda: addToCalculation("3"),
                font = ("Arial Rounded MT Bold", 24))
num3.grid(row = 3, column = 3)

num4 = tk.Button(fenster, text = "4",
                command = lambda: addToCalculation("4"),
                font = ("Arial Rounded MT Bold", 24))
num4.grid(row = 3, column = 4)

num5 = tk.Button(fenster, text = "5",
                command = lambda: addToCalculation("5"),
                font = ("Arial Rounded MT Bold", 24))
num5.grid(row = 3, column = 5)

num6 = tk.Button(fenster, text = "6",
                command = lambda: addToCalculation("6"),
                font = ("Arial Rounded MT Bold", 24))
num6.grid(row = 3, column = 6)

num7 = tk.Button(fenster, text = "7",
                command = lambda: addToCalculation("7"),
                font = ("Arial Rounded MT Bold", 24))
num7.grid(row = 3, column = 7)

num8 = tk.Button(fenster, text = "8",
                command = lambda: addToCalculation("8"),
                font = ("Arial Rounded MT Bold", 24))
num8.grid(row = 3, column = 8)

num9 = tk.Button(fenster, text = "9",
                command = lambda: addToCalculation("9"),
                font = ("Arial Rounded MT Bold", 24))
num9.grid(row = 3, column = 9)

            
tk.mainloop()
