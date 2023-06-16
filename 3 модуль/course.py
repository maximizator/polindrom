import requests
import xml.etree.ElementTree as ET


response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
xml = response.content
root = ET.fromstring(xml)
usd = root.find(".//*[@ID='R01235']/Value")
print(f'Курс доллара: {usd.text}')