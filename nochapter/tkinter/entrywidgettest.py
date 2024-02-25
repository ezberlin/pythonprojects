#imports: tk, ttk
import tkinter as tk
from tkinter import ttk

def print_input():
    """prints the input of the entry into the command line"""
    print(entry1.get())
    returned_label = ttk.Label(root, text=entry1.get())
    returned_label.pack()

def delete_input():
    """deletes the input of the entry"""
    entry1.delete(0, tk.END)

#create window
root = tk.Tk()
root.geometry("1080x800")

#set style
style = ttk.Style()
style.theme_use("clam")

#create entry widget
entry1 = ttk.Entry(root)
entry1.pack()

#change entry width
entry1["width"] = 40

#change entry justify
entry1["justify"] = "center"

#change entry color
entry1["foreground"] = "blue"

#give entry a start text
entry1.insert(0, "sussy ")
entry1.insert(6, "baka")

#create entry print button
entry_print_button = ttk.Button(root, command=print_input)
entry_print_button.pack()

#set entry print button text
entry_print_button["text"] = "save"

#create entry delete button
entry_delete_button = ttk.Button(root, command=delete_input)
entry_delete_button.pack()

#set entry save button text
entry_delete_button["text"] = "delete"

#create quit button
quit_button = ttk.Button(root, command=root.destroy, text="Stop")
quit_button.pack(side="bottom")

#display image
root.mainloop()