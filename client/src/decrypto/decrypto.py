#coding=utf-8
#import libs 
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
sys.path.append(abspath("..\\.."))
import decrypto_cmd
import decrypto_sty
from lib import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  decrypto:
    def __init__(self,root,id,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.id=id
        Fun.Register(uiName,'root',root)
        style = decrypto_sty.SetupStyle()
        if isTKroot == True:
            root.title("解密界面")
            Fun.CenterDlg(uiName,root,889,378)
            root['background'] = '#dbffff'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 889,height = 378)
        Form_1.configure(bg = "#dbffff")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Button_10 = tkinter.Button(Form_1,text="下载解密",width = 10,height = 4)
        Fun.Register(uiName,'Button_10',Button_10)
        Button_10.place(x = 661,y = 15,width = 100,height = 38)
        Button_10.configure(command=lambda:decrypto_cmd.Button_10_onCommand(uiName,"Button_10"))
        Button_10_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_10.configure(font = Button_10_Ft)

        TreeView_12 = tkinter.ttk.Treeview(Form_1,show="tree")
        Fun.Register(uiName,'TreeView_12',TreeView_12)
        TreeView_12.place(x = 5,y = 62,width = 882,height = 244)
        TreeView_12.configure(show = "headings")
        TreeView_12.configure(selectmode = "extended")
        TreeView_12.configure(columns = ["加密文件"])
        TreeView_12.column("加密文件",anchor="center",width=440)
        TreeView_12.heading("加密文件",text="加密文件(按时间排序)")

        TreeView_13 = tkinter.ttk.Treeview(Form_1,show="tree")
        Fun.Register(uiName,'TreeView_13',TreeView_13)
        TreeView_13.place(x = 5,y = 307,width = 882,height = 70)
        TreeView_13.configure(show = "headings")
        TreeView_13.configure(selectmode = "extended")
        TreeView_13.configure(columns = ["解密结果"])
        TreeView_13.column("解密结果",anchor="center",width=440)
        TreeView_13.heading("解密结果",text="解密结果")

        Button_14 = tkinter.Button(Form_1,text="加载数据",width = 10,height = 4)
        Fun.Register(uiName,'Button_14',Button_14)
        Button_14.place(x = 110,y = 15,width = 112,height = 38)
        Button_14.configure(command=lambda:decrypto_cmd.Button_14_onCommand(uiName,"Button_14",self.id))
        Button_14_Ft=tkinter.font.Font(family='System', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_14.configure(font = Button_14_Ft)

        Button_15 = tkinter.Button(Form_1,text="返回",width = 10,height = 4)
        Fun.Register(uiName,'Button_15',Button_15)
        Button_15.place(x = 0,y = 0,width = 40,height = 20)
        Button_15.configure(command=lambda:decrypto_cmd.Button_15_onCommand(uiName,"Button_15"))
        Button_15_Ft=tkinter.font.Font(family='System', size=8,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_15.configure(font = Button_15_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = decrypto(root,'')
    root.mainloop()
