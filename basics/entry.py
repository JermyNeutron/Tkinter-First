from tkinter import *

# entry widget

root = Tk()

# e = Entry(root, width=50)
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")

# .get() gets whatever is in the field
# .insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()
