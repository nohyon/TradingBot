import win32com.client
StockChart = win32com.client.Dispatch("CpSysDib.StockChart")

def GetItemData():
    StockChart.SetInputValue(0,ItemCode)
    StockChart.SetInputValue(1,ord('2'))
    StockChart.SetInputValue(4,20)
    StockChart.SetInputValue(5,5)
    StockChart.SetInputValue(6,ord('D'))

StockChart.BlockRequest()
numData = StockChart.GetHeaderValue(3)
for i in range(numData):
    print(StockChart.GetDataValue(0, i))