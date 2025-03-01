#coding=utf-8
import hashlib
import sys
import os
from   os.path import abspath, dirname
import tempfile
# import time
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
from app import app_cmd
from lib import Fun
import SEAL_core as seal
from models import common
from models import getRawData
from models import GridBase
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 
temp_data_byAES=''
encdata=''
data=list()

def homoEncrypto(userhash,userdata):
    try:
        userdata=seal.vectorD(userdata)
        path=seal.enhandle(userhash,userdata)
        return path 
    except:
        return ''

def read(uiName,widgetName):
    global data
    data=getRawData.getRawData()
    treeview = GridBase.clearData(uiName,'TreeView_12')
    for item in data:
        treeview.insert('', 'end', values=item)

def Encrypto(uiName,widgetName):
    try:
        # data=[1,2,3,4,5]
        if len(data)!=0:
            key_path=app_cmd.openPath
            key=app_cmd.password
            
            temp_key_path=tempfile.mkdtemp()+"\\dec_key"
            global temp_data_byAES
            temp_data_byAES=tempfile.mkdtemp()+"\\temp_AES"
            with open("AES",'w') as f:
                for i in data:
                    f.write(str(i)+' ')
            f.close()

            common.enc_AES("AES",temp_data_byAES,key)
            common.dec_key(key_path,temp_key_path,key)

            global encdata
            encdata=homoEncrypto(temp_key_path,data)
            os.remove(temp_key_path)
            Fun.MessageBox("本地加密成功")
        else:
            Fun.MessageBox("请先进行测量！")
    except:
        Fun.MessageBox("加密失败")

def pack(uiName,widgetName,id):
    global encdata
    if encdata!='':
        if(common.file_post(app_cmd.key_sha256,id,encdata,temp_data_byAES)):
            Fun.MessageBox("上传成功")
        else:
            Fun.MessageBox("上传失败")
    else:
        Fun.MessageBox("请先进行加密！")

def Decrypto(uiName,widgetName,id):
    if(Fun.AskBox('解密界面','是否跳转至解密页面')):
        root = Fun.GetElement(uiName, 'root')
        root.destroy()
        topLevel = tkinter.Tk()
        from src.decrypto import decrypto
        decrypto.decrypto(topLevel,id)
        topLevel.mainloop()
    else:
        pass
def Button_6_onCommand(uiName,widgetName):
    root = Fun.GetElement(uiName, 'root')
    root.destroy()
    topLevel = tkinter.Tk()
    from src.manage import DbList
    DbList.DbList(topLevel)
    topLevel.mainloop()
