# import vk_api
# from max_dp import *
#
# token = 'vk1.a.dfbQtNUXugUh_p5tXHlQWSkBUJgrvA_n2NRV94Ij9OZZuiqGsc8jXFcmlQ-Bj4fSy-UjCEvaYco51ffcHwQbcASll1PWaak79KDllpn-qzvtqPDk8tQiuTipM0hLCECw_b7p-5IM5LvbjPPmhvSOWuUWrZhv2wafGt98lBygQmMRB9xBoaB_UqxfSDwdSnqK4cj7cTJN2Yo-f5spezxZhA'
#
# vk = vk_api.VkApi(token=token)
#
# vk._auth_token()
#
# while True:
#     messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages['count'] > 0:
#         print(messages)
#         msg = messages['items'][0]['last_message']['text']
#         id = messages['items'][0]['last_message']['from_id']
#         message_id = messages['items'][0]['last_message']['id']
#
#         if msg.lower() == 'планеты':
#             vk.method('messages.send', {'user_id': id, 'random_id': message_id, 'message': find_max_diameter_planet()})
#         else:
#             vk.method('messages.send', {'user_id': id, 'random_id': message_id, 'message': msg})


import vk_api
from max_dp import *

token = 'vk1.a.dfbQtNUXugUh_p5tXHlQWSkBUJgrvA_n2NRV94Ij9OZZuiqGsc8jXFcmlQ-Bj4fSy-UjCEvaYco51ffcHwQbcASll1PWaak79KDllpn-qzvtqPDk8tQiuTipM0hLCECw_b7p-5IM5LvbjPPmhvSOWuUWrZhv2wafGt98lBygQmMRB9xBoaB_UqxfSDwdSnqK4cj7cTJN2Yo-f5spezxZhA'

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] > 0:
        print(messages)
        msg = messages['items'][0]['last_message']['text']
        id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']

        if msg.lower() == 'корабли':
            vk.method('messages.send', {'user_id': id, 'random_id': message_id, 'message': get_starship_with_highest_atmospheric_speed()})
        else:
            vk.method('messages.send', {'user_id': id, 'random_id': message_id, 'message': msg})







