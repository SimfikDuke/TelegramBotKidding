from telegram.ext import Filters, MessageHandler, Updater, CommandHandler    
from datetime import datetime as dt
import re
from bs4 import BeautifulSoup as B
from urllib.request import urlopen
from random import randint


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Привет, {Человек, мопс}!\
    \nДавай будем считать жор и смешно шутить!')    


def dialog(bot, update):
    message = str(update.message.text)
    if re.match(r'.*(пар)|(кон)|(осталось)|(еще).*', message.lower()):
        ghorleft(bot, update)
    elif re.match(r'.*(шут)|(анекд)|(рофл)(хах).*', message.lower()):
        bot.sendMessage(chat_id=update.message.chat_id, text=get_random_joke())
    elif re.match(r'.*(жор)|(шам)|(врем)|(час).*', message.lower()):
        ghora(bot, update)
    elif re.match(r'city [a-zA-z]{2,15}', message.lower()):
        cityinfo(bot, update)
    elif re.match(r'.*(богд)|(штогр)|(жоп).*', message.lower()):
        bot.sendMessage(chat_id=update.message.chat_id, text='Мопс')
    elif re.match(r'.*(пук)|(мопс)|(пес).*', message.lower()):
        bot.sendMessage(chat_id=update.message.chat_id, text='Пёрд пёрд')
    elif re.match(r'^\.\..*', message.lower()):
        secretchat(bot, update)
        
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text='~Эщкерее!')  


def secretchat(bot, update):
    log = open('/root/simfik/se/log.txt', 'r')
    last = ['','']
    last[0] = log.read()
    last[1] = log.read()
    log.close()
    #if last[0] != update.message.chat.id:
    last[0] = update.message.chat.id
    bot.sendMessage(chat_id=update.message.chat_id, text=last[1])
    last[1] = update.message.text  
    log = open('/root/simfik/se/log.txt', 'w')
    log.write(last[0])
    log.write(last[1])
    log.close()

def get_random_joke():
    html = urlopen('http://anekdotme.ru/lenta/page_' + str(randint(1,464)))
    soup = B(html)
    content = soup.find_all('div', 'anekdot')
    joke_list = [i.find('div', 'anekdot_text').text for i in content]
    return str(joke_list[randint(0, len(joke_list))])


def cityinfo(bot, update):
    message = update.message.text
    city = message[5:]
    html = urlopen('http://nesiditsa.ru/city/' + city)
    soup = B(html, "html.parser")
    content = soup.find('div', 'city-info-block row')
    sections = content.find_all('td')
    #joke_list = [i.find('div', 'anekdot_text').text for i in content]
    bot.sendMessage(chat_id=update.message.chat_id, text=city[0].upper()+city[1:]+' city:')
    for i in sections:
        bot.sendMessage(chat_id=update.message.chat_id, text=i.text)


def ghora(bot, update):
    h, m = dt.now().hour, dt.now().minute
    timeinghor = 'Сейчас ' + timetoghor(h,m)
    bot.sendMessage(chat_id=update.message.chat_id, text=timeinghor)
    
    
def ghorleft(bot, update):
    h, m = dt.now().hour, dt.now().minute
    if h == 8 or (h == 9 and m <= 25):
        bot.sendMessage(chat_id=update.message.chat_id, text='До конца пары осталось:\n'\
        +timetoghor(0,(9-h)*60+30-m))
    elif h == 9 and m >= 50 or h == 10 or h == 11 and m <= 15:
        bot.sendMessage(chat_id=update.message.chat_id, text='До конца пары осталось:\n'
        +timetoghor(0,(11-h)*60+20-m))
    elif h == 11 and m >= 30 or h == 12:
        bot.sendMessage(chat_id=update.message.chat_id, text='До конца пары осталось:\n'\
        +timetoghor(0,(13-h)*60-m))
    else:
        bot.sendMessage(chat_id=update.message.chat_id,\
        text='Не мопси! Сникерсни!')


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
start_handler = CommandHandler('start', start)
ghor_handler = MessageHandler(Filters.text, dialog)
update.dispatcher.add_handler(ghor_handler)
update.dispatcher.add_handler(start_handler)
update.start_polling()

