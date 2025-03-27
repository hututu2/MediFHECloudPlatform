
#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
from lib import Fun
from models import common
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

openPath=''
password=''
def key_select(uiName,widgetName):
    global openPath
    openPath = tkinter.filedialog.askopenfilename(initialdir=os.path.abspath('.'),title='Open key File',filetypes=[('All files','*')])
    Fun.SetText(uiName,'Button_3','已选择')
def turn_main(uiName,widgetName):
    global openPath
    global password
    global key_sha256
    password=Fun.GetText(uiName,'Entry_9')
    [flag,key_sha256]=common.dec_file(openPath,os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\private key\\dec_key',password)
    # print(key_sha256)
    if(flag and common.login('/login',key_sha256)):
        if(Fun.AskBox('登录成功','登陆成功是否跳转至管理页面')):
            root = Fun.GetElement(uiName, 'root')
            root.destroy()
            topLevel = tkinter.Tk()
            from src.manage import DbList
            DbList.DbList(topLevel)
            topLevel.mainloop()
        else:
            pass
    else:
        Fun.MessageBox('登录失败,请重新输入password和选择密钥')
        openPath=''
        password=''
        Fun.SetText(uiName,'Entry_9','')
        Fun.SetText(uiName,'Button_3','请选择密钥')
        pass
def turn_rigster(uiName,widgetName):
    root = Fun.GetElement(uiName, 'root')
    root.destroy()
    topLevel = tkinter.Tk()
    from src.register import register
    register.register(topLevel)
    topLevel.mainloop()
