import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from shapes import *

class Node(Shapes):
    def __init__(self,node):
        self.window = node
    def NewNode(self):
        return node
    def ConnectTo(self):
        pass

    def TestNode(self):
        self.window.title("TestNode")
        self.window.geometry('200x200')
        newShape = Shapes(self.window)
        newShape.circle()
        self.window.mainloop()

root = Tk()
TestNode = Node(root)
TestNode.TestNode()
