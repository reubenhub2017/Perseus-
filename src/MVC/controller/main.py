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
        self.root.geometry('2048x720')

        testCanvas = Frame(self.root, bg="grey", height=720, width=2048, bd=4, relief=SUNKEN)
        testCanvas.grid(row=1, column=2)
        testCanvas.pack()
        frame = Frame(self.root, bg='black',height=720, width=2048, bd=2, relief=SUNKEN)
        frame.grid(row=0,column=0)

        nb = ttk.Notebook(testCanvas)
        nb.grid(row=0, column=2,columnspan=40,rowspan=39,sticky='NESW')

        page1 = ttk.Frame(nb)
        page2 = ttk.Frame(nb)

        nb.add(page1, text="Tab1 ")
        nb.add(page2, text="Tab2 ")

        nb.pack(expand=1, fill="both")

        #TestShape = Shapes(frame)
        #TestShape.circle()


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

        datamenu = Menu(menubar, tearoff=0)
        datamenu.add_command(label="Edit compression rate", command=self.hello)
        datamenu.add_command(label="Statistical view", command=self.hello)
        datamenu.add_command(label="Formula input", command=self.hello)
        menubar.add_cascade(label="Data analytics", menu=datamenu)

        profileMenu = Menu(menubar, tearoff=0)
        profileMenu.add_command(label="Sign in", command=self.hello)
        profileMenu.add_command(label="Sign out", command=self.hello)
        profileMenu.add_command(label="Send Data", command=self.hello)
        profileMenu.add_command(label="Retrieve partial Data", command=self.hello)
        menubar.add_cascade(label="Account", menu=profileMenu)


        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Toggle File Tree", command=self.hello)
        viewmenu.add_command(label="Toggle Compression Rate ",command=self.hello)
        viewmenu.add_command(label="Toggle Search", command=self.hello)
        menubar.add_cascade(label="View", menu=viewmenu)

        Windowmenu = Menu(menubar, tearoff=0)
        Windowmenu.add_command(label= "Zooom in", command=self.hello)
        Windowmenu.add_command(label="Zoom out", command=self.hello)
        Windowmenu.add_command(label="Minimize", command=self.hello)
        menubar.add_cascade(label="Window", menu=Windowmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.hello)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        self.root.config(menu=menubar)
        frame.pack()
        #testCanvas.pack()
