# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         self.__days = days
#
#     @property
#     def season(self):
#         return self.__season
#
#
# year = Year(365, 'осень')
# year.days = 300
# print(year.days, year.season, sep='\n')


class Person:
    def __init__(self, age, name):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


person = Person(40, 'Tom')
person.name = 'TIM'
print(person.name)

del person.name
print(person.name if hasattr(person, 'name') else "Name attribute is deleted")

del person.age
print(person.age if hasattr(person, 'age') else "Age attribute is deleted")






















