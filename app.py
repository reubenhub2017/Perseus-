import sys
sys.path.insert(0, 'ext/imports/')
from dependecies import *
from main import Controller
from shapes import Shapes
import turtle

global root

def start():
    root = tk.Tk()
    test = Controller(root)
    test.run()
    test.analytics()
    test.updateUsers()
    test.runvisuals()
    root.mainloop()

if __name__ == '__main__':
    start()
