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
label1 = tk.Label(root, text="Never gonna give you up", bg="red")
label1.pack(side="left", expand=True, fill="both")

label2 = tk.Label(root, text="Never gonna let you down", bg="orange")
label2.pack(side="right", expand=True, fill="both")

#main loop
root.mainloop()

#exit
print("Fenster geschlossen")