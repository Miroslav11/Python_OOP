import tkinter as tk
import webbrowser

def learn(event):
	webbrowser.open_new_tab("http://cleverprogrammer.com/courses/enrolled/130834")

def github(event):
	webbrowser.open_new_tab("https://github.com/Miroslav11")

def cant_touch_this(event):
	webbrowser.open_new_tab("https://youtu.be/otCpCn0l4Wo?t=13")

window = tk.Tk()
window.title("Learning Python")
window.geometry("310x50")

label_1 = tk.Label(text="OOP Python")
label_1.grid(column=0, row=0)

label_2 = tk.Label(text="My Github page")
label_2.grid(column=1, row=0)

label_3 = tk.Label(text="Dont touch this!!!")
label_3.grid(column=2, row=0)

button1 = tk.Button(window, text="Open OOP Python")
button1.grid(column=0, row=1)

button2 = tk.Button(window, text="Open My Github")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="NOOOO!!! :)")
button3.grid(column=2, row=1)

button1.bind("<Button-1>", learn)

button2.bind("<Button-1>", github)

button3.bind("<Button-1>", cant_touch_this)

window.mainloop()