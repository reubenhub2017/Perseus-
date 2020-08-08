import sys
sys.path.insert(0,'./ext/imports/')
from dependecies import *
<<<<<<< HEAD

#from shapes import *
import time
from windowfuncs import *
#from gui import *
=======
import time
from windowfuncs import *
>>>>>>> 73be496... Finish
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk
from PIL import Image
<<<<<<< HEAD
#from Node import Node
=======
>>>>>>> 73be496... Finish
import os
import random

class Controller(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        #self.winfo_toplevel().title("Perseus 1.0.0")


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
        #newFrame.config(bg="black")
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
=======
    def signup(self):
        print("Runnning signin option ")
        signinWindow = Tk()
        signinFrame = Frame(siginWindow, height=200, width=200)

        EmailLabel = Label(signinWindow, text="Email")
        PasswordLabel = Label(signinWindow, text = "Password")

        Email = Entry(siginFrame, width=10)
        Password = Entry(siginFrame, width=10)
        SubmitBtn = Button(siginFrame, width=10, text="Submit")

        EmailLabel.grid(row=0,column=0)
        PasswordLabel.grid(row=1,column=0)

        Email.grid(row=0,column=1)
        Passsword.grid(row=1,column=1)
        SubmitBtn.grid(row=2, column=0)



    def runvisuals(self):
        #Have to make user_id set in the sessions

        #GOOGLE APIS
        try:
            from googlesearch import search
        except ImportError:
                print("We could not find it at all!")
        query = "Instagram"
        for i in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(i)
        self.winfo_toplevel().title("Perseus 1.1.0")
        #self.parent.geometry('2000x900')
        self.parent.configure(background="grey")
        #sideFrame = Frame(self.parent,height=1500,width=100, relief=SUNKEN)
        #sideFrame.grid(row=0,column=0, sticky='w')
        newFrame = Frame(self.parent, height=1500,width=150, relief=SUNKEN)
        newFrame.grid(row=0,column=1, sticky='ne',padx=(0,10))

        e = Entry(newFrame, width=150);
        e.grid(row=0,column=0,padx=(0,10))

        def Search():
            try:
                from googlesearch import search
            except ImportError:
                    print("We could not find it at all!")
            query = e.get()
            r = 2
            for i in search(e.get(), tld="co.in", num=10, stop=10, pause=2):
                LabelResult = Label(newFrame, text=i)
                LabelResult.grid(row=r, column=0, sticky='nw', padx=(0,10))
                ButtonOptions = Button(newFrame, text="Save", command=lambda:SaveLink(e.get(),i, 1))
                ButtonOptions.grid(row=r, column=2, sticky='nw', padx=(0,10))
                r = r + 1


        searchBtn = Button(newFrame,text="Search", command=Search)
        searchBtn.grid(row=1,column=0, sticky='nw',padx=(0,10))

        #newFrame.grid(row=2,column=0)
        #yscrolbar.configure(command=newSpace.yview)
        #xscrollbar.configure(command=newSpace.xview)

        """ Making the Side window with File Tree
>>>>>>> 73be496... Finish
        p = ttk.Panedwindow(sideFrame, orient=VERTICAL)
        # first pane, which would get widgets gridded into it:
        fp = ttk.Labelframe(p, text='File Management', width=200, height=720)
        p.add(fp)
        p.pack(fill=BOTH, expand=1)
        #Tab view
        n = ttk.Notebook(fp)
        f1 = ttk.Frame(n, width=200, height=720)   # first page, which would get widgets gridded into it
<<<<<<< HEAD
        f2 = ttk.Frame(n, width=200, height=720)
        # second page
        n.add(f1, text='Local Files')
        n.add(f2, text='Online Files')

        n.pack(fill="both", expand=1)

        #Toolbar view
        #toolbar = Frame(frame, style='My.TFrame', height=720, width=25, relief=SUNKEN)
        #canvasToolbar = Canvas(toolbar, bg='blue',height=720, width=20)
        #toolbar.pack(side=RIGHT, fill=BOTH, expand=1)
        #toolbar.place(relx=1,rely=0,anchor=NE)


        #buttons on the toolbar
        """for i in range(15):
            button = Button(toolbar, height=1)
            button.pack(side=TOP, fill=BOTH, expand=1)
        """

        """Label"""
        ttk.Label(f1, text="Hierachical Treeview").pack()
        """Treeview"""
        treeview=ttk.Treeview(f1)
        treeview.pack()
        """Treeview items"""
=======

        # second page
        n.add(f1, text='Saved Files')

        n.pack(fill="both", expand=1)
        #Toolbar view
        toolbar = Frame(newFrame, style='My.TFrame', height=720, width=25, relief=SUNKEN)
        canvasToolbar = Canvas(toolbar, bg='blue',height=720, width=20)
        toolbar.pack(side=RIGHT, fill=BOTH, expand=1)
        toolbar.place(relx=1,rely=0,anchor=NE)"




        #buttons on the toolbar
        #options = ["Search", "Save", "Delete"]
        #for i in options:
        #    button = Button(toolbar, text=i)
        #    button.pack(side=TOP, fill=BOTH, expand=1)"""

        """#Label
        ttk.Label(f1, text="Hierachical Treeview").pack()
        #Treeview
        treeview=ttk.Treeview(f1)
        treeview.pack()
        #Treeview items
>>>>>>> 73be496... Finish
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
<<<<<<< HEAD
        treeview.move('item3','item1','end')
        """Making the compression Rate Label """
        #compressionRateLabel = Label(frame, text="Compression Rate : ",   height=1, width=1648, bd=1, bg="grey")
        #compressionRateLabel.place(relx=0, rely= 1, anchor=S)
        #TestShape = Shapes(frame)
        #TestShape.circle()
        """ Making the menu bar for the application"""
        menubar = Menu(self.parent)
        """Making the file tree """
        localFileTree = Treeview(f1)
=======
        treeview.move('item3','item1','end')"""



        """Making the compression Rate Label """

        #ompressionRateLabel = Label(Shapes.frame, text="Compression Rate : ", width=1648, bd=1, bg="grey")
        #compressionRateLabel.place(relx=0, rely= 1, anchor=S)
        #TestShape = Shapes(newFrame)
        #TestShape.circle(10,10,100,100,"red",)
        """ Making the menu bar for the application"""
        menubar = Menu(self.parent)
        """Making the file tree """
        #localFileTree = Treeview(f1)
>>>>>>> 73be496... Finish
        """Making the compression Rate Label """
        #compressionRateLabel = Label(frame, text="Compression Rate : ",   height=1, width=1648, bd=1, bg="grey")
        #compressionRateLabel.place(relx=0, rely= 1, anchor=S)

        #TestShape = Shapes(frame)
        #TestShape.circle()
        """ Making the menu bar for the application"""
        menubar = Menu(self.parent)
        """ create a pulldown menu, and add it to the menu bar"""
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=open)
        filemenu.add_command(label="Save", command=save)
        filemenu.add_separator()
<<<<<<< HEAD
        filemenu.add_command(label="Exit", command=Fram)
=======
        filemenu.add_command(label="Exit", command=Frame)
>>>>>>> 73be496... Finish
        menubar.add_cascade(label="File", menu=filemenu)
        """create more pulldown menus"""
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=cut)
        editmenu.add_command(label="Copy", command=paste)
        editmenu.add_command(label="Paste", command=paste)
        menubar.add_cascade(label="Edit", menu=editmenu)
<<<<<<< HEAD
        """Data pulldown"""
        datamenu = Menu(menubar, tearoff=0)
        datamenu.add_command(label="Edit compression rate", command=Edit_compressionRate)
        datamenu.add_command(label="Statistical view", command=Statistical_view)
        datamenu.add_command(label="Formula input", command=Formula_input)
        menubar.add_cascade(label="Data analytics", menu=datamenu)
        """user Data pulldown"""
        profileMenu = Menu(menubar, tearoff=0)
        profileMenu.add_command(label="Sign in", command=signin)
        profileMenu.add_command(label="Sign out", command=signout)
        profileMenu.add_command(label="Send Data", command=SendDataToCloud)
        profileMenu.add_command(label="Retrieve partial Data", command=RetrieveDataFromCloud)
        menubar.add_cascade(label="Account", menu=profileMenu)

        """Toggle File Tree"""
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
=======

        """user Data pulldown"""
        profileMenu = Menu(menubar, tearoff=0)
        profileMenu.add_command(label="Sign up!", command=signup)
        profileMenu.add_command(label="Sign in!", command=signin)
        profileMenu.add_command(label="Sign out", command=signout)
        #profileMenu.add_command(label="Retrieve Saved Links", command=RetrieveLinks)
        menubar.add_cascade(label="Account", menu=profileMenu)


>>>>>>> 73be496... Finish
        #Info pulldown
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=About)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        self.parent.config(menu=menubar)
<<<<<<< HEAD
        #frame.pack()
        self.parent.mainloop()

        # display the menu
        self.parent.config(menu=menubar)
        frame.pack()
        newroot.mainloop()
=======

        self.parent.mainloop()

        # display the menu
        #self.parent.config(menu=menubar)



def SaveLink(link_text,link, user_id):

    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='?Drogba96',
                                             database='Perseus',
                                             auth_plugin='mysql_native_password')
        if connection.is_connected():
            curA = connection.cursor(buffered=True)
            id = curA.lastrowid
            insert = 'INSERT INTO links (id, link_text, link, user_id_corresponding_to_link) VALUES (%s, %s, %s, %s)'
            curA.execute(insert, (float(id), link_text, link, user_id))
            connection.commit()
            curA.close()
            print("Successful Saved Link on MYSQL")
    except Exception as e:
        print("Error while connecting to MySQL", e)
>>>>>>> 73be496... Finish
