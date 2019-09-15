from pandas import Series, DataFrame
import pandas_datareader.data as web
import datetime
import sqlite3

'''
#데이터 입력 폼 예시
daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

#날짜
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']

#columns 가로줄 index 세로줄 
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
close = daeshin_day['close']
print (close)
print(daeshin_day)

#특정일 데이터 출력
day_data = daeshin_day.ix['16.02.24']
print(day_data)
print(type(day_data))
'''

'''
#인터넷에서 주가 정보 가져오는 부분
start = datetime.datetime(2019, 9, 5)
end = datetime.datetime(2019, 9, 15)
gs = web.DataReader("078930.KS", "yahoo", start, end)
print (gs)
#위 정보로 이평값 구하는 부분
ma5 = gs['Adj Close'].rolling(window=5).mean()
print (ma5.tail(10))
'''

'''
#DB부분 
con = sqlite3.connect("stock.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE GS(Date text, Open int, Low int, Closing int, Volumn int)")
cursor.execute("INSERT INTO kakao VALUES()")
con.commit
con.close

cursor.execute("SELECT * FROM kakao")
cursor.fetchone()
cursor.fetchone()
cursor.execute("SELECT * FROM kakao")
cursor.fetchall()

cursor.execute("SELECT * FROM kakao")
kakao = cursor.fetchall()
kakao [0][0]
kakao [0][1]
kakao [0][2]
'''
