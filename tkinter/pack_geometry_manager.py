from tkinter import Button, Frame, Label, Tk, ttk
from tkinter import LEFT, RIGHT, TOP, BOTTOM, X, Y


root = Tk()

frame = Frame(root)

Label(frame, text="A Bunch of Buttons").pack()
Button(frame, text="One").pack(side=LEFT, fill=Y)
Button(frame, text="Two").pack(side=TOP, fill=X)
Button(frame, text="Three").pack(side=RIGHT, fill=X)
Button(frame, text="Four").pack(side=BOTTOM, fill=X)

frame.pack()

root.mainloop()