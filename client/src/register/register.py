#coding=utf-8
#import libs 
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import register_cmd
import register_sty
from lib import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  register:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = register_sty.SetupStyle()
        if isTKroot == True:
            root.title("注册")
            Fun.CenterDlg(uiName,root,658,489)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 658,height = 489)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="输入口令：",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Label_2.place(x = 103,y = 106,width = 144,height = 48)#lock
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','')
        Entry_3 = tkinter.Entry(Form_1,textvariable=Entry_3_Variable)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Entry_3.place(x = 310,y = 106,width = 224,height = 48)#lock
        Entry_3.configure(bg = "#7dffff")
        Entry_3.configure(relief = "sunken")
        Entry_3.configure(show = "*")
        Entry_3_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_3.configure(font = Entry_3_Ft)
        Label_4 = tkinter.Label(Form_1,text="确认口令：",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Label_4.place(x = 103,y = 211,width = 144,height = 46)#lock
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5 = tkinter.Entry(Form_1,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Entry_5.place(x = 310,y = 211,width = 224,height = 46)#lock
        Entry_5.configure(bg = "#7dffff")
        Entry_5.configure(relief = "sunken")
        Entry_5.configure(show = "*")
        Entry_5_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_5.configure(font = Entry_5_Ft)
        Button_6 = tkinter.Button(Form_1,text="确认",width = 10,height = 4)
        Fun.Register(uiName,'Button_6',Button_6)
        Button_6.place(x = 174,y = 296,width = 114,height = 46)#lock
        Button_6.configure(bg = "#7dffff")
        Button_6.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_6,15,15)
        Button_6.configure(command=lambda:register_cmd.register_key(uiName,"Button_6"))
        Button_6_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_6.configure(font = Button_6_Ft)
        Button_7 = tkinter.Button(Form_1,text="取消",width = 10,height = 4)
        Fun.Register(uiName,'Button_7',Button_7)
        Button_7.place(x = 360,y = 296,width = 120,height = 46)#lock
        Button_7.configure(bg = "#7dffff")
        Button_7.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_7,15,15)
        Button_7.configure(command=lambda:register_cmd.destroy(uiName,"Button_7"))
        Button_7_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_7.configure(font = Button_7_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = register(root)
    root.mainloop()
