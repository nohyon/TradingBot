import win32com.client

def ConnetionStatus(): 
    Cybos = win32com.client.Dispatch("CpUtil.CpCybos")
    if Cybos.IsConnect == True:
        return True
    else:
        return False

SendConnectionStatus = ConnecttionStatus()

def GetItem():
    Item = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codelist = Item.GetStockListByMarket(1)

    for i, code in enumerate(codelist):
        secondCode = Item.GetStockSectionKind(code)
        name = Item.CodeToName(code)
        print(i, code, secondCode, name)
    
