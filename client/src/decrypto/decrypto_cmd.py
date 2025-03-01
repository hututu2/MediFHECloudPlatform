#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
import tempfile
sys.path.append(abspath(".."))
import tkinter
import tkinter.filedialog
from  tkinter import *
from app import app_cmd
from lib import Fun
from models import common
from models import GridBase
import SEAL_core as seal
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

def homoDecrypto(userhash,userdata):
    result=seal.vectorD()
    result=seal.dehandle(userhash,userdata)
    return list(result)

def Button_10_onCommand(uiName,widgetName):
    item = GridBase.deleteSelected(uiName, 'TreeView_12')
    if(item == None):
        Fun.MessageBox("请先选择数据,再进行下载解密!")
        return
    path=''.join(item)
    re=common.download(path)
    decrypto_file=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\download\\'+path[-14:]
    with open(decrypto_file,"wb") as f:
        f.write(re.content)
    key_path=app_cmd.openPath
    key=app_cmd.password
    temp_key_path=tempfile.mkdtemp()+"\\dec_key"
    common.dec_key(key_path,temp_key_path,key)
    result=homoDecrypto(temp_key_path,decrypto_file)
    print(result)
    os.remove(temp_key_path)
    treeview = GridBase.clearData(uiName,'TreeView_13')
    for item in result:
        treeview.insert('', 'end', values=item)

def Button_14_onCommand(uiName,widgetName,id):
    treeview = GridBase.clearData(uiName,'TreeView_12')
    [flag,res] = common.dblist(app_cmd.key_sha256,id)
    if(flag):
        for item in res.text.split(','):
            treeview.insert('', 'end', values=item)
    else:
        Fun.MessageBox('没有数据')
def Button_15_onCommand(uiName,widgetName):
    root = Fun.GetElement(uiName, 'root')
    root.destroy()
    topLevel = tkinter.Tk()
    from src.main import main
    main.main(topLevel)
    topLevel.mainloop()
