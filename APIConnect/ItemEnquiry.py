import win32com.client 
inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
inStockMst = win32com.client.Dispatch("dscbo1.StockMst")

#종목코드로 종목의 이름을 가져오는 function입니다
def CodeToName(ItemCode):
    ItemName = inCpStockCode.CodeToName(ItemCode)
    return(ItemName)

#종목이름으로 종목의 코드를 가져오는 function입니다
def NameToCode(ItemName):
    ItemCode = inCpStockCode.NameToCode(ItemName)
    return(ItemCode)

#전체종목의 갯수를 가져오는 function입니다
def ItemCount():
    EntireItem = inCpStockCode.GetCount()
    return(EntireItem)

# 종목코드로 인덱스를 가져오는 function입니다
def CodeToIndex(ItemCode):
    Index = inCpStockCode.CodeToIndex(ItemCode)
    return(Index)

#종목코드로 종목정보를 가져오는 function입니다
def ItemInfo(ItemCode):
    inStockMst.SetInputValue(0, ItemCode)
    inStockMst.BlockRequest()
    Code = inStockMst.GetHeaderValue(0)
    Name = inStockMst.GetHeaderValue(1)
    CurrentPrice = inStockMst.GetHeaderValue(11)
    MarketPrice = inStockMst.GetHeaderValue(13)
    NewHighPriceDay = inStockMst.GetHeaderValue(22)
    NewLowPriceDay = inStockMst.GetHeaderValue(24)
    print (Code '\n' Name'\n'CurrentPrice'\n'MarketPrice'\n'NewHighPriceDay'\n'NewLowPriceDay)