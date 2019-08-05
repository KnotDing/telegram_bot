import telebot
import os
import weather
import helpdoc
import yd
import aibot
import express
import test

token = 'xxxxxxxx:XXXXXXXXXXXXXXXXXXXXX'
bot = telebot.TeleBot(token)
your_username = 'xxxxxxxxxx'
your_chat_id = 'xxxxxxxxx'
you_bot_name = 'xxxx'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '大家好，我是机器人')

@bot.message_handler(commands=['status'])
def send_welcome(message):
    bot.reply_to(message, parse_mode='MARKDOWN', text=os.popen('zsh state.sh').read())

@bot.message_handler(commands=['weather'])
def send_welcome(message):
    bot.reply_to(message, text=weather.weath(message.text))

@bot.message_handler(commands=['fanyi'])
def send_welcome(message):
    bot.reply_to(message, text=yd.fanyi(message.text))

@bot.message_handler(commands=['kuaidi'])
def send_welcome(message):
    bot.reply_to(message, text=express.searchPackage(message.text))

@bot.message_handler(commands=['test'])
def send_welcome(message):
    bot.reply_to(message, text=test.recognise(message.text))

@bot.message_handler(commands=['ai'])
def send_welcome(message):
    markup = telebot.types.ForceReply(selective=False)
    bot.reply_to(message, text=aibot.get_nlp_textchat(message.text,message.chat.id), reply_markup = markup)

@bot.message_handler(commands=['moli'])
def send_welcome(message):
    bot.reply_to(message, parse_mode='MARKDOWN', text=aibot.send_moli(message.text))

@bot.message_handler(commands=['zhihu'])
def send_welcome(message):
    bot.reply_to(message, parse_mode='MARKDOWN', text=zhihu.zhihudaily())

@bot.message_handler(commands=['drive'])
def send_welcome(message):
    os.system('zsh /root/mybot/gdrive.sh' + message.text.replace('/drive','') + ' ' + str(message.chat.id) + ' ' + str(message.message_id) + ' ' + token)

@bot.message_handler(commands=['need'])
def send_welcome(message):
    bot.send_message(your_chat_id, text=message.from_user.username+message.text.replace('/need', ''))

@bot.message_handler(commands=['shell'])
def send_welcome(message):
    if str(message.from_user.username)==your_username:
        bot.reply_to(message, os.popen(str(message.text.replace('/shell ',''))).read())

@bot.message_handler(commands=['help'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    itembtna = telebot.types.KeyboardButton('/weather')
    itembtnb = telebot.types.KeyboardButton('/fanyi s')
    itembtnc = telebot.types.KeyboardButton('/status')
    itembtnd = telebot.types.KeyboardButton('/zhihu')
    itembtne = telebot.types.KeyboardButton('/ai 好久不见')
    itembtnf = telebot.types.KeyboardButton('/moli 笑话')
    itembtng = telebot.types.KeyboardButton('/moli 月老灵签')
    markup.row(itembtna, itembtnb, itembtnc, itembtnd)
    markup.row(itembtne, itembtnf, itembtng)
    bot.reply_to(message, parse_mode='MARKDOWN', text=helpdoc.helpdocs(), reply_markup=markup)
    bot.send_message(message.chat.id, text='https://github.com/smalljiejie/telegram_bot/blob/master/README.md')

@bot.message_handler()
def send_welcome(message):
    if you_bot_name in message.text:
        markup = telebot.types.ForceReply(selective=True)
        bot.reply_to(message, text=aibot.get_nlp_textchat(message.text.replace('@'+you_bot_name+' ', ''),message.chat.id), reply_markup = markup)
    try:
        if message.reply_to_message.json['from']['username']==you_bot_name:
            markup = telebot.types.ForceReply(selective=True)
            bot.reply_to(message, text=aibot.get_nlp_textchat(message.text,message.chat.id), reply_markup = markup)
    except  AttributeError:
        print('no replay')


if __name__ == '__main__':
    bot.polling()
