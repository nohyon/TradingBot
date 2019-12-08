import string
import re 

message1 = "대신증권"
message3 = "대신증권 시세"
message4 = "대신증권 매수"
message5 = "대신증권 1주 매수"
message6 = "대신증권 1주 시장가에 매수"
message7 = "대신증권 1주 13000원에 매수"

'''
def GetMessage(Message):
    from Chatbot import get_message
    Message = get_message
    return Message
'''

SplittedMessage = message7.split(' ')
print (SplittedMessage)

def ChatBotProcess(message):
    import APIConnect/ItemInquiry
    
    