#coding=utf-8
import sys
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
from app import app_cmd
from models import common
import GridBase
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 
global id
id='11'
def Button_8_onCommand(uiName,widgetName):
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import add
    add.add(topLevel)
    tkinter.Tk.wait_window(topLevel)
def Button_10_onCommand(uiName,widgetName):
    item = GridBase.deleteSelected(uiName, 'TreeView_12')
    if(item == None):
        Fun.MessageBox("请先选择病人,再进行删除!")
        return
    if(common.delete_patient(app_cmd.key_sha256,item[4])):
        Fun.MessageBox("删除成功")
    else:
        Fun.MessageBox("删除失败")
def Button_13_onCommand(uiName,widgetName):
    item = GridBase.getSelected(uiName, 'TreeView_12')
    if(item == None):
        Fun.MessageBox("请先选择病人,再进行修改!")
        return
    topLevel = tkinter.Toplevel()
    topLevel.attributes("-toolwindow", 1)
    topLevel.wm_attributes("-topmost", 1)
    import add
    add.add(topLevel)
    #设置修改页的值
    Fun.SetText('add','Entry_2',item[0])
    Fun.SetText('add','Entry_3',item[1])
    Fun.SetText('add','Entry_5',item[3])
    Fun.SetText('add','Entry_6',item[4])
    Fun.SetTKAttrib('add','Entry_6','state','disable')
    Fun.SetText('add', 'Button_8', '修改')
    tkinter.Tk.wait_window(topLevel)
def Button_14_onCommand(uiName,widgetName):
    treeview = GridBase.clearData(uiName,'TreeView_12')
    res = common.patient_list(app_cmd.key_sha256)
    if(res.text!=''):
        for i in res.text.split(','):
            item = i.split('|')
            treeview.insert('', 'end', values=(item[0], item[1], item[2],item[3],item[4],item[5]))
def Button_15_onCommand(uiName,widgetName):
    item = GridBase.getSelected(uiName, 'TreeView_12')
    if(item == None):
        Fun.MessageBox("请先选择病人,在进入主页!")
        return
    root = Fun.GetElement(uiName, 'root')
    root.destroy()
    # root.withdraw()
    topLevel = tkinter.Tk()
    from src.main import main
    main.main(topLevel,str(item[4]))
    topLevel.mainloop()
