import tkinter as tk
from tkinter import ttk
from pil import Image, ImageTk

root = tk.Tk()
root.geometry("1080x720")

photo = ImageTk.PhotoImage(Image.open("rickroll.jpg"))

label1 = ttk.Label(root)
label1.pack()

label1.configure(image=photo)

root.mainloop()