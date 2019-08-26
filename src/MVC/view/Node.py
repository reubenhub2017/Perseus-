#import sys
#sys.path.insert(0,'./ext/imports/')
#from dependecies import *
#from shapes import *
import math
import random
"""This is is how the data structure of the perseus is going to be represented as a Tree"""
class Node:
    def __init__(self):
        self.root = dict()

    def addNode(self):
        newNode = random.randrange(11)
        newNode2 = random.randrange(10)
        if self.root.get(newNode) == None:
            self.root[newNode] = []
        else:
            self.root[newNode].append(newNode2)


    def addEdge(self, parent):
        newFilePath = random.randrange(100)
        #Gotta check all the values with the keys(nodes)
        for key, value in self.root.items():
            for i in range(len(value)):
                if self.root[key][i] == parent:
                    self.root[key].append("0000")

    def printTree(self):
        print(self.root)

newNode = Node()
for i in range(50):
    newNode.addNode()
newNode.addEdge(5)
newNode.printTree()


def threesixtyNodeAndEdge():
    """Making the Node with Edges Testing """
    colors = ['blue', 'black', 'red', 'yellow', 'green','grey', 'orange',
              'pink']
    x1 = 225
    y1 = 225
    for i in range(0,400,100):
        for j in range(0,400,100):
            newNumber = random.randint(0,len(colors)-1)
            newSpace.create_line(x1,y1,i+5,j+5,fill=colors[newNumber])
            newSpace.create_line(x1+100,y1+100,i+100,j+100,fill=colors[newNumber-1])


    newSpace.create_oval(200,200, 250,250, fill='white')
    newSpace.create_oval(300,300, 350,350, fill='white')
