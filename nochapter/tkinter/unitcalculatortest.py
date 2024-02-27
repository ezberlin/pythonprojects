#imports: tk, ttk
import tkinter as tk
from tkinter import ttk

def milesToKilometer():
    try:
        km = round(float(miles_entry.get()) * 1.60934, 3)
        km_value.set(km)
    except ValueError:
        pass
        km_value.set("Please enter a valid number!")

#create window
root = tk.Tk()
root.geometry("300x180")
root.title("Unit Converter")
root.configure(background="SystemButtonFace")

km_value = tk.StringVar()

#set style
style = ttk.Style()
style.theme_use("clam")

miles_label = ttk.Label(root, text="Miles: ")
miles_label["font"] = ("Arial", 18)
miles_label["background"] = "SystemButtonFace"
miles_label.pack(fill="x", padx=5, pady=2)

miles_entry = ttk.Entry(root)
miles_entry["font"] = ("Arial", 18)
miles_entry.pack(fill="x", padx=5, pady=2)

calc_button = ttk.Button(root, command=milesToKilometer)
calc_button["text"] = "Convert!"
calc_button.pack(side="bottom", fill="x", padx=5, pady=2)

km_label = ttk.Label(root, text="Kilometer: ")
km_label["font"] = ("Arial", 18)
km_label["background"] = "SystemButtonFace"
km_label.pack(fill="x", padx=5, pady=2)

km_output = ttk.Label(root)
km_output["textvariable"] = km_value
km_output["font"] = ("Arial", 18)
km_output["background"] = "SystemButtonFace"
km_output.pack(fill="x", padx=5, pady=2)

#display image
root.mainloop()