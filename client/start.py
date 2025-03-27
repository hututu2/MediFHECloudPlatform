#coding=utf-8
#import libs 
import sys
import time
import hashlib
from lib import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
import SEAL_core as seal

#Add your Varial Here: (Keep This Line of comments)

#Define UI Class
class  start:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        if isTKroot == True:
            root.title("同态加密")
            Fun.CenterDlg(uiName,root,640,480)
            root['background'] = '#d7ffff'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 640,height = 480)
        Form_1.configure(bg = "#d7ffff")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_4 = tkinter.Label(Form_1,text="第一次启动，正在初始化...",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Label_4.place(x = 149,y = 109,width = 328,height = 93)
        Label_4.configure(bg = "#d7ffff")
        Label_4.configure(relief = "flat")
        Label_4_Ft=tkinter.font.Font(family='宋体', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_4.configure(font = Label_4_Ft)
        Progress_2 = tkinter.ttk.Progressbar(Form_1)
        Fun.Register(uiName,'Progress_2',Progress_2)
        Progress_2.place(x = 70,y = 332,width = 492,height = 20)
        Progress_2.configure(orient = tkinter.HORIZONTAL)
        Progress_2.configure(mode = "determinate")
        Progress_2.configure(maximum = "100")
        Progress_2.configure(value = "0.0")
        Progress_2.configure(command=increment(uiName,"Progress_2"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)

#生成密钥池
def create_userfile(ID:int):
    usertemp_filepath=seal.create_parms_keys(ID)
    try:
        f = open(usertemp_filepath, 'rb')
        temp=f.read()
        hash=hashlib.md5()
        hash.update(temp)
        userhash_bin=hash.digest()
        # userhash=os.path.dirname(__file__)+'\\key pool'+'\\'+hash.hexdigest()
        userhash='./key pool'+'/'+hash.hexdigest()
        userfile=open(userhash,'wb')#修改userhash处可以更换用户文件保存目录
        userfile.write(userhash_bin+ID.to_bytes(4,'little')+temp)
        f.close()
        userfile.close()
        os.remove(usertemp_filepath)
        return userhash
    except:
        if f:
            f.close()
        return ''

#初始化进度条
def increment(uiName,widgetName):
    p1=Fun.GetElement(uiName,widgetName)
    # if not os.listdir(os.path.dirname(__file__)+'\\key pool'):
    if not os.listdir('./key pool'):
        for i in range(80):
            p1["value"] = i+1
            root.update()
            time.sleep(0.1)
        for i in range(3):
            create_userfile(3)
        for i in range(20):
            p1["value"] = i+81
            root.update()
            time.sleep(0.1)
    root.destroy()
    topLevel = tkinter.Tk()
    from src.app import app
    app.app(topLevel)
    topLevel.mainloop()

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = start(root)
    root.mainloop()
