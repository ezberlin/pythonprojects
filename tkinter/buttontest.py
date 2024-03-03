#imports: tk, ttk, pillow
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def addExclamationMark():
    """"A function that adds an exclamation mark to a StringVar"""
    global text_var
    text_var.set(text_var.get() + "!")

#create window
root = tk.Tk()
root.geometry("1080x800")

#set style
style = ttk.Style()
style.theme_use("clam")

#create photo
photo1 = ImageTk.PhotoImage(Image.open("/Users/ismail/source/pythonprojects/nochapter/tkinter/rickroll.png"))
photo2 = ImageTk.PhotoImage(Image.open("/Users/ismail/source/pythonprojects/nochapter/tkinter/rickroll2.png"))

text_var = tk.StringVar()
text_var.set("Click me") 

#create button widgets
button1 = ttk.Button(root, command=addExclamationMark)
button1.pack()

button2 = ttk.Button(root, command=root.destroy)
button2.pack()

#set button texts
button1["textvariable"] = text_var
button2["text"] = "goodBYE!!"


#set button image
button1["compound"] = "top"
button1["image"] = photo1

button2["compound"] = "top"
button2["image"] = photo2

#display image
root.mainloop()