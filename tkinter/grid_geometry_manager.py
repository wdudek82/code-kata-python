from tkinter import Tk, ttk
from tkinter import Button, Entry, Label
from tkinter import N, NE, NW, W, E, S, SE, SW


root = Tk()

Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

button = Button(root, text="Submit").grid(row=2, column=0, sticky=W, pady=4)
button = Button(root, text="Clear").grid(row=2, column=1, sticky=W, pady=4)

root.mainloop()