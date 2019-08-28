import sys
sys.path.insert(0, 'ext/imports/')
from dependecies import *
from tkinter import *
from PIL import ImageTk
from PIL import Image
from main import Controller
from shapes import Shapes
from Node import Node
from customization import Template
#import turtle
import os
import time

"""Start-up load screen  """


def SplashScreen():
    root = Tk()
    root.title("Works")
    image2 = Image.open("load.png")
    imageFile = ImageTk.PhotoImage(image = image2, size='200x200')
    progress_bar = ttk.Progressbar(root, orient= 'horizontal', length=300,mode="determinate")
    progress_bar.config(mode='determinate',maximum=100, value=5)
    progress_bar.pack(side="bottom")
    label = Label(master=root,image=imageFile).pack()
    progress_bar["maximum"] = 100
    for i in range(101):
        time.sleep(0.05)
        progress_bar["value"] = i
        progress_bar.update()

        progress_bar["value"] =  K0
    #root.overideredirect(True)
    progress_bar.start()
    root.mainloop()

"""Starting the Application """
def start():
    root = Tk()
    test = Controller(parent=root)

    progress_bar["value"] = 0
    #root.overrideredirect(True)
    progress_bar.start()
    root.mainloop()

def start():
    root = Tk()
    test = Controller(root)
    test.run()
    test.analytics()
    test.updateUsers()
    test.runvisuals()


if __name__ == '__main__':
    #SplashScreen()
    start()
