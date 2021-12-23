# from random import randint, randrange  # *
import copy
import random as r
# import math
# import math as m
# from math import sqrt, ceil, floor
from math import *

# Списки
# s = [1, 2, 3, 4, 5, 6, 7]
# s.insert(1, 100)
# print(s)
#
# s1 = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("-> "))
#     s1.append(x)
# print(s1)

# Программа должна просить пользователя заданное количество раз ввести число кратное 3,
# проверять, действительно ли оно кратно 3. Если да, то добавлять в список, если нет,
# то выводить пользователю на экран *введенное пользователем число* не делится на 3 без остатка.
# Кол-во элементов списка: 6
# Введите число кратное 3: 9
# Введите число кратное 3: 3
# Введите число кратное 3: 5
# 5 не делится на 3 без остатка.
# Введите число кратное 3: 8
# 8 не делится на 3 без остатка.
# Введите число кратное 3: 12
# Введите число кратное 3: 1
# 1 не делится на 3 без остатка.
# [9, 3, 12]

# a = []
# n = int(input("введите количество элементов: "))
# for i in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 != 0:
#         print(f"{x} не делится на 3 без остатка")
#     else:
#         a.append(x)
# print(a)

# Создать список из двух списков так, чтобы получились только совпадающие и уникальные элементы в третьем списки
# a = [5, 9, 2, 1, 4, 3, 2, 4, 7, 8, 9, 5, 2, 2, 1, 4]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:
#     if i in c:
#         continue
#     if i in b:
#         c.append(i)
# print(c)

# Напишите функцию, которая создает комбинацию двух списков таким образом:
# [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in a:
#     c.extend([i, b[i-1]])
# print(c)

# s = [1, 100, 2, 3, 4, 5, 6, 7, 'add', 1, 2, 3, 'a', 'd', 'd']
# s[7:] = []
# print(s)  # [1, 100, 2, 3, 4, 5, 6]
#
# s.remove(100)
# print(s)

# last = s.pop()
# print(last)
# print(s)
# second = s.pop(-2)
# print(second)
# print(s)
# s.clear()
# print(s)
# del s[:]
# print(s)

# Дан список из чисел и индекс в списке k. Удалите из списка элемент с индексом k,
# сдвинув влево все элементы, стоящие правее элемента с индексом k.
# Вариант 1:
# s1 = [int(input('-> ')) for i in range(int(input('Введите элементы списка:\nn = ')))]
# k = int(input("Введите индекс:\nk = "))
# s1.pop(k) if len(s1) - 1 > k >= 0 else print('Нет такого элемента')
# print(s1)

# Вариант 2:
# print("Введите элементы списка:")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# for i in range(k + 1, len(a)):
#     a[i - 1] = a[i]
# a.pop()
# print(a)

# s = [2, 3, 6, 3, 1, 3, 20, 3, 4, 50, 3]
# print(s)
# num = s.count(3)
# print(num)
#
# ind = s.index(3)
# print(ind)

# s_copy = s.copy()
# print(s)
# print(s_copy)

# a = [1, 2, 3]
# b = a
# c = a.copy()
# print("a = ", a)
# print("b = ", b)
# print("c = ", c)
# a.append(120)
# print("a = ", a)
# print("b = ", b)
# print("c = ", c)

# Дан список из чисел и элемента в списке k. Нужно удалить этот элемент из списка
# и отсортировать по убыванию.
# s1 = [int(input('-> ')) for i in range(int(input('Введите элементы списка:\nn = ')))]
# k = int(input("Введите индекс:\nk = "))
# s1.remove(k) if k in s1 else print('Нет такого элемента')
# print(sorted(s1, reverse=True))

# Генерация случайных чисел

# print(r.randint(2, 9))
# print(r.randrange(0, 11, 2))
#
# cities = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Иркутск"]
# r.shuffle(cities)  # перемешать
# print(cities)
# print(r.choice(cities))  # выбрать один элемент
# print(r.choices(cities, k=2))  # выбрать заданное количество элементов
#
# print(round(r.uniform(10.5, 25.5), 2))  # с плавающей точкой

# mas = [r.randint(0, 10) for i in range(10)]
# print(mas)
# print("len =", len(mas))
# print("min =", min(mas))
# print("min =", max(mas))
# print("min =", sum(mas))

# Заполнить список из 10 элементов случайными числами. Найти максимальный элемент списка
# и переместить его в начало списка.

# s = [r.randint(0, 100) for i in range(10)]
# print(s)
# s.remove(max(s))
# s.insert(0, max(s))
# print(f'Max: {max(s)}\n{s}')

# Напишите программу заполнения списка положительными и отрицательными элементами.
# Из него требуется сформировать новый массив только из положительных элементов.
# Найти из них наибольший элемент. Распечатать новый массив и наибольший элемент.

# s = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print(f'Список: {s}')
# lst = [i for i in s if i > 0]
# print(f'Новый список, состоящий из положительных элементов: {lst}')
# print(f'Наибольший элемент списка: {max(lst)}')


# Заполнить список из 10 элементов случайными числами как положительными, так и отрицательными.
# Изменить этот список таким образом, чтобы все отрицательные элементы оказались в конце.

# s = [r.randint(-20, 20) for i in range(10)]
# print(s)
# s.sort(reverse=True)
# print(s)

# Заполнить список из 10 элементов случайными числами. Удалить все элементы,
# расположенные перед минимальным элементом списка.

# s = [r.randint(0, 100) for i in range(10)]
# print(f'{s}\nMin: {min(s)}\nindex min: {s.index(min(s))}')
# s = s[s.index(min(s)):]
# print(s)

# x = list('1ass26dfta6')
# print(x)
# print('a' in x)
# print('a' not in x)
#
# lst = []
# if not lst:
#     print("Список пустой")
# if len(lst) == 0:
#     print("Список пустой")

# Два списка целых заполняются случайными числами.
# Необходимо:
# Сформировать третий список, содержащий элементы обоих списков;
# Сформировать третий список, содержащий элементы обоих списков без повторений;
# Сформировать третий список, содержащий элементы общие для двух списков;
# Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.

# Введите размер первого списка: 5
# Введите размер второго списка: 4
# Первый список: [9, 3, 0, 5, 10]
# Второй список: [6, 7, 3, 10]
# Третий список: [9, , 0, 5, 10, 6, 7, 3, 10]
# Элементы обоих списков без повторений: [9, 3, 0, 5, 10, 6, 7]
# Элементы общие для двух списков: [3, 10]
# Минимальное и максимальное значение каждого из списков: [0, 3, 10, 10]

# lst1 = [r.randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# lst2 = [r.randint(0, 10) for i in range(int(input("Введите размер второго списка: ")))]
# print(f'Первый список: {lst1}\nВторой список {lst2}')
# lst3 = lst1 + lst2
# print(f'Третий список: {lst3}')
# # print(f'Элементы обоих списков без повторений: {set(lst3)}')
# lst4, lst5 = [], []
# for i in range(len(lst3)):
#     if lst3[i] not in lst4:
#         lst4.append(lst3[i])
# print(f'Элементы обоих списков без повторений: {lst4}')
# for i in lst3:
#     if i in lst1 and i in lst2 and not lst5:
#         lst5.append(i)
# print(f'Элементы общие для двух списков: {lst5}')
# print(f'Минимальное и максимальное значение каждого из списков: {min(lst1), max(lst1), min(lst2), max(lst2)}')

# user1 = ["Игорь", "Владимир", "Алла"]
# user2 = copy.deepcopy(user1)
# user2.append("Виктория")
# print(user1)
# print(user2)
# print(user1 is user2)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m)
# print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# matrix = [[x*y for x in range(1, w+1)] for y in range(1, h+1)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(f"{x} * {y} = {x*y}")

# Преобразуйте матрицу mas(n, m) таким образом, чтобы строки с нечетными индексами
# были упорядочены по убыванию, а с четными - по возрастанию.

# mas = [
#     [2, 5, 8],
#     [5, 8, 2],
#     [8, 7, 1],
#     [0, 7, 1],
#     [9, 11, 6]
# ]
#
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# for row in range(len(mas)):
#     mas[row]. sort() if row % 2 == 0 else mas[row].sort(reverse=True)
# print('*' * 10)
#
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()

# Написать программу, которая  случайным образом заполняет двумерный список
# размерностью 3х4 цифрами от -20 до 10. Необходимо найти количество
# отрицательных элементов.
# w, h, n = 3, 4, 0
# mas = [[r.randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in mas:
#     for x in row:
#         if x < 0:
#             n += 1
#         print(x, end="\t\t")
#     print()
# print(f'Количество отрицательных элементов: {n}')

# Написать программу, которая случайным образом заполняет двумерный
# список размером 6х6 цифрами от 0 до 10. Поменять местами 1-ю и 2-ю
# строки, 3-ю и 4-ю строки, 5-ю и 6-ю строки двумерного списка.
# Вариант 1:

# w, h = 6, 6
# mas = [[r.randint(0, 10) for x in range(w)] for y in range(h)]
# for f in range(2):
#     for row in range(len(mas)):
#         for col in range(len(mas[row])):
#             if f == 0:
#                 print(mas[row][col], end="\t")
#             if row % 2 == 0 and f == 1:
#                 print(mas[row+1][col], end="\t")
#             elif row % 2 != 0 and f == 1:
#                 print(mas[row-1][col], end="\t")
#         print()
#     f += 1
#     print('-' * 22)

# Вариант 1:

# h, w = 6, 6
# m = [[r.randint(0, 10) for x in range(w)] for y in range(h)]
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# row = 0
# while row < h:
#     m[row], m[row + 1] = m[row + 1], m[row]
#     row += 2
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# num1 = sqrt(2)  # Возвращает квадратный корень для указанного числа. ... x
# num2 = ceil(3.2)  # Округление в большую сторону
# num3 = floor(3.8)  # Округление в меньшую сторону
#
# print(num1)
# print(num2)
# print(num3)
# print(pi)

# radius = 2
# print("Площадь окружности: ", round(pi * (radius ** 2), 2))

# radius = int(input("Введите радиус: "))
# print("Длина окружности равна :",
#       round(2 * pi * radius, 2))

# num = -5.24
# print("Модуль числа:", fabs(num))
#
# a = 14
# b = 8
# c = 2
# print("Наибольший общий делитель a и b: ", gcd(a, b, c))

# lst = [1, 5, 3, 3.8]
# print(fsum(lst))
#
# print(fsum([0.3, 0.3, 0.3]))
# # decimal
# print(Decimal(0.3))

# перевод из радиан в градусы
# print(degrees(3.14159))
# print(cos(radians(60)))
# print(sin(radians(90)))
# print(tan(radians(0)))

# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.

# k1 = int(input("Катет 1: "))
# k2 = int(input("Катет 2: "))
# print(f'Гипотенуза: {round(sqrt(k1**2 + k2**2), 2)}')

# Вычисление площади фигур
# Выбор фигуры:
# 1 - Треугольник
# 2 - Прямоугольник
# 3 - Круг
# : 1
# Введите сторону a = 15
# Введите сторону b = 20
# Введите сторону с = 6
# 28.59

# select = int(input(f"выбор фигуры:\n1 - Треугольник\n2 - Прямоугольник\n3 - Круг\n -> "))
# if select == 3:
#     radius = int(input("Введите радиус: "))
#     print("площадь круга ", round((pi * (radius ** 2)), 2))
# elif select == 2:
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     print("Площадь прямоугольника равна ", a * b)
# elif select == 1:
#     a = int(input("Введите сторону a: "))
#     b = int(input("Введите сторону b: "))
#     c = int(input("Введите сторону c: "))
#     p = (a + b + c) / 2
#     print("Площадь треугольника равна ", round(sqrt(p * ((p - a) * (p - b) * (p - c))), 2))
# else:
#     print("Некорректное значение")

