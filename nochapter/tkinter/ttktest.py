import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1080x720")

image = Image.open("/Users/ismail/source/pythonprojects/nochapter/tkinter/rickroll.png")
photo = ImageTk.PhotoImage(image)

label1 = ttk.Label(root)
label1.pack()

label1.configure(image=photo)

root.mainloop()