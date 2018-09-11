from telegram.ext import Updater
from telegram.ext import Filters, MessageHandler
from datetime import datetime as dt
import re

def start(bot, updater):
    bot.sendMessage(chat_id=updater.message.chat_id, text='Hi!')    


def dialog(bot, updater):
    if re.match(r'.*(жор)|(шам)|(врем)|(час).*', str(updater.message.text).lower()):
        ghora(bot, updater)
    else:
        bot.sendMessage(chat_id=updater.message.chat_id, text='~Эщкерее!')  


def ghora(bot, updater):
    text = 'Сейчас ' + str(dt.now().hour * 2)
    if dt.now().hour * 2 in [1, 21, 31, 41]:
        text += ' Жора'
    elif dt.now().hour * 2 in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44]:
        text += ' Жоры'
    else: text += ' Жор'
    if dt.now().minute >=5 :
        if dt.now().minute / 5  == 1:
            text += ' и ' + str(int(dt.now().minute/5)) + ' Шамиль'
        elif dt.now().minute / 5 in [2,3,4]:
            text += ' и ' + str(int(dt.now().minute/5)) + ' Шамиля'
        else:
            text += ' и ' + str(int(dt.now().minute/5)) + ' Шамилей'
    bot.sendMessage(chat_id=updater.message.chat_id, text=text)


updater = Updater(token='490394177:AAFLj9xuY3UJA5heHaVJ1JtDZYcPwbqJcoQ')
#start_handler = CommandHandler('ghor', ghora)
ghor_handler = MessageHandler(Filters.text, dialog)
updater.dispatcher.add_handler(ghor_handler)
#updater.dispatcher.add_handler(start_handler)
updater.start_polling()

