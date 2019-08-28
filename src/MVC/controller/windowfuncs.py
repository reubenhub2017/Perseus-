import os
import sys
#from model import *
sys.path.insert(0,'./ext/imports/')
from dependecies import *

from tkinter import *
import time


""" Window view functions """
def open():
    pass
def save():
    pass
def Exit():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass
""" Computation of Data"""
def Edit_compressionRate():

    EditCompressionWindow = Tk()
    EditCompressionWindow.title("Edit_compressionRate")
    Title = Label(EditCompressionWindow, text="Edit Comppression Algorithm")
    Title.pack()
    paragraph = Label(EditCompressionWindow, text= "Choose another Algorithm to use")
    paragraph.pack()
    SelectorOption =  Listbox(EditCompressionWindow)
    SelectorOption.pack()
    SelectorOption.insert(END, "Compression Rates")
    for item in ["HuffmanCompression", "lowerDataAlgorithm", "LZWCompression", "RLECompression", "Flate_deflateCompression"]:
        SelectorOption.insert(END, item)

    ApplyButton = Button(EditCompressionWindow, text= "Apply Changes")
    ApplyButton.pack()
    EditCompressionWindow.mainloop()


def Statistical_view():
    pass
def Formula_input():
    pass
def Data_analytics():
    pass
"""client authentication """
def signin():

    signinloop = Tk()
    signinloop.title("Sign In")
    UsernameLabel = Label(signinloop, text="Username")
    UsernameLabel.grid(row=0,column=0)

    UsernameEntry = Entry(signinloop)
    UsernameEntry.grid(row=0,column=1)

    PasswordLabel = Label(signinloop, text="Password")
    PasswordLabel.grid(row=1,column=0)

    PasswordEntry = Entry(signinloop)
    PasswordEntry.grid(row=1,column=1)

    SubmitBtn = Button(signinloop, text="Submit")
    SubmitBtn.grid(row=2,column=0)


    signinloop.mainloop()
def signout():
    confirmation = Tk()
    confirmation.title("Hate to see you go!")
    label_header = Label(confirmation, text="Hope you found everything you needed")
    label_compression = Label(confirmation, text="Compressioned from today 560kb")
    label_btn = Button(confirmation, text="End Application")
    label_header.pack()
    label_compression.pack()
    label_btn.pack()
    confirmation.mainloop()

    pass
def signout():
    pass

""" Data Management """
#Hopefully to end where
def SendDataToCloud():
    pass
def RetrieveDataFromCloud():

    RetrieveDataFromCloudWindow = Tk()
    RetrieveDataFromCloudWindow.title("Retrieving Data")
    RetrieveDataFromCloudLabel = Label(RetrieveDataFromCloudWindow, text="Retrieving data from Cloud")
    RetrieveDataFromCloudLabel.pack()
    progress_bar = ttk.Progressbar(RetrieveDataFromCloudWindow, orient= 'horizontal', length=300,mode="determinate")
    progress_bar.config(mode='determinate',maximum=100, value=5)
    progress_bar.pack(side="bottom")
    #label = Label(master=RetrieveDataFromCloud,image=imageFile).pack()
    progress_bar["maximum"] = 100
    for i in range(101):
        time.sleep(0.05)
        progress_bar["value"] = i
        progress_bar.update()
        progress_bar["value"] = 0
    progress_bar.start()
    #RetrieveDataFromCloudLabel.pack()
    RetrieveDataFromCloudWindow.mainloop()

def ToggleFileTree():
    pass
def ToggleCompressionRate():
    pass
def ToggleSearch():
    pass
def Help():
    pass
def About():
    pass
""" Window functions """
def ZoomIn():
    pass
def ZoomOut():
    pass
def MinimizeWin():
    pass
def MaximumWin():
    pass
def ErrorMessageWin():
    pass

def clickableCanvas(self):
        def callback(self,event):
            print("clicked at, ", event.x, event.y)

        root = Tk()
        clickableFrame = Canvas(root,width=100, height=100, bg='black')
        clickableFrame.bind("<Button-1>", callback)
        clickableFrame.pack()
        root.mainloop()
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

    """Make a new window for specific functions """

    def newWindow(self, height, width, positionx, positiony, title,  f = lambda t :t() ):
        screen = Tk()
        screen.title(title)
        screen.geometry('%dx%d+%d+%d' % (width, height, positionx, positiony))
        f(screen)
