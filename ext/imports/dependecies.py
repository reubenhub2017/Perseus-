import math
import sys
import socket
#import tensorflow

sys.path.insert(0, './src/MVC/controller/')
sys.path.insert(0,'./src/MVC/view/')
sys.path.insert(0,'./src/MVC/model/')

from tkinter import *
from tkinter.ttk import *
import mysql.connector
from mysql.connector import Error

#from tkcolorpicker import askcolor
from customization import Template
from PIL import ImageTk
from PIL import Image
