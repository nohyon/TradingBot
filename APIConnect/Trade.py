import win32com.client

CpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
CpTd0311 = win32com.client.Dispatch("CpTrade.CpTd0311")

#주문초기화
initCheck = objTrade.TradeInit(0)
if (initCheck != 0):
    print("주문 초기화 실패")
    exit()

#주식매매주문
Tradetype = 
Account = objTrade.AccountNumber[0] #계좌번호
Itemcode = 
Quantity =
Price = 

CpTd0311.SetInputValue(0, Tradetype)   # 1:매도, 2:매수
CpTd0311.SetInputValue(1, Account)   #  계좌번호
CpTd0311.SetInputValue(3, Itemcode)   # 종목코드
CpTd0311.SetInputValue(4, Quantity)   # 수량
CpTd0311.SetInputValue(5, Price)   # 주문단가
CpTd0311.BlockRequest() # 주문 전송
 
rqStatus = CpTd0311.GetDibStatus()
rqRet = CpTd0311.GetDibMsg1()
print("통신상태", rqStatus, rqRet)
if rqStatus != 0:
    exit()