from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Learn To Code at Codemy.com")

# default icon for gui window is a feather
root.iconbitmap('C:/Users/jerem/Downloads/ring.ico')

my_img = ImageTk.PhotoImage(Image.open("C:/Users/jerem/OneDrive/Pictures/Screenshot 2023-05-30 230215.png"))
my_label = Label(image=my_img)
my_label.pack()

#exit buttons
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()