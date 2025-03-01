from lib import Fun
def deleteSelected(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    item = treeview.item(index)
    return item['values']
def getSelected(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    index = treeview.selection()
    if(len(index) == 0):
        return None
    return treeview.item(index)['values']
def clearData(uiName,TreeViewName):
    treeview = Fun.GetElement(uiName,TreeViewName)
    obj = treeview.get_children()
    for i in obj:
        treeview.delete(i)
    return treeview
