# Циклы
# Вывести пустой прямоугольник, для описания контура фигуры использовать звездочки
# Вариант 1

# w = int(input("Введите ширину: "))
# h = int(input("Введите высоту: "))
# for i in range(h):
#     if i == 0 or i == h - 1:
#         for j in range(w):
#             print('*', end=' ')
#     else:
#         print('*', end=' ')
#         for j in range(1, w - 1):
#             print(' ', end=' ')
#         print('*', end=' ')
#     print()

# Вариант 2

# w = int(input("ширина: "))
# h = int(input("длина: "))
# for i in range(h):
#     for j in range(w):
#         print("* " if i == 0 or i == h - 1 or j == 0 or j == w - 1 else "  ", end="")
#     print()

# Вариант 3

# w = int(input("ширина: "))
# h = int(input("длина: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


# Списки (list)

# print([i*2 for i in "Hello"])
# print([i for i in range(1, 30) if 36 % i == 0])

# num = [8, 3, 9, 4, 1]
# print(num)
# print("Длина списка", len(num))

# print(type(num))
# print(type(["one", "two", 2, 3.5, [1, 2, 3]]))
# print(num[0])
# print(num[-1])
# num[1] = 256
# print(num)
# num[3] += 100
# print(id(num))

# s = list("Hello")  # или s = []
# print(s)

# s = [5]
# print(s)
# print(id(s))
# s.append(6)
# print(s)
# print(id(s))

# n = list(range(10, 2, -2))
# print(n)
# n2 = [10, 8, 6, 4]
# if n == n2:
#     print("Списки равны")
# else:
#     print("Списки не равны")
# print(id(n))
# print(id(n2))

# n = 5
# print([i ** 2 for i in range(0, n+1)])
# print([i * 3 for i in "list"])

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):  # если range, то мы должны работать через индекс элемента
#     print(a[i] * 2, end=" ")
#
# print()
# for i in a:
#     print(i * 2, end=" ")

# lst = [1, 2, 3, 4, 5]
# print(lst)
# print("*" * 16)
# for i in range(len(lst)):
#     lst[i] += 5
#     print(lst)


# lst = [1, 2, 3, 4, 5]
# print(lst)
# print("*" * 16)
# for i in lst:
#     i += 5
#     print(lst)

# Посчитать в списке сумму всех отрицательных элементов (список вводит пользователь)
# result = 0
# lst = ([int(input("--> ")) for i in range(int(input("Введите количество элементов в списке: ")))])
# for i in lst:
#     print(i, end=' ')
#     if i < 0:
#         result += i
# print(f"\nСумма отрицательных элементов: {result}")

# result = 0
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     if a[i] < 0:
#         result += a[i]
# print(result)

# В списке на 20 элементов посчитать количество четных элементов и найти сумму нечетных элементов.
# count = 0
# sum1 = 0
# a = list(range(21, 41))
# print(a)
# for i in a:
#     if i % 2 == 0:
#         count += 1
#     else:
#         sum1 += i
# print(f"Количество четных элементов списка:  {count}\nСумма нечетных элементов:  {sum1}")

# Найти среднее арифметическое всех ненулевых элементов введенного списка.
# a = [int(input("->  ")) for i in range(int(input("n =  ")))]
# sum1 = 0
# count = 0
# for i in a:
#     if i != 0:
#         sum1 += i
#         count += 1
# print(sum1 / count)

# a = [7, 9, 2, 1, 17]
# a[0], a[1] = a[1], a[0]

# срезы [start:stop:step]

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4:])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0, 0, 0]
# print(s)

# методы списка: в python Console dir(list), print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# append - добавляет элемент в конец списка
# s = [1, 2, 3, 4, 5, 6, 7]
# s.append(99)
# print(s)

# extend - добавляет несколько элементов в с конец списка
# s.extend([100, 101, 101])
# print(s)
# s.append('add')
# print(s)
# s.extend('add')
# print(s)


# s = list()
# s.extend(i**2 for i in range(1, 11))
# print(s)

# a = []
# for i in range(1, 11):
#     a.extend([i**2])
# print(a)


# Задача 1. Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...)

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов списка: ")))]
# for i in range(0, len(a), 2):
#     print(a[i], end=' ')


# Дан список чисел. Выведите все элементы списка которые больше предыдущего элемента.

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов списка: ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=' ')


# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=" ")


