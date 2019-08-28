import os
import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from shapes import *
import pip


class filemanagmentTree:

    def __init__(self,file, file_name):
        self.file = file
        self.file_name = file_name

    def write(self, data):
        #What are you writing to
        self.file = open(self.file_name,"w" )
        file.write(str(data))

    def read(self):
        self.file = open(self.file_name, "r")

    def makeDirectory(self, directory ):
        #We need to gather all the files that are in the database/cloud of the specific updateUsers
        path = '/model/' + directory
        try :
            os.mkdir(path)
        except OSError:
            print("Creation the directory failed " % directory )
        else:
            print("Successfully created the new directory" % directory)


    def makeTree(self):
        #We make the file tree to show in the ux.
        pass
