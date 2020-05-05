import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup

dolar_url = 'https://www.google.com/search?rlz=1C1CHBD_ruUA898UA899&sxsrf=ALeKk03ccpui5t0TPismQrhLh4q4iFheWA%3A1588411112531&ei=6DqtXrb8H7LIrgTxib_4Ag&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc+&gs_lcp=CgZwc3ktYWIQAxgAMgsIABAKEAEQywEQKjIJCAAQChABEMsBMgkIABAKEAEQywEyCQgAEAoQARDLATIJCAAQChABEMsBMgkIABAKEAEQywEyCQgAEAoQARDLATICCAAyCQgAEAoQARDLATIJCAAQChABEMsBOgQIABBHOgYIIxAnEBM6BAgjECc6BQgAEIMBOgQIABBDOgQIABAKUNPgB1jL5gdg2fYHaABwAXgAgAHhAYgB4wWSAQUwLjQuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab'
evro_url = 'https://www.google.com/search?rlz=1C1CHBD_ruUA898UA899&sxsrf=ALeKk01v9myWHYK8yZ4w6Rb3G6Q1VRyPFw%3A1588411736144&ei=WD2tXvCoCJCxrgTpo5XQCw&q=%D0%BA%D1%83%D1%80%D1%81+%D1%8D%D0%B2%D1%80%D0%BE&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%8D%D0%B2%D1%80%D0%BE&gs_lcp=CgZwc3ktYWIQAzIKCAAQywEQRhCCAjIECAAQCjIECAAQCjIHCAAQChDLATIHCAAQChDLATIHCAAQChDLATIHCAAQChDLATIHCAAQChDLATIHCAAQChDLATIECAAQCjoECAAQRzoCCAA6BQgAEMsBUJuatAFYlKW0AWC2qLQBaABwAngAgAGLAYgB8QOSAQMwLjSYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjwtKjq7pTpAhWQmIsKHelRBboQ4dUDCAw&uact=5'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}

full_page = requests.get(dolar_url, headers=headers)
full_page_2 = requests.get(evro_url, headers=headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
soup_2 = BeautifulSoup(full_page_2.content, 'html.parser')
convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
convert_2 = soup_2.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

dolar = convert[0].text
evro = convert_2[0].text

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn = types.KeyboardButton('Узнать курс долара')
	btn2 = types.KeyboardButton('Узнать курс эвро')
	markup.add(btn, btn2)
	bot.send_message(message.chat.id, "Привет! Как дела?\n Хочеш узнать курс валют?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def kurs(message):
	if message.chat.type == 'private':
		if message.text == 'Узнать курс долара':
			bot.send_message(message.chat.id, "Сейчас курс долара: " + dolar + " грн")
		if message.text == 'Узнать курс эвро':
			bot.send_message(message.chat.id, "Сейчас курс эвро: " + evro + " грн")

bot.polling(none_stop=True)