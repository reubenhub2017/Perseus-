import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from shapes import *

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
