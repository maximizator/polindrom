# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other
#
#
# item_1 = Item('Видеокарта', 25_000, 1)
# item_2 = Item('Процессор', 10_000, 2)
#
# print(item_1 + 5_000, item_2 + item_1)


from tkinter import *
from random import randint

window = Tk()
window.geometry('1500x600')
canvas = Canvas(window, width=1500, height=600)
canvas.pack()


class Fire:
    image = PhotoImage(file='fire.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay


class Water:
    image = PhotoImage(file='drop.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Starch):
            return Liquid


class Wind:
    image = PhotoImage(file='wind.png').subsample(4, 4)


class Volcano:
    image = PhotoImage(file='вулкан.png').subsample(4, 4)


class Glycerin:
    image = PhotoImage(file='глицерин.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Potassium):
            return Volcano


class Liquid:
    image = PhotoImage(file='жидкость.png').subsample(4, 4)


class Potassium:
    image = PhotoImage(file='калий.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Glycerin):
            return Volcano


class Starch:
    image = PhotoImage(file='крахмал.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Liquid


class Earth:
    image = PhotoImage(file='ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay


class Clay:
    image = PhotoImage(file='pottery.png').subsample(4, 4)


def move(event):
    image_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(image_id) == 2:
        elem_1 = elements[image_id[0] - 1]
        elem_2 = elements[image_id[1] - 1]

        new_elem = elem_1 + elem_2
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)
    canvas.coords(image_id, event.x, event.y)


elements = [Fire(), Earth(), Wind(),
            Water(), Glycerin(),
            Potassium(), Starch()]
for elem in elements:
    canvas.create_image(randint(50, 350), randint(50, 350), image=elem.image)

window.bind('<B1-Motion>', move)

window.mainloop()


# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __sub__(self, other):
#         return self.price - other.price
#
#     def __mul__(self, other):
#         return self.weight * other.weight
#
#     def __truediv__(self, other):
#         return self.price / other.weight
