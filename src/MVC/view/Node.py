import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from shapes import *
import math
import random

class Node(Shapes):
    def __init__(self,node):
        self.window = node
    """Calls function that makes the new """

    def node(self, width, height, x,y, NodeColor, BgNodeCanvas):
        node = Shapes(self.window)
        node.circle(width,height,x,y,BgNodeCanvas,250,250,NodeColor)

    def Edge(self, frame, x1,y1,x2,y2, EdgeColor, BgEdgeColor):
        node = Shapes(frame)
        node.line(x1,y1,x2,y2,EdgeColor,BgEdgeColor)

    """

    def childObject(self,frame):
            Figure out the position of the parent node, rightChild, leftChild"
            Circle parameters is as follows
                 width, height, x, y,
                           bg, circlewidth,
                           circleheight, circlebg


        line parameters is as follows
                x1, y1, x2, y2,
                           bg, circlewidth,
                           circleheight, circlebg



        #parent = self.parent()
        #RightChildren = self.Edge(self.frame, parentNode)
        #LeftChildren = Shapes(self.frame, parentNode)


    def parentObject(self, Node, Edge):
        leftChildren = None
        RightChildren = None
        CurrentNode = None
        Node = None
        #Insert the new Node if it's empty
        while True:
            if Node == None:
                Node.append("root")
                CurrentNode = Node
            else:
                Node.leftChild = self.leftChild
                self.leftChild = node

            """

    def NodeAndEdge(self):
        root = Tk()
        #w = winfo_screenwidth
        #h  = winfo_screenheight
        newSpace = Canvas(root, height=400, width=400, background='white')
        newSpace.pack()
        #CurrentNode = parentNode
        Node = newSpace.create_oval(100,100,250,240, fill='black')
        #Node.grid(row=0, column=1)
        leftEdge = newSpace.create_line(200,200,350,350,fill='black')
        rightEdge = newSpace.create_line(150,200,0,350, fill='black')
        root.mainloop()

    """Got it to work (idea wise)"""
    """ New problem each node within the edge """
    """Solved the problem each node withint the edge """
    def threesixtyNodeAndEdge(self):
        root = Tk()
        newSpace = Canvas(root, height=400, width=400, background='white')
        newSpace.pack()
        colors = ['blue', 'black', 'red', 'yellow', 'green','grey', 'orange',
                  'pink']

        x1 = 225
        y1 = 225

        for i in range(0,400,100):
            for j in range(0,400,100):
                newNumber = random.randint(0,len(colors)-1)
                newSpace.create_line(x1,y1,i+5,j+5,fill=colors[newNumber])
                #newSpace.create_line(x1,y1,x2,y2,fill=colors[newNumber])
                newSpace.create_oval(i-5,j+5,i+5,j+5,fill=colors[newNumber])
                print((x1,y1),(i,j), colors[newNumber])
        Node = newSpace.create_oval(200,200, 250,250, fill='black')
        #newSpace.create_line(x1,y1,400,225)
        #newSpace.create_line(x1,y1,225,0)
        #newSpace.create_line(x1,y1,225,400)
        #newSpace.create_line(x1,y1,0,225)
        root.mainloop()

class TestNode:
    def __init__(self, Node=None, leftChild=None, rightChild=None):
        self.val = Node
        self.leftChild = leftChild
        self.rightChild = rightChild

    def insertLeft(self, child):
        if self.leftChild is None:
            self.leftChild = child
        else:
            child.left = self.leftChild
            self.leftChild = child

    def insertRight(self,child):
        if self.rightChild is None:
            self.rightChild = child
        else:
            child.rightChild = self.rightChild
            self.rightChild = child



root = TestNode()
root.val = "a"
print(root.leftChild, root.rightChild, root.val)
