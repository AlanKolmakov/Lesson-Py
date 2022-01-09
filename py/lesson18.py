# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.__old = year
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.name)
# p1.name = "Igor"
# del p1.name
# p1.name = "Alex"
# print(p1.old)
# p1.old = 31
# # del p1.old
# print(p1.__dict__)

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# a = 10
# print(Change.inc(a), Change.dec(a))
# ch = Change()
# print(ch.inc(a), ch.dec(a))
import math


#
#
# class Mat:
#     @staticmethod
#     def max_n(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def min_n(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def avr_n(a, b, c, d):
#         return round((a + b + c + d)/4, 2)
#
#     @staticmethod
#     def fact(x):
#         return math.factorial(x)
#
#
# print(Mat.max_n(3, 5, 7, 9))
# print(Mat.min_n(3, 5, 7, 9))
# print(Mat.avr_n(3, 5, 7, 9))
# print(Mat.fact(5))


# class Area:
#     count = 0
#
#     # def __init__(self):
#     #     Area.count += 1
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         p = (a + b + c) / 2
#         Area.count += 1
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area_2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print(f"Площадь треугольника по формуле Герона: {Area.triangle_area(3, 4, 5)}")
# print(f"Площадь треугольника через основание и высоту: {Area.triangle_area_2(6, 7)}")
# print(f"Площадь квадрата: {Area.square_area(7)}")
# print(f"Площадь прямоугольника: {Area.rect_area(2, 6)}")
# pl = Area()
# print(f"Площадь треугольника по формуле Герона: {pl.triangle_area(3, 4, 5)}")
# print(f"Площадь треугольника через основание и высоту: {pl.triangle_area_2(6, 7)}")
# print(f"Количество подсчетов площадей: {Area.get_count()}")

# class Date:
#     def __init__(self, day = 0, month = 0, year = 0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_validate(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day < 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# dates = [
#     '30.12.2000',
#     '30-12-2020',
#     '01.01.2021',
#     '12.31.2020'
# ]
#
# for d in dates:
#     if Date.is_date_validate(d):
#         date = Date.from_string(d)
#         st = date.string_to_db()
#         print(st)
#     else:
#         print("Неправильная дата или формат строки с датой")
# string_date = '23.10.2021'
# day, month, year = map(int, string_date.split("."))
# print(day, month, year)
# d1 = Date.from_string('23.10.2021')
# print(d1)
# print(d1.string_to_db())
# d2 = Date.from_string('21.11.2020')
# print(d2.string_to_db())
# date = Date(day, month, year)
# print(Date.string_to_db())

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num  # номер счета
        self.percent = percent
        self.value = value  # сумма в рублях
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        print(f'Состояние счета: {Account.convert(self.value, Account.rate_usd)} {Account.suffix_usd}')

    def convert_to_eur(self):
        print(f'Состояние счета: {Account.convert(self.value, Account.rate_eur)} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} были успешно начислены!")
        self.print_balance()

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}')

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f'Номер счета: #{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account('Долгих', '12345', 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
acc.add_percents()
acc.withdraw_money(3000)
acc.withdraw_money(100)
acc.add_money(5000)
acc.withdraw_money(3000)
