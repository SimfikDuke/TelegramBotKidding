import requests
from time import sleep, strftime, gmtime
import re

url = "https://api.telegram.org/bot490394177:AAFLj9xuY3UJA5heHaVJ1JtDZYcPwbqJcoQ/"
 
 
def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()
 
 
def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id


def get_mess(update):  
    mess = update['message']['text']
    return mess
 
def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    upd_id = last_update(get_updates_json(url))['update_id']
    while True:
        if upd_id == last_update(get_updates_json(url))['update_id']:
            chat_id = get_chat_id(last_update(get_updates_json(url)))
            mess = get_mess(last_update(get_updates_json(url)))
            if re.match(r'.*(time)|(час)|(время).*', str(mess).lower()):
                send_mess(chat_id, 'Московское время: '+ str(strftime('%H:%M:%S', gmtime())))
            else: send_mess(chat_id, 'Я не знаю, что это значит, но если это\
оскорбление, то сам ты ' + str(mess).lower())
            upd_id += 1
        sleep(1)


if __name__ == '__main__':
    main()