# ООП

# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1


#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = self.x + self.y
#         print(self.z)
#
#     def print_info(self):
#         print(f"Координата x: {self.x}, Координата y: {self.y}, сумма: {self.z}")
#
#
# p1 = Point()
# # print(type(p1))
# p1.x = 5
# p1.y = 10
# p1.set_coords(5, 10)
# p1.print_info()
# Point.set_coords(p1)
# p1.z = 7
# print(getattr(p1, "x"))
# print(getattr(p1, "z", "False"))
# print(hasattr(p1, "z"))
# setattr(p1, "z", 17)
# delattr(p1, "z")
# print(p1.x, p1.y)
# Point.x = 100

# print(p1.x, p1.y)
# print(id(Point))
# print(p1.x, Point.x)
# print("p1", p1.__dict__)
#
# p2 = Point()
# p2.x = 20
# p2.y = 30
# p2.set_coords()
# print(p2.x, p2.y)
# print("p2", p2.__dict__)

# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# class Human:
#     """********* Персональные данные *********"""
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, name, date, phone, country, city, address):
#         self.name = name
#         self.birthday = date
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         """Установить имя"""
#         self.name = name
#
#     def get_name(self):
#         """Получить имя"""
#         return self.name
#
#     def set_birthday(self, birthday):
#         """Установить дату рождения"""
#         self.birthday = birthday
#
#     def get_birthday(self):
#         """Получить дату рождения"""
#         return self.birthday
#
#     def set_phone(self, phone):
#         """Установить номер телефона"""
#         self.phone = phone
#
#     def get_phone(self):
#         """Получить номер телефона"""
#         return self.phone
#
#     def set_country(self, country):
#         """Установить страну"""
#         self.country = country
#
#     def get_country(self):
#         """Получить страну"""
#         return self.country
#
#     def set_city(self, city):
#         """Установить город"""
#         self.city = city
#
#     def get_city(self):
#         """Получить город"""
#         return self.city
#
#     def set_address(self, address):
#         """Установить город"""
#         self.address = address
#
#     def get_address(self):
#         """Получить город"""
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Марина")
# h1.print_info()
# print(f"Имя: {h1.get_name()}")
# h1.set_birthday("25.05.2007")
# print(f"Дата рождения: {h1.get_birthday()}")
# h1.set_phone("89-78-45")
# print(h1.get_phone())
# h1.set_country("Беларусь")
# print(h1.get_country())
# h1.print_info()


# class AutoClass:
#     """********* Данные автомобиля *********"""
#     marka_auto = "marka"
#     year_auto = "0000"
#     fabric_auto = "fabric"
#     power_auto = ""
#     color_auto = ""
#     price_auto = ""
#
#     def print_auto_class(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.marka_auto}\nГод выпуска: {self.year_auto}\n"
#               f"Производитель: {self.fabric_auto}\nМощность двигателя: {self.power_auto}\n"
#               f"Цвет машины: {self.color_auto}\nЦена: {self.price_auto}")
#         print("=" * 40)
#
#     def input_auto_class(self, marka, year, fabric, power, color, price):
#         self.marka_auto = marka
#         self.year_auto = year
#         self.fabric_auto = fabric
#         self.power_auto = power
#         self.color_auto = color
#         self.price_auto = price
#
#     def set_auto_class(self, marka):
#         self.marka_auto = marka
#
#     def get_auto_class(self):
#         return self.marka_auto
#
#     def set_year_auto(self, year):
#         self.year_auto = year
#
#     def get_year_auto(self):
#         return self.year_auto
#
#     def set_fabric_auto(self, fabric):
#         self.fabric_auto = fabric
#
#     def get_fabric_auto(self):
#         return self.fabric_auto
#
#     def set_power_auto(self, power):
#         self.power_auto = power
#
#     def get_power_auto(self):
#         return self.power_auto
#
#     def set_color_auto(self, color):
#         self.color_auto = color
#
#     def get_color_auto(self):
#         return self.color_auto
#
#     def set_price_auto(self, price):
#         self.price_auto = price
#
#     def get_price_auto(self):
#         return self.price_auto
#
#
# h1 = AutoClass()
# h1.print_auto_class()
# h1.input_auto_class("X7 M50i", "2021", "BMW", "530 л.с.", "White", "10790000")
# h1.print_auto_class()
# h1.set_auto_class("Carina")
# h1.print_auto_class()
# print(f"Model: {h1.get_auto_class()}")
# h1.set_year_auto("2007")
# print(f"Год выпуска: {h1.get_year_auto()}")
# h1.set_fabric_auto("Toyota")
# print(f"Производитель: {h1.get_fabric_auto()}")
# h1.set_power_auto("200 л.с.")
# print(f"Мощность: {h1.get_power_auto()}")
# h1.set_color_auto("Red")
# print(f"Цвет машины: {h1.get_color_auto()}")
# h1.set_price_auto("1370000")
# print(f"Цвет машины: {h1.get_price_auto()}")
# h1.print_auto_class()

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print(f"Данные сотрудника: {self.name} {self.surname}")
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника: {self.skill}")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
# p2 = Person("Anna", "dolgih")
# p2.print_info()
# p2.add_skill(2)

# конструктор (__new__)
# инициалтзация (__init__)
# деструктор (__del__)


# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра: " + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p2 = Point()
# print(p2.__dict__)
# p3 = Point(y=2)
# print(p3.__dict__)
# # del p1  # или p1 = 0
# print(p1.x)


# class Point:
#     count = 0  # статическая переменная
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(2, 3)
# p3 = Point(1, 4)
# print(Point.count)

# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация робота: {self.name}")
#         Robot.count += 1
#
#     def __del__(self):
#         print(f"{self.name} выключается")
#         Robot.count -= 1
#
#         if Robot.count == 0:
#             print(f"{self.name} был последним")
#         else:
#             print(f"Работающих роботов осталось {Robot.count}")
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут: {self.name}")
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print(f"Численность роботов: {Robot.count}")
# print()
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print(f"Численность роботов: {Robot.count}")
# droid3 = Robot('B1-4V')
# droid3.say_hi()
#
# print(f"\nЗдесь роботы могут проделать какую-то работу\n")
#
# print(f"Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# print(f"Численность роботов: {Robot.count}")


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(1, 2)
# print(p1.get_coords())
#
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 40
# print(p1.__dict__)

# Создать класс Rectangle, описывающий прямоугольник.
# В классе должны быть все необходимые методы, а так же методы вычисления площади,
# периметра и диагонали, и метод, который рисует прямоугольник
# Длина прямоугольника: 3
# Ширина прямоугольника: 9
# Площадь прямоугольника: 27
# Периметр прямоугольника: 54
# Гипотенуза прямоугольника: 9.49
# *********
# *********
# *********

# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(z):
#         if isinstance(z,(int, float)):
#             return True
#
#     # Setters
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#         else:
#             print("Координата ширины должна быть числом")
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#         else:
#             raise ValueError("Длина должна быть числом")
#
#     # Getters
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     # площадь
#     def get_area(self):
#         return self.__length * self.__width
#
#     # периметр
#     def get_perimetr(self):
#         return 2 * (self.__length + self.__width)
#
#     # диагональ прямоугольника
#     def get_hypotenuse(self):
#         return round((self.__length**2 + self.__width**2)**.5, 2)
#
#     def get_draw(self):
#         for i in range(self.__length):
#             print("*" * self.__width)
#
#
# a = Rectangle(4, 12)
# a.set_length(3)
# a.set_width(9)
# print(f"Длина прямоугольника: {a.get_length()}")
# print(f"Ширина прямоугольника: {a.get_width()}")
# print("Площадь прямоугольника:", a.get_area())
# print("Периметр прямоугольника:", a.get_perimetr())
# print("Гипотенуза прямоугольника:", a.get_hypotenuse())
# a.get_draw()

# Вариант 2:
# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_length(self):
#         return self.a
#
#     def get_width(self):
#         return self.b
#
#     def perimeter(self):
#         return (self.a + self.b) * 2
#
#     def square(self):
#         return self.a * self.b
#
#     def hypotenuse(self):
#         return round((self.a**2 + self.b**2)**.5, 2)
#
#     def draw(self):
#         for i in range(self.a):
#             print("*" * self.b)
#
#
# r = Rectangle(10, 20)
# print(f"Длина прямоугольника: {r.get_length()}")
# print(f"Ширина прямоугольника: {r.get_width()}")
# print(f"Площадь прямоугольника: {r.square()}")
# print(f"Периметр прямоугольника: {r.perimeter()}")
# print(f"Гипотенуза прямоугольника: {r.hypotenuse()}")
# r.draw()

# class Point:
#     WIDTH = 50
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y

# def __getattr__(self, item):
#     return f"В классе {__class__.__name__} отсутствует атрибут {item}"

# def __getattribute__(self, item):
#     if item == "_Point__x":
#         return "Закрытая переменная"
#     else:
#         return object.__getattribute__(self, item)

# def __setattr__(self, key, value):
#     if key == "WIDTH":
#         raise AttributeError("Значение константы WIDTH изменять нельзя")
#     else:
#         self.__dict__[key] = value

#     def get_coords(self):
#         return self.__x, self.__y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#
# p1 = Point(1, 2)
# # print(p1.zzz)
# print(p1.get_coords_x())

# class Kgfunt:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg_funt(self):
#         return self.__kg
#
#     @kg_funt.setter
#     def kg_funt(self, kg):
#         if isinstance(kg, (int, float)):
#             self.__kg = kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# p1 = Kgfunt(12)
# print(p1.to_pound())
# p1.kg_funt = 41
# print(p1.to_pound())


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())