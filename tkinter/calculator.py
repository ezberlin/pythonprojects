#imports: tk, ttk
import tkinter as tk
from tkinter import ttk

#creates window
root = tk.Tk()
root.geometry("720x1080")
root.title("Calculator")

#sets style
style = ttk.Style()
style.theme_use("clam")
style.configure('.', font=('Futura', 32))

button1 = ttk.Button(root, text="Aa")
button1.grid(row=1, column=1, ipady=10, ipadx=10)
print(button1.keys())




#displays window
root.mainloop()