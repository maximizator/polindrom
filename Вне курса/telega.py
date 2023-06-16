import requests
from bs4 import BeautifulSoup
import random
import telebot

bot = telebot.TeleBot("5997029630:AAFibdOZlXBA7JadfDITg1gwVj9fl-CPaOU")


def get_fact():
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    res = random.choice(html.find_all(class_="p-2 clearfix"))
    return [res.text, res.a.attrs["href"]]


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    welcome_txt = f"Что вы желаете узнать? <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    botton_1 = telebot.types.KeyboardButton("Факт")
    botton_2 = telebot.types.KeyboardButton("В рай")
    botton_3 = telebot.types.KeyboardButton("во что поиграть на компьютере?")
    botton_4 = telebot.types.KeyboardButton("Стикер")
    keyboard.add(botton_1, botton_2, botton_3, botton_4)
    bot.send_message(message.chat.id, welcome_txt, reply_markup=keyboard, parse_mode="html")


@bot.message_handler(commands=["fact"])
def send_fact(message):
    text = get_fact()
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    botton_1 = telebot.types.InlineKeyboardButton("Перейти...", url=text[1])
    keyboard.add(botton_1)
    bot.send_message(message.chat.id, text[0], reply_markup=keyboard)


@bot.message_handler(commands=["img"])
def send_img(message):
    number_img = random.randint(18, 20)
    img = open(f"{number_img}_Games.jpeg", "rb")
    bot.send_photo(message.chat.id, img)


@bot.message_handler()
def message_replay(message):
    if "аудио" in message.text.lower():
        song = open("test_1.mp3", "rb")
        bot.send_audio(message.chat.id, song)
    elif "Факт" == message.text:
        send_fact(message)
    elif "во что поиграть на компьютере?" == message.text.lower():
        send_img(message)
    elif message.text == "Во что поиграть на компьютере?".lower():
        bot.send_message(message.chat.id, "Лучшая игра в 2023 году - World of Tanks")
    elif message.text == "жанр игры - шутер".lower():
        bot.send_message(message.chat.id, "Лучший шутер в 2023 году - Call of Duty")
    elif message.text == "жанр игры - хоррор".lower():
        bot.send_message(message.chat.id, "Лучший хоррор в 2023 году - Layers of Fear")
    elif message.text == "жанр игры - симулятор".lower():
        bot.send_message(message.chat.id, "Лучший симулятор в 2023 году - Fifa 2023")
    elif message.text == "жанр игры - хоррор".lower():
        bot.send_message(message.chat.id, "Лучший хоррор в 2023 году - Layers of Fear")
    elif message.text == "жанр игры - стратегия".lower():
        bot.send_message(message.chat.id, "Лучший жанр игры по стратегии в 2023 году - Total war")
    elif "Стикер" == message.text:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHlBdj3VbC4SObp9iuvy60BehyA81uHwACwSIAAny3IErc54RP4LUOdC4E")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode="html")




bot.polling(none_stop=True)