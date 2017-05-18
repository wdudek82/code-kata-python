from tkinter import Button, Frame, Label, StringVar, Tk, ttk


root = Tk()

frame = Frame(root)

label_text = StringVar()
label = Label(frame, textvariable=label_text)
label_text.set("I am a Label")

button = Button(frame, text="Click Me")

label.pack()
button.pack()
frame.pack()

root.mainloop()
