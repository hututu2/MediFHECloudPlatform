# coding=utf-8
# import libs
import sys
from os.path import abspath, dirname

sys.path.append(abspath(dirname(__file__)))
import app_cmd
import app_sty
from lib import Fun
import tkinter
from tkinter import *
import tkinter.ttk
import tkinter.font


# Add your Varial Here: (Keep This Line of comments)
# Define UI Class



# Create the root of Kinter
if __name__ == "__main__":
    root = tkinter.Tk()
    MyDlg = app(root)
    root.mainloop()
