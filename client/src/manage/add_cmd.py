#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
import time
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
from app import app_cmd
from models import common
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import GridBase
def Button_8_onCommand(uiName,widgetName):
    root = Fun.GetElement(uiName, 'root')
    UIInputDataArray = Fun.GetInputDataArray(uiName)
    t=time.strftime("%Y%m%d-%H.%M", time.localtime())
    name = UIInputDataArray['Entry_2'][0]
    age = UIInputDataArray['Entry_3'][0]
    if(UIInputDataArray['Group_1'][0]==1):
        gender='男'
    else:
        gender='女'
    rate = UIInputDataArray['Entry_5'][0]
    id_number = UIInputDataArray['Entry_6'][0]
    txt = Fun.GetText('add', 'Button_8')
    if(txt == "修改"):
        
        if(common.change_patient(app_cmd.key_sha256, name,age,gender,rate,id_number)):
            root.withdraw()
            Fun.MessageBox('修改病人信息成功')
            GridBase.editSelected('DbList', 'TreeView_12',name,age,gender,rate,id_number,t) 
        else:
            root.withdraw()
            Fun.MessageBox('出错了，请重新修改！')    
    else:
        [flag,text]=common.add_patient(app_cmd.key_sha256, name,age,gender,rate,id_number,t)
        if(flag):
            if(text=='添加成功'):
                GridBase.addItem('DbList', 'TreeView_12',name,age,gender,rate,id_number,t)
                root.withdraw()
                Fun.MessageBox('添加病人成功') 
            else:
                root.withdraw()
                Fun.MessageBox('身份证号已存在') 
        else:
            root.withdraw()
            Fun.MessageBox('出错了，请重新添加！')    
def destroy(uiName,widgetName):
    root = Fun.GetElement(uiName, 'root')
    root.withdraw()