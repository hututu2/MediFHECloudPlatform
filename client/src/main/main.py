#coding=utf-8
#import libs 
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import main_cmd
import main_sty
from lib import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  main:
    def __init__(self,root,id,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.id=id
        Fun.Register(uiName,'root',root)
        style = main_sty.SetupStyle()
        if isTKroot == True:
            root.title("主界面")
            Fun.CenterDlg(uiName,root,673,673)
            root['background'] = '#dbffff'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 673,height = 673)
        Form_1.configure(bg = "#dbffff")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'主界面',Form_1)
        #Create the elements of root 
        TreeView_12 = tkinter.ttk.Treeview(Form_1,show="tree")
        Fun.Register(uiName,'TreeView_12',TreeView_12)
        TreeView_12.place(x = 100,y = 15,width = 470,height = 150)
        TreeView_12.configure(show = "headings")
        TreeView_12.configure(selectmode = "extended")
        TreeView_12.configure(columns = ["数据"])
        TreeView_12.column("数据",anchor="center",width=100)
        TreeView_12.heading("数据",text="实测数据(取前5个)")
        Button_2 = tkinter.Button(Form_1,text="仪器读取",width = 10,height = 4)
        Fun.Register(uiName,'Button_2',Button_2)
        Button_2.place(x = 100,y = 190,width = 220,height = 200)#lock
        Button_2.configure(bg = "#b9ffb9")
        Button_2.configure(activebackground = "#95ff95")
        Button_2.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_2,15,15)
        Button_2.configure(command=lambda:main_cmd.read(uiName,"Button_2"))
        Button_2_Ft=tkinter.font.Font(family='宋体', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_2.configure(font = Button_2_Ft)
        Button_3 = tkinter.Button(Form_1,text="本地加密",width = 10,height = 4)
        Fun.Register(uiName,'Button_3',Button_3)
        Button_3.place(x = 350,y = 190,width = 220,height = 200)#lock
        Button_3.configure(bg = "#b9ffb9")
        Button_3.configure(activebackground = "#95ff95")
        Button_3.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_3,15,15)
        Button_3.configure(command=lambda:main_cmd.Encrypto(uiName,"Button_3"))
        Button_3_Ft=tkinter.font.Font(family='宋体', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_3.configure(font = Button_3_Ft)
        Button_4 = tkinter.Button(Form_1,text="打包上传",width = 10,height = 4)
        Fun.Register(uiName,'Button_4',Button_4)
        Button_4.place(x = 100,y = 400,width = 220,height = 200)#lock
        Button_4.configure(bg = "#b9ffb9")
        Button_4.configure(activebackground = "#95ff95")
        Button_4.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_4,15,15)
        Button_4.configure(command=lambda:main_cmd.pack(uiName,"Button_4",self.id))
        Button_4_Ft=tkinter.font.Font(family='宋体', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_4.configure(font = Button_4_Ft)
        Button_5 = tkinter.Button(Form_1,text="解密窗口",width = 10,height = 4)
        Fun.Register(uiName,'Button_5',Button_5)
        Button_5.place(x = 350,y = 400,width = 220,height = 200)#lock
        Button_5.configure(bg = "#b9ffb9")
        Button_5.configure(activebackground = "#95ff95")
        Button_5.configure(relief = "flat")
        Fun.SetRoundedRectangle(Button_5,15,15)
        Button_5.configure(command=lambda:main_cmd.Decrypto(uiName,"Button_5",self.id))
        Button_5_Ft=tkinter.font.Font(family='宋体', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_5.configure(font = Button_5_Ft)

        Button_6 = tkinter.Button(Form_1,text="返回",width = 10,height = 4)
        Fun.Register(uiName,'Button_15',Button_6)
        Button_6.place(x = 0,y = 0,width = 40,height = 20)
        Button_6.configure(command=lambda:main_cmd.Button_6_onCommand(uiName,"Button_6"))
        Button_6_Ft=tkinter.font.Font(family='System', size=8,weight='bold',slant='roman',underline=0,overstrike=0)
        Button_6.configure(font = Button_6_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = main(root,'')
    root.mainloop()
