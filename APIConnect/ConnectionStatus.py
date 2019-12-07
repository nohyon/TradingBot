import win32com.client

def ConnetionStatus(): 
    Cybos = win32com.client.Dispatch("CpUtil.CpCybos")
    if Cybos.IsConnect == True:
        return True
    else:
        return False
