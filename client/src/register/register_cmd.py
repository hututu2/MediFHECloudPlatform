#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
from lib import Fun
import random
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import SEAL_core as seal
import hashlib
from models import common
userpath=''
def register_key(uiName,widgetName):
    if(Fun.GetText(uiName,'Entry_3')==Fun.GetText(uiName,'Entry_5')):
        global userpath
        files=os.listdir(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\key pool')
        id=random.randint(0,len(files)-1)
        userpath=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\key pool\\'+files[id]
        temp=seal.ret_parms(userpath)
        [flag,key_hash]=common.enc_file(userpath,os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\private key\\key',Fun.GetText(uiName,'Entry_3'))
        if(userpath!='' and flag and common.register('/register',key_hash,temp)):
            Fun.MessageBox('注册成功成功，跳转至登录页面')             
            root = Fun.GetElement(uiName, 'root')
            root.destroy()
            topLevel = tkinter.Tk()
            from src.app import app
            app.app(topLevel)
            topLevel.mainloop()
        else:
            Fun.MessageBox('不好意思出错了，请重新注册！')
            pass
    else:
        Fun.MessageBox('两次密码不一致，请重新注册！')
        pass
def destroy(uiName,widgetName):
    root = Fun.GetElement(uiName, 'root')
    root.destroy()
    topLevel = tkinter.Tk()
    from src.app import app
    app.app(topLevel)
    topLevel.mainloop()
