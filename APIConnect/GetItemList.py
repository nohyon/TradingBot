from pandas import Series, DataFrame
import sqlite3
import win32com.client 
inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
inCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
inStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

CodeList1 = inCpCodeMgr.GetStockListByMarket(1) #코스피
CodeList2 = inCpCodeMgr.GetStockListByMarket(2) #코스닥

'''
#코스피의 모든종목코드를 KOSPI.db에 기록하는 function입니다.
def WriteKospi():
    connect = sqlite3.connect("KOSPI.db")
    print("코스피 종목코드", len(CodeList1))
    for i, code in enumerate(CodeList1):
        print (code)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE "+code+" (Date text, Open int, High int, Low int, Closing int, Volumn int)")
    connect.commit
    connect.close

#코스닥의 모든종목코드를 KOSDAQ.db에 기록하는 function입니다.
def WriteKosdaq():
    connect = sqlite3.connect("KOSDAQ.db")
    print("코스닥 종목코드", len(CodeList2))
    for i, code in enumerate(CodeList2):
        print(code)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE "+code+" (Date text, Open int, High int, Low int, Closing int, Volumn int)")
    connect.commit
    connect.close
'''

# 차트 객체 구하기

 
inStockChart.SetInputValue(0, ItemCode)   #종목 코드
inStockChart.SetInputValue(1, ord('2')) # 개수로 조회
inStockChart.SetInputValue(4, 20) # 최근 20일 치
inStockChart.SetInputValue(5, [0,2,3,4,5,8]) #날짜,시가,고가,저가,종가,거래량
inStockChart.SetInputValue(6, ord('D')) # '차트 주가 - 일간 차트 요청
inStockChart.SetInputValue(9, ord('1')) # 수정주가 사용
inStockChart.BlockRequest()

len = inStockChart.GetHeaderValue(3)

#KOSPI.db의 테이블에 정보를 입력하는 부분입니다.
def StoreKospiData():
    connect = sqlite3.connect("KOSPI.db")
    cursor.execute("INSERT INTO "+code+" VALUES(Date text, Open int, High int, Low int, Closing int, Volumn int)")
    for i in range(len):
    day = inStockChart.GetDataValue(0, i)
    open = inStockChart.GetDataValue(1, i)
    high = inStockChart.GetDataValue(2, i)
    low = inStockChart.GetDataValue(3, i)
    close = inStockChart.GetDataValue(4, i)
    vol = inStockChart.GetDataValue(5, i)
    prt (day, open, high, low, close, vol)





 


