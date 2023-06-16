# from pprint import *
# from typing import Iterator
#
# goods = [
#     {
#         'name': 'iphone 14',
#         'brand': 'Apple',
#         'price': 50_000
#     },
#     {
#         'name': 'Samsung A10',
#         'brand': 'Samsung',
#         'price': 40_000
#     },
#     {
#         'name': 'RealMe 10',
#         'brand': 'RealMe',
#         'price': 10_000
#     }
# ]


# def item_price(item):
#     return item['price']


# pprint(sorted(goods, key=lambda item: item['price']))

# for item in goods:
#     if item['brand'] == 'Apple':
#         print(item)


# apple_list = filter(lambda item: item['brand'] == 'Apple', goods)
# print(apple_list)
# print(isinstance(apple_list, Iterator))

# with open('27.txt') as f:
#     lst = [list]
# print(lst)


# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         return self.brand
#
#
# items_list = [
#     Item(1000, 'Apple'),
#     Item(1000, 'Apple'),
#     Item(1000, 'Apple'),
#     Item(1000, 'Apple'),
#     Item(1000, 'Apple'),
# ]
#
# result = list(filter(lambda x: x.brand == items_list[0].brand, items_list))[1:]


names_list = ['данил', 'артём', 'никита', 'влад']
result = list(map(lambda x: x.capitalize(), names_list))
print(result)






























