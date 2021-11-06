# Исключения, Ошибки
# try-except
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n/m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Делить на 0 нельзя")
# else:
#     print("Все нормально. Вы ввели", n)
# finally:
#     print("Конец программы")
#
# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
# т.е. соединение строк. В остальных случаях ыыеденные числа суммируются.

# a, b = input("Введите значения a: "), input("Введите значения b: ")
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)

# Написать программу, которая выводит на экран только четные числа
# try:
#     print("Введите число до которого будет выполняться цикл: ")
#     user_num = int(input())
#     i = 1
#     while i <= user_num:
#         if i % 2 == 0:
#             print(i)
#         i += 1
# except ValueError:
#     print("Ошибка ввода")

# Вариант 2.
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# Написать программу, которая выводит на экран ряд из звездочек
# a = int(input("a?"))
# i = 1
# while i <= a:
#     print("*", end='')
#     i += 1

# Написать программу, которая находит сумму всех целых нечетных чисел в диапазоне, указанном пользователем.
# a = int(input("a?"))
# b = int(input("b?"))
# c = 0
# while a <= b:
#     if a % 2 != 0:
#         c += a
#     a += 1
# print(c)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Ведите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 1
# while True:
#     print("Для выхода из программы введите '0'")
#     a = int(input("Введите число: "))
#     if a == 0:
#         print(i)
#         break
#     i *= a

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i <5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# y = int(input("Введите y: "))
# for j in range(y):
#     print(" " * j + '+')


# x = int(input("Введите x: "))


# print('Таблица умножения')
#
# for a in range(1, 10):
#     for b in range(2, 10):
#         print(f'{a} * {b} = {a * b}\t', end='')
#     print('')
# else:
#     print("It's off")

# a = 1
# while a <= 10:
#     b = 1
#     while b <= 10:
#         print(f'{a} * {b} = {a * b}\t\t', end='')
#         b += 1
#     print(" ")
#     a += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i +=1

# Необходимо вывести на экран прямоугольник из чередующихся символов
# ++++++++++++++++
# ----------------
# ++++++++++++++++
# ----------------
# ++++++++++++++++

# for i in range(1, 6):
#     for j in range(1, 17):
#         print('-' if i % 2 == 0 else '+', end='')
#     print()

# вывести диагональ из звездочек

# for i in range(5):
#     print(' ' * i, "*")

# y = int(input("Введите y: "))
# for j in range(y):
#     print(" " * j + '+')


# for i in "Hello":
#     print(i, end='   ')


# for color in 'red', 'orange', 'yellow', 'green', 'blue', 1, 20, 0.3:
#     print("color: ", color)

# range(start, stop, step)

# Пользователь вводит число.
# Необходимо вывести все целые числа, на которое заданное число делится без остатка.

# x = int(input('Введите число: '))
# for i in range(1, x):
#     if x % i == 0:
#         print(i, end=' ')

# Вывести целые числа в диапазоне от 10 до 100 у которых есть две одинаковые цифры.
# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for y in range(10, 100):
#     if y % 10 == y // 10:
#         print(y, end=" ")


# for i in range(30):
#     print("+" * i)
#     for j in range(1):
#         print("-" * i)

# Задача вывести на экран прямоугольник из звездочек, ширину и высоту задает пользователь

# x = int(input('Введите ширину прямоугольника: '))
# y = int(input('Введите высоту прямоугольника: '))
# for i in range(y):
#     for j in range(x):
#         print('*', end='')
#     print()

