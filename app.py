import sys
sys.path.insert(0, 'ext/imports/')
from dependecies import *
from tkinter import *
from PIL import ImageTk
from PIL import Image
from main import Controller
<<<<<<< HEAD
from shapes import Shapes
from Node import Node
from customization import Template
=======


>>>>>>> 73be496... Finish
#import turtle
import os
import time

<<<<<<< HEAD
"""Start-up load screen  """




"""Starting the Application """
def start():
    root = Tk()
    test = Controller(parent=root)

    progress_bar["value"] = 0
    #root.overrideredirect(True)
    progress_bar.start()
    root.mainloop()
=======
"""Starting the Application """

>>>>>>> 73be496... Finish

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
