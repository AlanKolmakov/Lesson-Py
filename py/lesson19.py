import re


# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 36, "1234 567890", 80.8)
# print(p1.__dict__)
# p1.fio = "Волков Николай Николаевич"
# p1.old = 40
# p1.password = "4567 789456"
# p1.weight = 60
# print(p1.__dict__)
# print(p1.old)

# class Point(object):
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self.__color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#     @property
#     def color(self):
#         return self.__color
#
#
# class Line(Prop):
#
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self.color}, {self.get_width()}")
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self.color}, {self.get_width()}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительной")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.width)
# print(rect.height)
# rect.width = 3
# print(rect.color)
# rect.area()
# print(rect.area())


# class Liquid(object):
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density  # плотность
#
#     def edit_density(self, val):  # изменение плотности
#         self.density = val
#
#     def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
#         v = round(m/self.density, 2)
#         print(f"объем {m} кг {self.name} равен {v} m^3.")
#         return v
#
#     def calc_m(self, v):  # вычисление массы жидкости, соответствующей заданному объему
#         m = v * self.density
#         print(f"Вес {v} m^3 {self.name} составляет {m} кг.")
#         return m
#
#     def print_info(self):
#         print(f"Жидкость {self.name} (Плотность = {self.density} kg/m^3.)")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#     def calc_v(self, m):
#         v = super().calc_v(m)
#         v_alc = v * self.strength
#         print(f"Объем алкоголя в {m} кг {self.name} составляет {v_alc} m^3")
#         return v, v_alc
#
#     def calc_m(self, v):
#         m = super().calc_m(v)
#         m_alc = m * self.strength
#         print(f"Вес алкоголя {v} m^3 {self.name} составляет {m_alc} m^3")
#         return m, m_alc
#
#     def print_info(self):
#         print(f"Жидкость {self.name} (Плотность = {self.density} kg/m^3.), крепость = {self.strength:.0%}")
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
# a.edit_density(1000)
# a.print_info()
# print()
# a.calc_m(0.5)
# a.calc_v(300)
# p1 = Liquid("Wine", 1064.2)
# p1.calc_m(0.5)
# p1.calc_v(300)
