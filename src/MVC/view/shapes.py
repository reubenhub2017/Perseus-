import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from tkinter import *

global root
class Shapes:
    """Modify code to specify the dimension and position """
    def __init__(self,frame):
        self.frame = frame


    def circle(self, width, height, x, y,
               bg, circlewidth,
               circleheight, circlebg):
        can = Canvas(self.frame, width=width, height=height, bg=bg)
        can.place(relx=0,rely=1,anchor=NE)
        can.pack()
        can.create_oval(circlewidth,circleheight,x,y, fill=circlebg)
        self.frame.resizable(0,0)
        self.frame.mainloop()



    """Each line should be at least 5 units long """

    def line(self, width, height, x, y,
               bg, circlewidth,
               circleheight, circlebg):
        can = Canvas(self.frame, width=width, height=height, bg=bg)
        can.place(relx=0,rely=1,anchor=NE)
        can.pack()
        can.create_line(circlewidth,circleheight,x,y, fill=circlebg)
        self.frame.resizable(0,0)
        self.frame.mainloop()

        can.create_line(100,100,100,100)
    def curve_lines(self):
        pass
