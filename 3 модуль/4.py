# def square_generator(n):
#     for i in range(n):
#         yield i ** 2
#
#
# squares = square_generator(1_000_000)
#
# for i in range(10):
#     print(next(squares))
#
# print('------------------------------------------------------------')
#
# squares = (i**2 for i in range(1_000_000))
#
# for i in range(10):
#     print(next(squares))


from contextlib import contextmanager
from bs4 import BeautifulSoup

import requests


@contextmanager
def get_course_info(currency_id):
    try:
        response = requests.get('httpNO LINKSwww.cbr.ru/scripts/XML_daily.asp')
        soup = BeautifulSoup(response.content, features='xml')

        currency = soup.find('Valute', ID=currency_id)

        currency_name = currency.Name.text
        currency_value = currency.Value.text
        currency_nominal = currency.Nominal.text

        currency_info = f'({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.'
    except AttributeError:
        currency_info = 'Валюта не была найдена'

    yield currency_info


with get_course_info('R01010') as currency:
    print(currency)


# from xml.etree import ElementTree
# import requests
#
#
# def get_course_info(currency_id):
#     try:
#         response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
#         root = ElementTree.fromstring(response.content)
#         for currency in root.findall('Valute'):
#             if currency.get('ID') == currency_id:
#                 name = currency.find('Name').text
#                 nominal = currency.find('Nominal').text
#                 value = currency.find('Value').text
#                 currency_info = f'({nominal} шт.) {name} стоит(ят) {value} руб.'
#                 break
#
#     except:
#         currency_info = 'Ошибка при получении информации о курсе валюты'
#     return currency_info
#
#
# currency = get_course_info('R01010')
# print(currency)
