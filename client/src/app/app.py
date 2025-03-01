#coding=utf-8
#import libs 
import sys
from  os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import app_cmd
import app_sty
from lib import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  app:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = app_sty.SetupStyle()
        if isTKroot == True:
            root.title("同态加密")
            root.resizable(False,False)
            root.wm_attributes("-transparentcolor","#ffffff")
            Fun.CenterDlg(uiName,root,784,646)
            root['background'] = '#e8ffff'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 784,height = 646)
        Form_1.configure(bg = "#ffffff")
        Fun.SetRootRoundRectangle(Form_1,0,0,784,646,radius=10,fill='#e8ffff',outline='#ffffff',width=0)
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Group_1_Variable = Fun.AddTKVariable(uiName,'Group_1')
        Group_1_Variable.set(1)
        #Create the elements of root 
        Label_2 = tkinter.Label(Form_1,text="支持同态加密的\n\n医疗数据计算系统",width = 10,height = 4)
        Fun.Register(uiName,'Label_2',Label_2,'introduction')
        Label_2.place(x = 23,y = 142,width = 334,height = 321)
        Label_2.configure(bg = "#7dff7d")
        Label_2.configure(fg = "#00000b")
        Label_2.configure(relief = "flat")
        Fun.SetRoundedRectangle(Label_2,90,90)
        Label_2_Ft=tkinter.font.Font(family='华文行楷', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Button_3 = tkinter.Button(Form_1,text="选择密钥",width = 10,height = 4)
        Fun.Register(uiName,'Button_3',Button_3,'key_select')
        Button_3.place(x = 490,y = 261,width = 216,height = 43)
        Button_3.configure(bg = "#84ffff")
        Button_3.configure(activebackground = "#007979")
        Button_3.configure(activeforeground = "#000000")
        Button_3.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_3,15,15)
        Button_3.configure(command=lambda:app_cmd.key_select(uiName,"Button_3"))
        Button_3_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_3.configure(font = Button_3_Ft)
        Label_8 = tkinter.Label(Form_1,text="password：",width = 10,height = 4)
        Fun.Register(uiName,'Label_8',Label_8,'pass')
        Label_8.place(x = 367,y = 205,width = 123,height = 38)
        Label_8.configure(bg = "#e6ffff")
        Label_8.configure(relief = "flat")
        Label_8_Ft=tkinter.font.Font(family='宋体', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_8.configure(font = Label_8_Ft)
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9 = tkinter.Entry(Form_1,textvariable=Entry_9_Variable)
        Fun.Register(uiName,'Entry_9',Entry_9,'pass_input')
        Entry_9.place(x = 494,y = 205,width = 212,height = 38)
        Entry_9.configure(bg = "#8affff")
        Entry_9.configure(relief = "flat")
        Entry_9.configure(show = "*")
        Entry_9_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_9.configure(font = Entry_9_Ft)
        Label_10 = tkinter.Label(Form_1,text="key文件 ：",width = 10,height = 4)
        Fun.Register(uiName,'Label_10',Label_10,'key')
        Label_10.place(x = 367,y = 261,width = 123,height = 43)
        Label_10.configure(bg = "#e3ffff")
        Label_10.configure(relief = "flat")
        Label_10_Ft=tkinter.font.Font(family='宋体', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_10.configure(font = Label_10_Ft)
        Button_11 = tkinter.Button(Form_1,text="登录",width = 10,height = 4)
        Fun.Register(uiName,'Button_11',Button_11,'login')
        Button_11.place(x = 427,y = 340,width = 100,height = 38)
        Button_11.configure(bg = "#84ffff")
        Button_11.configure(activebackground = "#00b9b9")
        Button_11.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_11,15,15)
        Button_11.configure(command=lambda:app_cmd.turn_main(uiName,"Button_11"))
        Button_11_Ft=tkinter.font.Font(family='宋体', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_11.configure(font = Button_11_Ft)
        Button_12 = tkinter.Button(Form_1,text="注册",width = 10,height = 4)
        Fun.Register(uiName,'Button_12',Button_12,'register')
        Button_12.place(x = 580,y = 340,width = 100,height = 38)
        Button_12.configure(bg = "#84ffff")
        Button_12.configure(activebackground = "#00b9b9")
        Button_12.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_12,15,15)
        Button_12.configure(command=lambda:app_cmd.turn_rigster(uiName,"Button_12"))
        Button_12_Ft=tkinter.font.Font(family='宋体', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_12.configure(font = Button_12_Ft)

        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = app(root)
    root.mainloop()
