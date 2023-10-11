import telebot, json
from config import *
from telebot import types
from models.Weather import Weather


# load language scheme
with open('data/lang.json', encoding='UTF-8') as lang_file:
    lang = json.load(lang_file)[LANG]

bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Санкт-Петербург', 'Москва')
    markup.row('Уфа', 'Казань', 'Омск')
    markup.row('Екатеринбург', 'Новосибирск')
    bot.send_message(message.chat.id, lang['welcome'], reply_markup=markup)
    weather(message)

@bot.message_handler(commands=['weather'])
def weather(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Санкт-Петербург', 'Москва')
    markup.row('Уфа', 'Казань', 'Омск')
    markup.row('Екатеринбург', 'Новосибирск')

@bot.message_handler(content_types=['text'])
def send_weather(message):
    try:
        data = Weather.get(message.text)
        result = lang['result'] % (message.text, data['temp'], data['feels_like'], data['wind_speed'], data['humidity'])
        bot.send_message(message.chat.id, result)
    except Exception as error:
        bot.send_message(message.chat.id, lang['unknown'])


# launch bot
bot.polling()
