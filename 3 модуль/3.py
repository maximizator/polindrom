import requests
import xml.etree.ElementTree as ET
import vk_api

vk = vk_api.VkApi(token='vk1.a.dfbQtNUXugUh_p5tXHlQWSkBUJgrvA_n2NRV94Ij9OZZuiqGsc8jXFcmlQ-Bj4fSy-UjCEvaYco51ffcHwQbcASll1PWaak79KDllpn-qzvtqPDk8tQiuTipM0hLCECw_b7p-5IM5LvbjPPmhvSOWuUWrZhv2wafGt98lBygQmMRB9xBoaB_UqxfSDwdSnqK4cj7cTJN2Yo-f5spezxZhA')

vk._auth_token()

while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})

    if messages['count'] >= 1:
        id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']

        if message_text.lower() == 'привет':
            vk.method("messages.send", {"peer_id": id, "random_id": message_id, "message": "Привет)"})

        elif message_text.lower() == '-к валюта':
            response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
            xml = response.content
            root = ET.fromstring(xml)
            usd = root.find(".//*[@ID='R01235']/Value")
            vk.method("messages.send", {"peer_id": id, "random_id": message_id, "message": f"Курс доллара: {usd.text}"})

        else:
            vk.method("messages.send", {"peer_id": id, "random_id": message_id, "message": "Не понял запроса"})

        print(messages['items'][0])
