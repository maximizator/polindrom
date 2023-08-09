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

TOKEN = '6251292819:AAFFFrU1ds9JHIO3I_ZUMTWYWl6qSS7_p1M'
chat_id = '1398397779'
bot = telebot.TeleBot(TOKEN)

web = "https://ru-gr-services.gvcworld.eu/login/appointments/ru?lang=ru_RU"

driver.maximize_window()
driver.get(web)
wait = WebDriverWait(driver, 10)


@bot.message_handler(commands=['start'])
def start(message):
    # Бот приветсвует пользователя
    bot.send_message(message.chat.id,
                     'Привет! Я - Бот для бронирования виз.\n\n'
                     'Ищу для вас свободное место')

    element_user_code = driver.find_element(By.ID, 'username')
    element_user_code.clear()
    element_user_code.send_keys('')

    element_password = driver.find_element(By.ID, 'password')
    element_password.clear()
    element_password.send_keys('')

    sitekey = driver.find_element(by='id', value='recaptcha').get_attribute('data-sitekey')
    print(sitekey)

    api_key = "077e3810415c7e1343cdf11676bf18ca"
    solver = TwoCaptcha(api_key)
    print("Solving captcha...")
    response = solver.recaptcha(sitekey=sitekey, url=web, )

    print(f'Captcha Key: {response["code"]}')

    # Отправляет ключ Captcha в форму
    driver.execute_script(
        "document.getElementById"
        "('g-recaptcha-response').value = '{}';".format(response["code"]))

    time.sleep(10)

    login_button = driver.find_element(By.XPATH, '//*[@id="btn-login"]/span')
    login_button.click()
    time.sleep(10)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'menu-appointments-add')]")))

    new_record_button = driver.find_element(By.XPATH, "//*[contains(@class, 'menu-appointments-add')]")
    new_record_button.click()

    time.sleep(7)

    element_pasport = driver.find_element(By.ID, 'gp_passportnumber')
    element_pasport.clear()
    element_pasport.send_keys('345125878')

    element_pasport = driver.find_element(By.ID, 'gp_dateofbirth')
    element_pasport.clear()
    element_pasport.send_keys('02/04/1990')

    process_pars_free_window(message)


# Находим свободное окно
def process_pars_free_window(message):
    if message.from_user is None:
        return
    n = 0
    while n < 11:
        cookies = {
            '_ga': 'GA1.2.1554725483.1688201614',
            'cookiesession1': '678A3E10187F4118E5B0CCFB15EDA612',
            'language': 'ru',
            'country': 'RU',
            'auth_token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJMZW9uaXNicmF3bHN0YXJzIiwicm9sZSI6IlJPTEVfQVBQTElDQU5UIiwiaXNzIjoiZ3Zjdy1hcHAiLCJleHAiOjE2OTEzMDkzNjgsImlhdCI6MTY4OTUwOTM2OCwianRpIjoiM2RkN2UyNDMtYWI2OC00ODA1LWE2NGYtN2EzZWM4YmRlMjMxIn0.kFrwatrmmrWhv-xa5TBb_N9-xB00grOaFgKkBQ29JG8',
            '_ga_MDBD6SZ07F': 'GS1.2.1689682406.11.0.1689682406.60.0.0',
            'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE': 'ru',
            'JSESSIONID': '0C6588A2D4CDDC2361D7B006720880DD',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://ru-gr-services.gvcworld.eu',
            'Referer': 'https://ru-gr-services.gvcworld.eu/appointments/add',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition Yx 05)',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        # Присваиваем завтрашнюю дату
        now = datetime.now()
        tomorrow = now + timedelta(days=1 + n)
        datefrom = tomorrow.strftime('%d/%m/%Y')

        json_data = {
            'datefrom': datefrom,
            'type': 0,
            'bookingfor': 0,
            'members': 1,
            'method': 1,
            'id': 0,
            'vac': {
                'id': 46,
            },
        }

        response = requests.put(
            'https://ru-gr-services.gvcworld.eu/api/v1/periodslot/slots',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).json()
        time.sleep(10)

        # Все данные записываем в файл
        dates_ids = response.get('returnobject')
        with open('1_data_ids.json', 'w') as file:
            json.dump(dates_ids, file, indent=4, ensure_ascii=False)

        available_slots = []
        for date in dates_ids:
            if date['isavailable']:
                available_slots.append(date['starttime'])

        if available_slots:
            # Получаем минимальное значение времени
            min_time = min(available_slots)
            print(f"На дату {json_data['datefrom']} доступно окошко на бронирование: {min_time}")
            time.sleep(10)

            driver.find_element(By.ID, "datefrom").clear()
            driver.find_element(By.ID, "datefrom").send_keys(json_data['datefrom'])
            time.sleep(5)

            driver.find_element(By.ID, 'btn-search').click()
            time.sleep(5)

            driver.find_element(By.CSS_SELECTOR, f"div[slot-time='{min_time}']").click()
            time.sleep(5)

            driver.find_element(By.ID, 'btn-onetimepassword').click()
            time.sleep(8)

            process_message(message)

        else:
            n += 1
            print(f"Нет свободных окошек на {json_data['datefrom']}!")
            if n == 11:
                print('11 операций завершил!')
                time.sleep(120)
                process_pars_free_window(message)


def process_message(message):
    sms = driver.find_element(By.ID, 'onetimepassword')
    sms.clear()
    sms.send_keys()

    driver.find_element(By.ID, 'submitinfo').click()
    time.sleep(5)

    sitekey = driver.find_element(by='id', value='recaptcha').get_attribute('data-sitekey')
    print(sitekey)

    api_key = "077e3810415c7e1343cdf11676bf18ca"
    solver = TwoCaptcha(api_key)
    print("Solving captcha...")
    responses = solver.recaptcha(sitekey=sitekey, url=web)

    print(f'Captcha Key: {responses["code"]}')

    # Отправляет ключ Captcha в форму
    driver.execute_script(
        "document.getElementById('g-recaptcha-response').value = '{}';".format(responses["code"]))

    time.sleep(10)

    driver.find_element(By.ID, 'btn-new-appointment').click()
    time.sleep(10)

    imap_server = 'imap.yandex.ru'
    username = 'your_username'
    password = 'your_password'

    # Подключение к почтовому серверу
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)

    # Выбор ящика, где находятся письма
    mail.select('INBOX')

    # Поиск писем от указанного отправителя
    search_criteria = 'FROM noreply@gvcwassist.eu'
    status, message_ids = mail.search(None, search_criteria)

    # Проверка, что найдены письма от указанного отправителя
    if status == 'OK':
        message_ids = message_ids[0].split()
        # Чтение последнего письма
        latest_email_id = message_ids[-1]
        status, email_data = mail.fetch(latest_email_id, '(RFC822)')

        # Извлечение содержимого письма
        raw_email = email_data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Проверка, что письмо содержит нужный текст
        if 'Ваше бронирования на подачу заявления было успешно завершено!' in msg.get_payload():
            # Копирование содержимого письма в переменную
            email_content = msg.get_payload()
            print(email_content)

            # Парсинг min_time и json_data['datefrom']
            min_time = 10  # Значение для тестирования
            json_data = {
                'datefrom': '01 Января 2022'  # Значение для тестирования
            }

            # Проверка соответствия min_time и json_data['datefrom']
            while min_time != json_data['datefrom']:  # Ваше условие для проверки
                time.sleep(10)  # Пауза между проверками новых писем

                # Поиск новых писем от указанного отправителя
                status, message_ids = mail.search(None, search_criteria)

                if status == 'OK':
                    message_ids = message_ids[0].split()
                    for email_id in message_ids:
                        status, email_data = mail.fetch(email_id, '(RFC822)')
                        raw_email = email_data[0][1]
                        msg = email.message_from_bytes(raw_email)
                        email_content = msg.get_payload()

                        # Парсинг min_time и json_data['datefrom'] из нового письма
                        # Здесь ваш код парсинга

                        # Проверка соответствия min_time и json_data['datefrom']
                        if min_time == json_data['datefrom']:
                            print(email_content)
                            break
                else:
                    print('Ошибка при поиске писем')
    else:
        print('Не найдены письма от указанного отправителя')


    bot.send_message(message.chat.id, f'Бот забронировал под вас окно!\n\n Дата и время подачи заявления: {datetime}. Адрес визового центра:')



bot.polling(none_stop=True)
