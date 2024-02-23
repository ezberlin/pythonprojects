import tkinter as tk

#create window
root = tk.Tk()
root.title("Rickroll")

#resize window
root.geometry("1080x720")
root.minsize(720, 480)
root.maxsize(1920, 1080)
root.resizable(width=True, height=True)

#text
label1 = tk.Label(root, text="Never gonna give you up")
label1.pack()

#main loop
root.mainloop()

#exit
print("Fenster geschlossen")