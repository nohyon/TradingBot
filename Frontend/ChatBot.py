import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

#텔레그램 봇 토큰을 받는 function입니다.
def GetToken():
    file = open("TelegramToken.txt","r")
    token = file.read()
    return(token)

#메세지를 저장하는 function입니다.
def StoreMessage(m):
    file = open("MessageLog.txt","a")
    file.write(str(m)+'\n')
    file.close()

# 메세지에 대답하는 function입니다.
def get_message(bot, update):
    import ChatBotProcess
    MessageText = update.message.text
    ChatBotProcess(MessageText)

#Cybos 연결상태를 확인하는 function입니다.
def CybosConnection():
    from APIConnect.APIConnection import SendConnectionStatus
    if SendConnectionStatus == True:
        print("Cybos에 연결되었습니다.")
    else:
        print("Cybos에 연결하는데 문제가 생겼습니다.")


MyToken = ""
bot = telegram.Bot(token = MyToken)
update = bot.getUpdates()

for u in update :
    StoreMessage(u.message)

#봇이 유저에게 메세지를 보내는 코드
bot.send_message(chat_id = 842327320, text = "하하하")

'''
#매도/매수 주문체결 안내
def OrderFilled:
    from Trade import #체결부분변수
    {}
    bot.send_message(chat_id = 842327320, text = #종목이름변수 + #체결주수량변수 + "주 가" + #체결가격변수 + "원 에 체결되었습니다.")
'''
#전체종목 개수를 확인하는 function입니다
def EntireItem():
    from APIConnect.ItemInquiry import EntireItem
    Item = EntireItem()
    print("전체 종목의 수는"+Item+"개 입니다.")

#종목검색
def ItemSearch(MessageText):
    from APIConnect.ItemInquiry import ItemInfo
    update.message.reply_text(ItemName + "종목을 검색합니다.")
    
    #주식코드
    #종목이름
    #현재가
    #종목여부


#종목주문
def ItemOrder(MessageText):
    import re  
    s = '123abc'
    i = int(re.findall('\d+', s)[0])
    
    

'''
#현재잔고
def BankBalance:
    from #프로그램 import #잔고부분변수
    bot.send_message(chat_id = 842327320, text = "현재 평가금액은" + #평가금액변수 "원 입니다.")
    bot.send_message(chat_id = 842327320, text = )
    bot.send_message(chat_id = 842327320, text = )
'''

def StartCommand(bot, update):
    update.message.reply_text("TradingBot을 시작합니다.")

def HelpCommand(bot, update):
    update.message.reply_text("안녕하세요 TradingBot 입니다.\n저와 함께하면 이런것들을 할 수 있어요.")
 

updater = Updater(MyToken)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)


updater.start_polling(timeout=3, clean=True)
updater.idle()
