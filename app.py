import sys
sys.path.insert(0, 'ext/imports/')
from dependecies import *
from tkinter import *
from PIL import ImageTk
from PIL import Image
from main import Controller
from shapes import Shapes
#import turtle
import os
import time

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
        progress_bar["value"] = 0
    #root.overrideredirect(True)
    progress_bar.start()
    root.mainloop()
"""Creates a new Node profile for user """
def Node(frame):
    node = Shapes(frame)
    node.circle(100,100,10,10,"black", 100,100, "Tan")
def Edge(frame):
    node = Shapes(frame)
    node.line(100,100,10,10,"black", 100,100, "Tan")



def start():
    root = Tk()
    test = Controller(root)
    test.run()
    #test.analytics()
    #test.updateUsers()
    #test.runvisuals()
    test.newWindow(100,100,10,10,"test",Node(root))
    test.test.newWindow(100,100,10,10,"test",Edge(root))

    #test.messageBox()
if __name__ == '__main__':
    #SplashScreen()
    start()
