from tkinter import *

# instantiation of tkinter
window = Tk()
# title the window
window.title("Welcome to GUI app")
# size of the window
window.geometry('350x200')
# adding a label on the window
lbl = Label(window, text="Hello")
# positioning the label on the top of the window
lbl.grid(column=0, row=0)
# adding a textbox with a limited width
txt = Entry(window, width=10)
# Positioning the textbox on the window
txt.grid(column=1, row=0)

# adding a result label
msg = Label(window, text="")
# Positioning the label on the second line of the window
msg.grid(column=0, row=1)


# adding an action on the button
def clicked():
    # formatting a message to be displayed by concatenating the Hello word with the entered value
    greeting = "Hello " + txt.get()
    msg.configure(text=greeting)


# Adding a button on the window
btn = Button(window, text="Click Me", command=clicked)
# Positioning the Button on the window
btn.grid(column=2, row=0)

window.mainloop()
