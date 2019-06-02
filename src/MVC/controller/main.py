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
        # get screen width and height
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        w = 2048
        h = 720

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.geometry('2048x720')

        sideFrame = Frame(self.root, bg="grey", height=720,width=400, bd=4, relief=SUNKEN)
        sideFrame.pack(side=LEFT)

        frame = Frame(self.root, bg='black', bd=2, height=720,width=1648, relief=SUNKEN)
        frame.pack(side=RIGHT)






        p = ttk.Panedwindow(sideFrame, orient=VERTICAL)
        # first pane, which would get widgets gridded into it:
        f1 = ttk.Labelframe(p, text='File Management', width=400, height=720)
        p.add(f1)
        p.pack(fill=BOTH, expand=1)

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
