import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from tkinter import *
<<<<<<< HEAD
import random


=======

global root
>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
class Shapes:
    """Modify code to specify the dimension and position """
    def __init__(self,frame):
        self.frame = frame

<<<<<<< HEAD
=======

>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
    def circle(self, width, height, x, y,
               bg, circlewidth,
               circleheight, circlebg):
        can = Canvas(self.frame, width=width, height=height, bg=bg)
        can.place(relx=0,rely=1,anchor=NE)
        can.pack()
        can.create_oval(circlewidth,circleheight,x,y, fill=circlebg)
        self.frame.resizable(0,0)
        self.frame.mainloop()

<<<<<<< HEAD
    """Each line should be at least 5 units long """
    def line(self, x1, y1, x2, y2,
               bg, linebg):
        can = Canvas(self.frame, width=200, height=200, bg=bg)
        can.pack()
        can.create_line(x1,y1,x2,y2, fill=linebg)
=======


    """Each line should be at least 5 units long """

    def line(self, x1, y1, x2, y2,
               bg, linebg):
        can = Canvas(self.frame, width=200, height=200, bg=bg)
        #can.place(relx=0,rely=1,anchor=NE)
        can.pack()
        can.create_line(x1,y1,x2,y2, fill=linebg)
        #self.frame.resizable(0,0)
>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
        self.frame.mainloop()

        #can.create_line(0,0,100,100)
    def curve_lines(self):
        pass
