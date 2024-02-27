#imports: tk, ttk
import tkinter as tk
from tkinter import ttk

def milesToKilometers(miles):
    """Converts miles to kilometers"""
    try:
        return round(miles * 1.60934, 3)
    except ValueError:
        return "Please enter a valid number!"
    
def kilometersToMiles(km):
    """Converts kilometers to miles"""
    try:
        return round(km * 0.62137, 3)
    except ValueError:
        return "Please enter a valid number!"

def swapUnits():
    """Swaps the units to convert"""
    global calculated_unit
    if calculated_unit == "miles":
        upper_label["text"] = "Miles: "
        lower_label["text"] = "Kilometers: "
        calculated_unit = "km"
    else:
        upper_label["text"] = "Kilometers: "
        lower_label["text"] = "Miles: "
        calculated_unit = "miles"
    upper_entry.delete(0, "end")
    output_value.set("")

def convert():
    """Converts the given unit to the other"""
    if calculated_unit == "miles":
        output_value.set(kilometersToMiles(float(upper_entry.get())))
    else:
        output_value.set(milesToKilometers(float(upper_entry.get())))

#creates window
root = tk.Tk()
root.geometry("150x240")
root.title("Unit Converter")
root.configure(background="cyan")

#sets style
style = ttk.Style()
style.theme_use("clam")

#creates miles label widget
upper_label = ttk.Label(root, text="Miles: ")
upper_label["font"] = ("Arial", 18)
upper_label["background"] = "cyan"
upper_label.pack(fill="x", padx=5, pady=2)

#creates miles entry widget
upper_entry = ttk.Entry(root)
upper_entry["font"] = ("Arial", 18)
upper_entry["background"] = "cyan"
upper_entry.pack(fill="x", padx=5, pady=2)
print(upper_entry.keys())

#creates kilometer label widget
lower_label = ttk.Label(root, text="Kilometers: ")
lower_label["font"] = ("Arial", 18)
lower_label["background"] = "cyan"
lower_label.pack(fill="x", padx=5, pady=2)

#creates kilometer output widget
output_value = tk.StringVar()
lower_output = ttk.Label(root)
lower_output["textvariable"] = output_value
lower_output["font"] = ("Arial", 18)
lower_output["background"] = "cyan"
lower_output.pack(fill="x", padx=5, pady=2)

#creates calculation button
calc_button = ttk.Button(root, command=convert)
calc_button["text"] = "Convert!"
calc_button.pack(fill="x", padx=5, pady=2)

#creates unit swapping button
calculated_unit = "km"
swap_button = ttk.Button(root, command=swapUnits)
swap_button["text"] = "Swap Units!"
swap_button.pack(fill="x", padx=5, pady=2)

#creates exit window button
exit_button = ttk.Button(root, command=root.destroy)
exit_button["text"] = "Exit Window!"
exit_button.pack(side="bottom", fill="x", padx=5, pady=2)

#displays window
root.mainloop()