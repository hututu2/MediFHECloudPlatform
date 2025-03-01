#coding=utf-8

#import libs 
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
sys.path.append(abspath("..\\.."))
import add_cmd
import add_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  add:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", root.withdraw)
        style = add_sty.SetupStyle()
        if isTKroot == True:
            root.title("添加")
            Fun.CenterDlg(uiName,root,400,470)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 400,height = 470)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'root',root)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_2= tkinter.Label(root,text="姓名",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2)
        Label_2.place(x = 50,y = 50,width = 55,height = 34)
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)

        Label_3= tkinter.Label(root,text="年龄",width = 10,height = 4)
        Fun.Register(uiName,'Label_3',Label_3)
        Label_3.place(x = 50,y = 120,width = 54,height = 35)
        Label_3.configure(relief = "flat")
        Label_3_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_3.configure(font = Label_3_Ft)

        Label_4= tkinter.Label(root,text="性别",width = 10,height = 4)
        Fun.Register(uiName,'Label_3',Label_4)
        Label_4.place(x = 50,y = 190,width = 54,height = 35)
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)

        Label_5= tkinter.Label(root,text="心率情况",width = 10,height = 4)
        Fun.Register(uiName,'Label_3',Label_5)
        Label_5.place(x = 30,y = 250,width = 80,height = 35)
        Label_5.configure(relief = "flat")
        Label_5_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_5.configure(font = Label_5_Ft)

        Label_6= tkinter.Label(root,text="身份证",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_6)
        Label_6.place(x = 50,y = 320,width = 55,height = 34)
        Label_6.configure(relief = "flat")
        Label_6_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_6.configure(font = Label_6_Ft)

        Entry_2_Variable = Fun.AddTKVariable(uiName,'Entry_2','')
        Entry_2= tkinter.Entry(root,textvariable=Entry_2_Variable)
        Fun.Register(uiName,'Entry_2',Entry_2)
        Entry_2.place(x = 127,y = 50,width = 200,height = 36)
        Entry_2.configure(relief = "sunken")

        Entry_3_Variable = Fun.AddTKVariable(uiName,'Entry_3','')
        Entry_3= tkinter.Entry(root,textvariable=Entry_3_Variable)
        Fun.Register(uiName,'Entry_3',Entry_3)
        Entry_3.place(x = 127,y = 120,width = 200,height = 36)
        Entry_3.configure(relief = "sunken")

        Group_1_Variable = Fun.AddTKVariable(uiName,'Group_1')
        Group_1_Variable.set(1)
        #Create the elements of root 
        RadioButton_8 = tkinter.Radiobutton(Form_1,variable=Group_1_Variable,value=1,text="男",anchor=tkinter.W)
        Fun.Register(uiName,'RadioButton_8',RadioButton_8,None,'Group_1')
        RadioButton_8.place(x = 127,y = 190,width = 100,height = 20)
        RadioButton_9 = tkinter.Radiobutton(Form_1,variable=Group_1_Variable,value=2,text="女",anchor=tkinter.W)
        Fun.Register(uiName,'RadioButton_9',RadioButton_9,None,'Group_1')
        RadioButton_9.place(x = 227,y = 190,width = 100,height = 20)    

        Entry_5_Variable = Fun.AddTKVariable(uiName,'Entry_5','')
        Entry_5= tkinter.Entry(root,textvariable=Entry_5_Variable)
        Fun.Register(uiName,'Entry_5',Entry_5)
        Entry_5.place(x = 127,y = 250,width = 200,height = 36)
        Entry_5.configure(relief = "sunken")

        Entry_6_Variable = Fun.AddTKVariable(uiName,'Entry_6','')
        Entry_6= tkinter.Entry(root,textvariable=Entry_6_Variable)
        Fun.Register(uiName,'Entry_6',Entry_6)
        Entry_6.place(x = 127,y = 320,width = 200,height = 36)
        Entry_6.configure(relief = "sunken")

        Button_8= tkinter.Button(root,text="添加",width = 10,height = 4)
        Fun.Register(uiName,'Button_8',Button_8)
        Button_8.place(x = 150,y = 390,width = 100,height = 48)
        Button_8.configure(command=lambda:add_cmd.Button_8_onCommand(uiName,"Button_8"))
        Button_8_Ft=tkinter.font.Font(family='System', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_8.configure(font = Button_8_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = add(root)
    root.mainloop()
