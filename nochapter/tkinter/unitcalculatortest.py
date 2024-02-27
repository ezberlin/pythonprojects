#imports: tk, ttk
import tkinter as tk
from tkinter import ttk

#create window
root = tk.Tk()
root.geometry("300x180")
root.title("Unit Converter")
root.configure(background="SystemButtonFace")

#set style
style = ttk.Style()
style.theme_use("clam")

miles_label = ttk.Label(root, text="Miles: ")
miles_label["font"] = ("Arial", 18)
miles_label["background"] = "SystemButtonFace"
miles_label.pack(fill="x", padx=5, pady=2)

miles_entry = ttk.Entry(root)
miles_entry["font"] = ("Arial", 18)
miles_entry["background"] = "SystemButtonFace"
miles_entry.pack(fill="x", padx=5, pady=2)

km_label = ttk.Label(root, text="Kilometer: ")
km_label["font"] = ("Arial", 18)
km_label["background"] = "SystemButtonFace"
km_label.pack(fill="x", padx=5, pady=2)


#display image
root.mainloop()