from tkinter import *
from PIL import ImageTk
from PIL import Image
import os
import sys

root = Tk()
image2 = Image.open("load.png")
imageFile = ImageTk.PhotoImage(image = image2, size='200x200')
label = Label(master=root,image=imageFile)
label.pack()
root.mainloop()
