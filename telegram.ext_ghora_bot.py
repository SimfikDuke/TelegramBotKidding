from telegram.ext import Updater
from telegram.ext import Filters, MessageHandler
from datetime import datetime as dt
import re

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Hi!')    


def dialog(bot, update):
    message = str(update.message.text)
    if re.match(r'.*(пар)|(кон)|(осталось)|(еще).*', message.lower()):
        ghorleft(bot, update)
    elif re.match(r'.*(жор)|(шам)|(врем)|(час).*', message.lower()):
        ghora(bot, update)
    elif re.match(r'.*(богд)|(мопс)|(жоп)|(пес).*', message.lower()):
        bot.sendMessage(chat_id=update.message.chat_id, text='Мопс')  
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='~Эщкерее!')  



def ghora(bot, update):
    h, m = dt.now().hour, dt.now().minute
    timeinghor = 'Сейчас ' + timetoghor(h,m)
    bot.sendMessage(chat_id=update.message.chat_id, text=timeinghor)
    
    
def ghorleft(bot, update):
    h, m = dt.now().hour, dt.now().minute
    if h == 8 or (h == 9 and m <= 25):
        bot.sendMessage(chat_id=update.message.chat_id, text='До конца пары осталось:\n'+timetoghor(9-h,110-m))
    elif h == 9 and m >= 50 or h == 10 or h == 11 and m <= 15:
        bot.sendMessage(chat_id=update.message.chat_id, text='До конца пары осталось:\n'+timetoghor(11-h,80-m))
    elif h == 11 and m >= 30 or h == 12:
        bot.sendMessage(chat_id=update.message.chat_id, text='До конца пары осталось:\n'+timetoghor(13-h,120-m))

def timetoghor(hours, minutes):
    gh, sh = int(hours * 2 + minutes/30) , int((minutes % 30) / 5)
    text = str(gh)
    if gh in [1, 21, 31, 41]:
        text += ' Жора'
    elif gh in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44]:
        text += ' Жоры'
    else: text += ' Жор'
    text += ' \ud83d\ude47\ud83c\udffc'
    if sh :
        text += '\n'
        if sh  == 1:
            text += ' и ' + str(sh) + ' Шамиль'
        elif sh in [2,3,4]:
            text += ' и ' + str(sh) + ' Шамиля'
        else:
            text += ' и ' + str(sh) + ' Шамилей'
        text += ' \ud83e\udd26\ud83c\udffb\u200d\u2642'
    else: text += ' ровно'
    return text


update = Updater(token='490394177:AAFLj9xuY3UJA5heHaVJ1JtDZYcPwbqJcoQ')
#start_handler = CommandHandler('ghor', ghora)
ghor_handler = MessageHandler(Filters.text, dialog)
update.dispatcher.add_handler(ghor_handler)
#updater.dispatcher.add_handler(start_handler)
update.start_polling()

