import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from shapes import *

class Node(Shapes):
    def __init__(self,node):
        self.window = node
    """Calls function that makes the new """

    def Node(self, frame, width, height, x,y, NodeColor, BgNodeCanvas):
        node = Shapes(frame)
        node.circle(width,height,x,y,BgNodeCanvas,NodeColor)

    def Edge(self, frame, x1,y1,x2,y2, EdgeColor, BgEdgeColor):
        node = Shapes(frame)
        node.line(x1,y1,x2,y2,EdgeColor,BgEdgeColor)

    def childObject(self,frame):
        parent = self.parent()
        RightChild = self.Edge(self.frame,  )
        LeftChild = Shapes(frame)

        parent.circle()



    def parentObject(self, Node, Edge):
        pass

    def childObject(self, Node, Edge):
        "Figure out the position of the parent node, rightChild, leftChild"
        """Circle parameters is as follows
             width, height, x, y,
                       bg, circlewidth,
                       circleheight, circlebg

         """
         """ line parameters is as follows
            x1, y1, x2, y2,
                       bg, circlewidth,
                       circleheight, circlebg

         """
        parent = self.circle()
        RightChild = self.line(frame, )
        LeftChild = self.line(frame, )




    """ Call shape class to implement sizing of the window"""
    def TestNode(self):
        self.window.title("TestNode")
        self.window.geometry('200x200')
        newShape = Shapes(self.window)
        newShape.circle()
        self.window.mainloop()

root = Tk()
TestNode = Node(root)
TestNode.TestNode()
