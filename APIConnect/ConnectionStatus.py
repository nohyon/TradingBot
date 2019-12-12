'''
import win32com.client

def ConnetionStatus(): 
    Cybos = win32com.client.Dispatch("CpUtil.CpCybos")
    if Cybos.IsConnect == True:
        print("True")
    else:
        print("False")
'''
print("true")