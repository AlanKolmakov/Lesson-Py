import locale

locale.setlocale(locale.LC_ALL, "ru")

# seconds = time.time()
# print("Секунды с начала эпохи", seconds)
# local_time = time.ctime(seconds)
# print("Местное время:", local_time)
# res = time.localtime(seconds)
# print("Localtime:", res)
# print("Год: ", res.tm_year)  # или res[0]
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("Today is %B %d, %Y", time.localtime(1634936980)))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(str(pause) + " seconds.")

# text = input("Введите название напоминания: ")
# tm = float(input("Через сколько минут? "))
# tm = tm * 60
# time.sleep(tm)
# print(tm)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# print("Сегодня:", time.strftime("%B %d, %Y"))
# print(time.strftime("Сегодня %B %d, %Y"))

# n = Decimal("0.1")
# n = n + n + n
# print(n)

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)

# a = "hello"
# b = "hello"
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# Функции

# def hello(name):
#     print("Hello,", name)
#
#
# hello("Aleksander")


# def character_line(char1, char2, length):
#     for i in range(length):
#         if i % 2 != 0:
#             print(char2, end='')
#         else:
#             print(char1, end='')
#     print()
#
#
# character_line('+', '-', 9)
# character_line('X', '0', 7)

# def scrin1(x, y, n):
#     print((x + y) * n + x)
#
#
# scrin1("X", "O", 3)
# scrin1("+", "_", 5)

# def diff_find(x, y):
#     return x - y if x > y else x + y
#
#
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
#
# print(f"a = {num1}\nb = {num2}\nРезультат: {diff_find(num1, num2)}")

# def cube(x):
#     return x ** 3
#
#
# for i in range(1, 11):
#     print(f"{i} в кубе = {cube(i)}")

# Ряд Фибоначчи
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# fib(15)

# Написать функцию change(lst), которая принимает список и меняет местами его первый и
# последний элемент. В исходном списке минимум 2 элемента.

# Вариант 1:
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(list('слон')))

# Вариант 2:
# def change(lst):
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(list('слон')))

# def get_sum(a=5, b=4, c=2, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# Написать функцию, которая имеет количество символов = 20 и символ'-'
# в качестве аргументов по умолчанию и выводит на экран набор произвольных символов заданной длины.
# def set_params(n=20, s="_"):
#     print(s * n)
#
#
# set_params(10, '+')
# set_params(5, '*')
# set_params(15, '#')
# set_params(7, '-')
# set_params()

# def check_password(username, password, min_length=8, check_username=True):
#     if len(password) < min_length:
#         print("Пароль слишком короткий")
#     elif check_username and username in password:
#         print("Пароль содержит имя пользователя")
#     else:
#         print(f"Пароль пользователя {username} прошел все проверки")
#
#
# check_password('igor', '12345')
# check_password('igor', '12345igor')
# check_password('igor', '12345name')
# check_password('igor', '12345igor', check_username=False)

# def add_number(n):
#     print(f"Внутри функции: {n} = {id(n)}")
#     n += 1
#     print(f"После присвоения: {n} = {id(n)}")
#     return f"После присвоения: {n} = {id(n)}"
#
#
# x = 1
# print(f"{x} = {id(x)}")
# x = add_number(x)
# print(f"{x} = {id(x)}")

# def narcissistic(value):
#     lst = []
#     count = 0
#     res = 0
#     for i in str(value):
#         lst.append(int(i))
#         count += 1
#     for n in lst:
#         res += n ** count
#     return True if value == res else False

# def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))
#
#
# print(narcissistic(7), f"7 is narcissistic")
# print(narcissistic(371), f"371 is narcissistic")
# print(narcissistic(122), f"122 is not narcissistic")
# print(narcissistic(4887), f"4887 is not narcissistic")


# Кортежи (tuple)
# lst = [1, 2, 3]
# tp = (1, 2, 3)
# print(lst.__sizeof__())
# print(tp.__sizeof__())
#
# a = 1, 2, 3, 4, 5
# a = ()
# print(type(a))
# a = tuple((1, 2, 3, 4, 5))
# a = (1,)
# a = tuple('hello')
# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])

# s = tuple(int(input("-> ")) for i in range(5))
# print(s)
# s = input("Выедите по порядку без пробелов элементы кортежа: ")
# a = tuple(s)
# print(a)

# print(tuple(r.randint(0, 100) for i in range(10)))

# print(tuple(2**i for i in range(1, 13)))

# t1 = tuple('Hello')
# t2 = tuple(' World!!!')
# t3 = t1 + t2
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index("l", 3))
# for i in t3:
#     print(i, end=" ")

# def slicer(tup, num):
#     if num in tup:
#         if tup.count(num) > 1:
#             i1 = tup.index(num)
#             i2 = tup.index(num, i1 + 1)
#             return tup[i1:i2+1]
#         else:
#             return tup[tup.index(num):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# tup1 = tuple(r.randint(0, 5) for _ in range(10))
# tup2 = tuple(r.randint(-5, 0) for _ in range(10))
# tup3 = tup1 + tup2
# print(tup1)
# print(tup2)
# print(tup3, f'\nКоличество нулей: {tup3.count(0)}')

# def new_cortage(start, stop):
#     return tuple(r.randint(start, stop) for i in range(10))
#
#
# tp1 = new_cortage(0, 5)
# tp2 = new_cortage(-5, 0)
# tp3 = tp1 + tp2
# print(tp1)
# print(tp2)
# print(tp3, f'\nКоличество нулей: {tp3.count(0)}')

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4]. append('hi')
# print(t, id(t))

# def unique_tuple(x):
#     i = []
#     [i.append(item) for item in reversed(x) if item not in i]
#     return tuple(i)
#
#
# print(unique_tuple([1, 2, 3, 3, 2]))
# print(unique_tuple([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))
# print(unique_tuple((1, 2, 3, 4, 5, 6, 7)))

# Упаковка кортежа
# t = 1, 2, 3
# print(t)
# Распаковка кортежа
# t = 1, 2, 3
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = 'tom'
#     age = 25
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# a, b, c = user
# print(user)
# print(a, b, c)
#
# del user

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print(f"\nСтрана: {countryName} Население = {countryPopulation} млн.ч")
#     for city in cities:
#         cityName, cityPopulation = city
#         print(f"\tГород: {cityName} Население = {cityPopulation} млн.ч")
