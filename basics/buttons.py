from tkinter import *

# button widget

root = Tk()

# everything in tkinter is a widget, so a button is a widget

# create a function for something to happen
def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()

# myButton = Button(root, text="Click Me!", state=DISABLED, padx=50, pady=50)
# myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()
