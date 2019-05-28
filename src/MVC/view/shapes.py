import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from Tkinter import *

global root
class Shapes:
    def __init__(self,frame):
        self.frame = frame

    def circle(self):
        can = Canvas(self.frame, width=1024, height=620, bg="black")
        can.pack()
        can.create_oval(15,15,50,50, fill='blue')

    def lines(self):
        global root
        can = Canvas(root, width=250, height=250)
        can.pack()
        can.create_line(100,100,100,100)
    def curve_lines(self):
        pass
    def node(self):
        newNode = Node()
        return newNode
    def edge(self):
        edge = self.line()
        return edge
