import telebot
import time
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.by import By
import requests
import json
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import imaplib
import email

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = uc.Chrome(options=chrome_options)

TOKEN = '6517309195:AAFxs6-XjRk-mjBhZUj7t1PQI7KA7Pt5jrc'
chat_id = '1398397779'
bot = telebot.TeleBot(TOKEN)

web = "https://ru-gr-services.gvcworld.eu/login/appointments/ru?lang=ru_RU"

driver.maximize_window()
driver.get(web)
wait = WebDriverWait(driver, 10)


@bot.message_handler(commands=['start'])
def start(message):
    commencement = telebot.types.InlineKeyboardMarkup(row_width=2)
    major = telebot.types.InlineKeyboardButton('1', callback_data='moscow')
    other = telebot.types.InlineKeyboardButton('1', callback_data='volgograd')
    commencement.add(major, other)

    bot.send_message(message.chat.id,
                     'Если у вас есть прописка в одном из следующих городов: Москва, Санкт-Петербург или Архангельск, нажмите цифру 1.',
                     reply_markup=commencement)


@bot.callback_query_handlers(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'moscow':
            pass
        elif call.data == 'entities':
            pass


def moscow(message):
    pass


def others(message):
    pass












