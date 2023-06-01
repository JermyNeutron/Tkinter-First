from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Basic Image Viewer")
root.iconbitmap("C:/Users/jerem/Downloads/ring.ico")

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/jerem/Git/Tkinter-First/image viewer/images/orange1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/jerem/Git/Tkinter-First/image viewer/images/orange2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/jerem/Git/Tkinter-First/image viewer/images/orange3.jpg"))

image_list = [my_img1, my_img2, my_img3]



my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # .grid_forget() is an internal function the grid system can use to delete something.
    my_label.grid_forget()

def back():
    global my_label
    global button_forward
    global button_back

button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()