#imports: tk, ttk
import tkinter as tk
from tkinter import ttk

#create window
root = tk.Tk()
root.geometry("1080x800")

#set style
style = ttk.Style()
style.theme_use("clam")

#create stringvar for label
text_var = tk.StringVar()
text_var.set("lol")

#create label widget
label1 = ttk.Label(root, textvariable=text_var)
label1.pack()

#change stringvar and print it
text_var.set("lololol")
print(text_var.get())

#set bg color
label1["background"] = "orange"

#display image
root.mainloop()