from tkinter import Tk, ttk
from tkinter import Button, Entry, Event, Label
from tkinter import LEFT


def get_sum(event):
    entry_sum.delete(0, "end")

    num1 = float(entry1.get()) if (entry1.get()).isdigit() else 0
    num2 = float(entry2.get()) if entry2.get().isdigit() else 0

    entry_sum.insert(0, num1 + num2)

    print("Clicked")



root = Tk()

entry1 = Entry(root)
entry1.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

entry2 = Entry(root)
entry2.pack(side=LEFT)

equal_button = Button(root, text="=")

equal_button.bind("<Button-1>", get_sum)
equal_button.pack(side=LEFT)

entry_sum = Entry(root)
entry_sum.pack(side=LEFT)

root.mainloop()