#coding=utf-8
#import libs 
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import DbList_cmd
import DbList_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from app import app_cmd
from models import common
import GridBase
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  DbList:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = DbList_sty.SetupStyle()
        if isTKroot == True:
            root.title("病人管理")
            Fun.CenterDlg(uiName,root,689,450)
            root['background'] = '#dbffff'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 689,height = 450)
        Form_1.configure(bg = "#dbffff")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_8 = tkinter.Button(Form_1,text="添加",width = 10,height = 4)
        Fun.Register(uiName,'Button_8',Button_8)
        Button_8.place(x = 8,y = 15,width = 100,height = 38)
        Button_8.configure(fg = "#000000")
        Button_8.configure(command=lambda:DbList_cmd.Button_8_onCommand(uiName,"Button_8"))
        Button_8_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_8.configure(font = Button_8_Ft)
        Button_10 = tkinter.Button(Form_1,text="删除",width = 10,height = 4)
        Fun.Register(uiName,'Button_10',Button_10)
        Button_10.place(x = 208,y = 15,width = 100,height = 38)
        Button_10.configure(command=lambda:DbList_cmd.Button_10_onCommand(uiName,"Button_10"))
        Button_10_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_10.configure(font = Button_10_Ft)
        TreeView_12 = tkinter.ttk.Treeview(Form_1,show="tree")
        Fun.Register(uiName,'TreeView_12',TreeView_12)
        TreeView_12.place(x = 5,y = 62,width = 682,height = 314)
        TreeView_12.configure(show = "headings")
        TreeView_12.configure(selectmode = "extended")
        TreeView_12.configure(columns = ["姓名","年龄","性别","心率情况","身份证","添加时间"])
        TreeView_12.column("姓名",anchor="center",width=50)
        TreeView_12.heading("姓名",text="姓名")
        TreeView_12.column("年龄",anchor="center",width=50)
        TreeView_12.heading("年龄",text="年龄")
        TreeView_12.column("性别",anchor="center",width=50)
        TreeView_12.heading("性别",text="性别")
        TreeView_12.column("心率情况",anchor="center",width=80)
        TreeView_12.heading("心率情况",text="心率情况")
        TreeView_12.column("身份证",anchor="center",width=120)
        TreeView_12.heading("身份证",text="身份证(不可修改)")
        TreeView_12.column("添加时间",anchor="center",width=120)
        TreeView_12.heading("添加时间",text="添加时间(不可修改)")
        Button_13 = tkinter.Button(Form_1,text="修改",width = 10,height = 4)
        Fun.Register(uiName,'Button_13',Button_13)
        Button_13.place(x = 108,y = 15,width = 100,height = 38)
        Button_13.configure(command=lambda:DbList_cmd.Button_13_onCommand(uiName,"Button_13"))
        Button_13_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_13.configure(font = Button_13_Ft)
        Button_14 = tkinter.Button(Form_1,text="加载数据",width = 10,height = 4)
        Fun.Register(uiName,'Button_14',Button_14)
        Button_14.place(x = 571,y = 15,width = 112,height = 38)
        Button_14.configure(command=lambda:DbList_cmd.Button_14_onCommand(uiName,"Button_14"))
        Button_14_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_14.configure(font = Button_14_Ft)
        Button_15 = tkinter.Button(Form_1,text="病人主页",width = 10,height = 4)
        Fun.Register(uiName,'Button_15',Button_15)
        Button_15.place(x = 300,y = 400,width = 112,height = 25)
        Button_15.configure(command=lambda:DbList_cmd.Button_15_onCommand(uiName,"Button_15"))
        Button_15_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_15.configure(font = Button_15_Ft)
        Label_2 = tkinter.Label(Form_1,text="",width = 0,height = 0)
        Fun.Register(uiName,'Label_2',Label_2)
        Label_2.place(x = 0,y = 0,width = 0,height = 0)#lock
        Label_2.configure(relief = "flat")
        Label_2_Ft=tkinter.font.Font(family='宋体', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_2.configure(font = Label_2_Ft)
        Label_2.configure(command=Refresh(uiName,"Label_2"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
def Refresh(uiName,widgetName):
    treeview = GridBase.clearData(uiName,'TreeView_12')
    res = common.patient_list(app_cmd.key_sha256)
    if(res.text!=''):
        for i in res.text.split(','):
            item = i.split('|')
            treeview.insert('', 'end', values=(item[0], item[1], item[2],item[3],item[4],item[5]))


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = DbList(root)
    root.mainloop()
