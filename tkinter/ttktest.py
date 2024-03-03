#imports: tk, ttk, pillow, random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

#create window
root = tk.Tk()
root.geometry("1080x800")

#set style
style = ttk.Style()
style.theme_use("clam")

#load photos
photo = ImageTk.PhotoImage(Image.open("/Users/ismail/source/pythonprojects/nochapter/tkinter/rickroll.png").resize((1080, 700)))
photo2 = ImageTk.PhotoImage(Image.open("/Users/ismail/source/pythonprojects/nochapter/tkinter/rickroll2.png").resize((1080, 700)))

#create label widget
label1 = ttk.Label(root, text = "You've been rickrolled!")
label1.pack()

#set font & size
label1["font"] = ("Wingdings", 50)

#set compound
label1["compound"] = "top"


#set images to widget
label1["image"] = photo
if(random.randint(0, 1)):
    label1["image"] = photo2

#set bg color
label1["background"] = "orange"

#print key options
print(label1.keys())

#display image
root.mainloop()