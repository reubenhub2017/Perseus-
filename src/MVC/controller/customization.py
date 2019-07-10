from tkinter import *

class Template:
    def __init__(self, frame=None):
        pass
    def basicNodeTemplate(self,windowTitle = "Change Node Color", h=10,w=10):
        root = Tk()
        root.title(windowTitle)
        root.geometry('440x200')
        LeftFrame = Frame(root, bg="black", height=200,width=200)
        RightFrame = Frame(root, bg="tan", relief=SUNKEN, bd=5, height=200, width=300)

        LeftFrame.grid(row=0,column=0)
        RightFrame.grid(row=0,column=1)

        ChangeNodeColor = Button(LeftFrame,relief=SUNKEN, text="Change Node Color")
        ApplyBtn = Button(LeftFrame,relief=SUNKEN, text="Apply Changes")

        ChangeNodeColor.pack(fill='x',side=TOP)
        ApplyBtn.pack(fill='x',side=TOP)

        root.mainloop()
        """Need to see how to install color picker"""

    def basicEdgeTemplate(self):
        root = Tk()
        root.title(windowTitle)
        root.geometry('440x200')
        LeftFrame = Frame(root, bg="black", height=200,width=200)
        RightFrame = Frame(root, bg="tan", relief=SUNKEN, bd=5, height=200, width=300)

        LeftFrame.grid(row=0,column=0)
        RightFrame.grid(row=0,column=1)

        ChangeNodeColor = Button(LeftFrame,relief=SUNKEN, text="Change Edge Color")
        ApplyBtn = Button(LeftFrame,relief=SUNKEN, text="Apply Changes")

        ChangeNodeColor.pack(fill='x',side=TOP)
        ApplyBtn.pack(fill='x',side=TOP)

        root.mainloop()
        """Need to see how to install color picker"""
    def SignInTemplate(self):
        root = Tk()
        root.title("login ")
        root.geometry("200x200")
        UsernameLabel = Label(root, text="Username")
        PasswordLabel = Label(root, text="Password")
        Username = Entry(root)
        Password = Entry(root)
        ConfirmBtn = Button(root, text="Confirm")

        UsernameLabel.grid(row=0,column=0)
        PasswordLabel.grid(row=1,column=0)
        Username.grid(row=0,column=1)
        Password.grid(row=1, column=1)
        ConfirmBtn.grid(row=2,column=0)

        root.mainloop()


    def SignUpTemplate(self):
        root = Tk()
        root.title("Sign Up")
        root.geometry("200x200")
        UsernameLabel = Label(root, text="Username")
        PasswordLabel = Label(root, text="Password")
        Username = Entry(root)
        Password = Entry(root)
        ConfirmBtn = Button(root, text="Confirm")

        UsernameLabel.grid(row=0,column=0)
        PasswordLabel.grid(row=1,column=0)
        Username.grid(row=0,column=1)
        Password.grid(row=1, column=1)
        ConfirmBtn.grid(row=2,column=0)

        root.mainloop()

#NewNodeWindow = Template().basicNodeTemplate()
#NewSignInWindow = Template().SignInTemplate()
#NewSignUpWindow = Template().SignUpTemplate()
