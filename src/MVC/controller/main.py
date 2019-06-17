import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
from shapes import *
import time
from tkinter import *
from PIL import Image, ImageTk



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
        self.root.title("Perseus 1.0.0")
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

        sideFrame = Frame(self.root, bg="grey", height=720,width=200, bd=4, relief=SUNKEN)
        sideFrame.pack(side=LEFT)

        frame = Frame(self.root, bg='black', bd=2, height=720,width=1648, relief=SUNKEN)
        frame.pack(side=RIGHT)


        p = ttk.Panedwindow(sideFrame, orient=VERTICAL)
        # first pane, which would get widgets gridded into it:
        f1 = ttk.Labelframe(p, text='File Management', width=200, height=720)
        p.add(f1)
        p.pack(fill=BOTH, expand=1)

        #Tab view
        n = ttk.Notebook(f1)
        f1 = ttk.Frame(n, width=200, height=720)   # first page, which would get widgets gridded into it
        f2 = ttk.Frame(n, width=200, height=720)   # second page
        n.add(f1, text='Local Files')
        n.add(f2, text='Online Files')
        n.pack(fill=BOTH, expand=1)

        #Toolbar view
        toolbar = Frame(frame, bg='grey', bd=3, height=720, width=25, relief=SUNKEN)
        #canvasToolbar = Canvas(toolbar, bg='blue',height=720, width=20)
        #toolbar.pack(side=RIGHT, fill=BOTH, expand=1)
        toolbar.place(relx=1,rely=0,anchor=NE)

        #buttons on the toolbar
        for i in range(15):
            button = Button(toolbar, height=1)
            button.pack(side=TOP, fill=BOTH, expand=1)


        """Making the file tree """
        localFileTree = Treeview(f1)


        """Making the compression Rate Label """
        compressionRateLabel = Label(frame, text="Compression Rate : ",   height=1, width=1648, bd=1, bg="grey")
        compressionRateLabel.place(relx=0, rely= 1, anchor=S)

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

    """Make a new window for specific functions """

    def newWindow(self, height, width, positionx, positiony, t):
        screen = Tk()
        screen.title = t
        screen.geometry('%dx%d+%d+%d' % (width, height, positionx, positiony))
        return screen

    def SplashScreen(self):
        root = Tk()

        #Making the Window
        screenheight = (root.winfo_screenwidth() - 720)//2
        screenwidth = (root.winfo_screenheight() - 720)//2

        path = Image.open("load.png")

        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        photo= ImageTk.PhotoImage(path)

        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = Label(root, image=photo)
        panel.image = photo
        panel.pack()


        root.overrideredirect(True)
        progressbar = Progressbar(orient=HORIZONTAL, length=10000, mode='determinate')
        progressbar.pack(side='bottom')
        progressbar.start()
        root.after(6010,root.destroy)
        root.mainloop()
    "Having problems with PIL"

    def messageBox(self):
        root = Tk()
        #root.wm_attributes('-fullscreen','true')
        root.attributes('-alpha', 1)
        new_top = Toplevel(root,width=150)
        new_top.overrideredirect(True)
        root.geometry('200x200')
        #root.focus_force()

        root.title("Say Hello")
        label = Label(root, text="Hello World")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        button = Button(root, text="OK", command=lambda: root.destroy())
        button.pack(side="bottom", fill="none", expand=True)
        root.mainloop()

    def loadingScreen(self):
        screen = self.newWindow(100,100,0,0,"Loading screen")
        self.progress_bar = Progressbar(screen, orient= 'horizontal', length=300,mode="determinate")
        self.progress_bar.config(mode='determinate',maximum=100, value=5)
        self.progress_bar.pack()
        self.progress_bar["maximum"] = 100
        for i in range(101):
            time.sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()
            self.progress_bar["value"] = 0
        self.progress_bar.start()
