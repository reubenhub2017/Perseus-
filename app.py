import sys
sys.path.insert(0, 'ext/imports/')
from dependecies import *

from main import Controller
from shapes import Shapes
import turtle
global root


def add(x,y):
    return  x + y
def start():
    root = Tk()
    test = Controller(root)
    test.run()
    test.analytics()
    test.updateUsers()
    #test.SplashScreen()
    test.runvisuals()
    #test.newWindow(100,100,10,10,"test", add(2,4))
    test.messageBox()

    test.loadingScreen()

    root.mainloop()

if __name__ == '__main__':
    start()
