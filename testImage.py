from tkinter import *
from PIL import ImageTk
from PIL import Image
import os
import sys


#Got the Tk() to work for python 3.7
#Make sure the file is not corrupted
#make sure that you are loading for the same directory

root = Tk()
image2 = Image.open("load.png")
imageFile = ImageTk.PhotoImage(image = image2, size='200x200')
label = Label(root, image=imageFile)
label.pack()
#print(image2.format, image2.size,image2.mode)
#image2.show()

root.mainloop()
