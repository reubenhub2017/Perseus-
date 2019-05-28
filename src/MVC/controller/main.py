import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from shapes import *
class Controller:
    def __init__(self,root):
        self.root = root

    def run(self):
        print("Starting program now ")
        print("Installing on the drive...")
        print("Running...")

    def analytics(self):
        print("Updating analytics")
        print("Running analytics")
        print("Running.....")
        print("\n")

    def updateUsers(self):
        print("Updating user data")
        print("Adding Folders")
        print("Adding to Perseus")

    def hello(self):
        pass

    def runvisuals(self):
        self.root.title("Perseus")
        self.root.geometry('1024x720')
        frame = tk.Frame(self.root, bg="black", height=310, width=1024)
        TestShape = Shapes(frame)
        TestShape.circle()

        """ Making the menu bar for the application"""
        menubar = Menu(self.root)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.hello)
        filemenu.add_command(label="Save", command=self.hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # create more pulldown menus
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.hello)
        editmenu.add_command(label="Copy", command=self.hello)
        editmenu.add_command(label="Paste", command=self.hello)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.hello)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        self.root.config(menu=menubar)
        frame.pack()
