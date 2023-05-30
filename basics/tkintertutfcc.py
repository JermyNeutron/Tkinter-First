from tkinter import *

#first thing we create is the root widet aka window..
root = Tk()

# creating a Label widget
myLabel1 = Label(root, text="Hello, World!")
myLabel2 = Label(root, text="My name is Jeremy Crisostomo")

# .pack = shoving in at the first available spot in the screen.
# myLabel.pack()

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

# when you have a program open, it is always looping...
# an event loop
root.mainloop()
