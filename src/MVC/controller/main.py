import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
<<<<<<< HEAD
#from shapes import *
import time
from windowfuncs import *
#from gui import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
#from Node import Node
import os
import random

class Controller(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        #self.winfo_toplevel().title("Perseus 1.0.0")
=======
from shapes import *
import time
from windowfuncs import *
from gui import *
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk
from PIL import Image
from Node import Node
import os

class Controller(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa

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

<<<<<<< HEAD
    def runvisuals(self):
        self.winfo_toplevel().title("Perseus 1.1.0")
        self.parent.geometry('1200x900')
        w = 2048
        h = 720
        sideFrame = Frame(self.parent,height=720,width=100, relief=SUNKEN)
        sideFrame.grid(row=0,column=0, sticky='w')
        newFrame = Frame(self.parent, height=720,width=2100, relief=SUNKEN)
        newFrame.config(bg="black")
        newFrame.grid(row=0,column=1, sticky='ne',padx=(0,500))
        """Scrollbar for the Frame of the Canvas """
        yscrolbar = Scrollbar(newFrame, orient='vertical')
        xscrollbar = Scrollbar(newFrame, orient='horizontal')
        yscrolbar.grid(row=0,column=1, sticky='ns')
        xscrollbar.grid(row=1,column=0, sticky='we')
        """Canvas the new Frame """
        newSpace = Canvas(newFrame,width=900,height=610,yscrollcommand = yscrolbar.set, xscrollcommand=xscrollbar.set, background='black')
        newSpace.grid(row=0,column=0, sticky='nswe')
        newSpace["scrollregion"] = (50,50,1000,1000)
        #newSpace.grid(row=0,column=0)
        yscrolbar.configure(command=newSpace.yview)
        xscrollbar.configure(command=newSpace.xview)
        """Making the Side window with File Tree """
        p = ttk.Panedwindow(sideFrame, orient=VERTICAL)
        # first pane, which would get widgets gridded into it:
        fp = ttk.Labelframe(p, text='File Management', width=200, height=720)
        p.add(fp)
        p.pack(fill=BOTH, expand=1)
        #Tab view
        n = ttk.Notebook(fp)
        f1 = ttk.Frame(n, width=200, height=720)   # first page, which would get widgets gridded into it
        f2 = ttk.Frame(n, width=200, height=720)
        # second page
        n.add(f1, text='Local Files')
        n.add(f2, text='Online Files')

        n.pack(fill="both", expand=1)
=======
    def helloWorld(self):
        print("Hello World")

    "Zooming options for the window "
    def ZoomFunction(self, Frame):
        pass

    def addTest(a, b)->int:
        return a + b

    def runvisuals(self):
        newroot = tk.Tk()

        #newroot.title = "Perseus 1.0.0"
        # get screen width and height
        ws = newroot.winfo_screenwidth() # width of the screen
        hs = newroot.winfo_screenheight() # height of the screen

        w = 2048
        h = 720

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen
        # and where it is placed
        newroot.geometry('%dx%d+%d+%d' % (w, h, x, y))
        newroot.geometry('2048x720')

        gui_style = ttk.Style()
        gui_style.configure('My.TFrame', background='grey', )

        sideFrame = Frame(newroot, style='My.TFrame',height=720,width=200, relief=SUNKEN)
        sideFrame.pack(side=LEFT)

    """ A Few bugs that have to be worked ZoomOut
    1. Zoom inside the main window
    2. Node inside the left window.
    3. Combining everything
        """

        frame = Frame(newroot, style='My.TFrame' , height=720,width=1648, relief=SUNKEN)
        #path = 'logo.png'
        #Zoom_Advanced(frame.pack(side=RIGHT), path=path)
        newNode = Node(frame)
        newNode.threesixtyNodeAndEdge()
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
        toolbar = Frame(frame, style='My.TFrame', height=720, width=25, relief=SUNKEN)
        #canvasToolbar = Canvas(toolbar, bg='blue',height=720, width=20)
        #toolbar.pack(side=RIGHT, fill=BOTH, expand=1)
        toolbar.place(relx=1,rely=0,anchor=NE)
>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa

        #buttons on the toolbar
        """for i in range(15):
            button = Button(toolbar, height=1)
            button.pack(side=TOP, fill=BOTH, expand=1)
        """
<<<<<<< HEAD
        #Label
        ttk.Label(f1, text="Hierachical Treeview").pack()
        #Treeview
        treeview=ttk.Treeview(f1)
        treeview.pack()
        #Treeview items
        treeview.insert('','0','item1',text='Parent tree')
        treeview.insert('','1','item2',text='1st Child')
        treeview.insert('','end','item3',text='2nd Child')
        treeview.insert('item2','end','A',text='A')
        treeview.insert('item2','end','B',text='B')
        treeview.insert('item2','end','C',text='C')
        treeview.insert('item3','end','D',text='D')
        treeview.insert('item3','end','E',text='E')
        treeview.insert('item3','end','F',text='F')
        treeview.move('item2','item1','end')
        treeview.move('item3','item1','end')
        """Making the compression Rate Label """
        #compressionRateLabel = Label(frame, text="Compression Rate : ",   height=1, width=1648, bd=1, bg="grey")
        #compressionRateLabel.place(relx=0, rely= 1, anchor=S)
        #TestShape = Shapes(frame)
        #TestShape.circle()
        """ Making the menu bar for the application"""
        menubar = Menu(self.parent)
=======


        """Making the file tree """
        localFileTree = Treeview(f1)


        """Making the compression Rate Label """
        #compressionRateLabel = Label(frame, text="Compression Rate : ",   height=1, width=1648, bd=1, bg="grey")
        #compressionRateLabel.place(relx=0, rely= 1, anchor=S)

        #TestShape = Shapes(frame)
        #TestShape.circle()


        """ Making the menu bar for the application"""
        menubar = Menu(newroot)

>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=open)
        filemenu.add_command(label="Save", command=save)
        filemenu.add_separator()
        #filemenu.add_command(label="Exit", command=Fram)
        menubar.add_cascade(label="File", menu=filemenu)
<<<<<<< HEAD
=======

>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
        # create more pulldown menus
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=cut)
        editmenu.add_command(label="Copy", command=paste)
        editmenu.add_command(label="Paste", command=paste)
        menubar.add_cascade(label="Edit", menu=editmenu)
<<<<<<< HEAD
=======

>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
        #Data pulldown
        datamenu = Menu(menubar, tearoff=0)
        datamenu.add_command(label="Edit compression rate", command=Edit_compressionRate)
        datamenu.add_command(label="Statistical view", command=Statistical_view)
        datamenu.add_command(label="Formula input", command=Formula_input)
        menubar.add_cascade(label="Data analytics", menu=datamenu)
        #user Data pulldown
        profileMenu = Menu(menubar, tearoff=0)
        profileMenu.add_command(label="Sign in", command=signin)
        profileMenu.add_command(label="Sign out", command=signout)
        profileMenu.add_command(label="Send Data", command=SendDataToCloud)
        profileMenu.add_command(label="Retrieve partial Data", command=RetrieveDataFromCloud)
        menubar.add_cascade(label="Account", menu=profileMenu)
<<<<<<< HEAD
=======

>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
        #Toggle File Tree
        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Toggle File Tree", command=ToggleFileTree)
        viewmenu.add_command(label="Toggle Compression Rate ",command=ToggleCompressionRate)
        viewmenu.add_command(label="Toggle Search", command=ToggleSearch)
        menubar.add_cascade(label="View", menu=viewmenu)
        #Viewpoints pulldown
        Windowmenu = Menu(menubar, tearoff=0)
        Windowmenu.add_command(label= "Zooom in", command=ZoomIn)
        Windowmenu.add_command(label="Zoom out", command=ZoomOut)
        Windowmenu.add_command(label="Minimize", command=MinimizeWin)
        menubar.add_cascade(label="Window", menu=Windowmenu)
        #Info pulldown
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=About)
        menubar.add_cascade(label="Help", menu=helpmenu)
<<<<<<< HEAD
        # display the menu
        self.parent.config(menu=menubar)
        #frame.pack()
        self.parent.mainloop()
=======

        # display the menu
        newroot.config(menu=menubar)
        frame.pack()
        newroot.mainloop()




    """Make a new window for specific functions """

    def newWindow(self, height, width, positionx, positiony, title,  f = lambda t :t() ):
        screen = Tk()
        screen.title = title
        screen.geometry('%dx%d+%d+%d' % (width, height, positionx, positiony))
        f(screen)



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


    def clickableCanvas(self):
        def callback(self,event):
            print("clicked at, ", event.x, event.y)

        root = Tk()
        clickableFrame = Canvas(root,width=100, height=100, bg='black')
        clickableFrame.bind("<Button-1>", callback)
        clickableFrame.pack()
        root.mainloop()
>>>>>>> 3433180bc4a6ee25d05d761463e04e9c74a8edaa
