
# name = 'Виктор'
# age = 25
# grade = 9.2
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="")
#
# print(f"Меня Зовут {input('Введите имя :')}. Мне {input('Сколько вам лет? :')} лет.")
# print("Я учу Python")
# print("It's %s, %d. Level: %.1f" % (name, age, grade))
# print(f"It's {name}, {age}. Level: {grade}")

# print("This is a {0}. It's {1}". format("ball", "red"))

# name = input("Введите ваше имя: ")
# city = input("Введите ваш город: ")
# print("Вас зовут {0}. И ваш город {1}".format(name, city))
# print(f"Вас зовут {name}. И ваш город {city}")


# x = int(input("Введите число: "))
# y = int(input("Введите степень: "))
# print(pow(x, y))
# print(f"Результат = {int(input('Введите число: ')) ** int(input('Введите степень: '))}")
# print(f"Результат = {pow(int(input('Введите число: ')), int(input('Введите степень: ')))}")

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))

# result = (num1 + num2) / (num3 + num4)
# print("Результат: %.2f" % result)

# Boolean (Bool)
# False = False, 0, "", None
# b1 = True
# b2 = False
# print(b1 + 5) # 6
# print(b2 + 5) # 5
# print(type(b1)) # bool
# print(bool("python")) # true
# print(bool("")) # false
# print(bool(" ")) # true
# print(bool("0")) # false
# print(bool(None))

# test = None
# print(test)
# print(test is None)
# test = 5
# print(test)
# print(test is None)

# == равно
# != не равно
# > Больше
# < Меньше
# >= Больше или равно
# <= Меньше или равно

# print("привет" > "ПРИВЕТ") # true
# print(2 < 4 < 9) # true
# print(2 * 5 > 7 >= 4 + 3) # true

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# or или
# and и
# not не

# print(5 - 3 == 2 and 1 + 3 == 4) # true
# print(5 - 3 == 2 or 3 + 3 == 4) # true
# print(not 9 - 2 == 7) # false
# print(not 9 - 9)  # true


# условия

# cnt = 5
# if cnt < 10:
# 	cnt += 1  # cnt = cnt + 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#    print("Доступ на сайт разрешен")
# else:
#    print("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#    print("a > b")
# elif a < b:
#    print("b > a")
# else:
#    print("a == b")


# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#   print("Равностороний")
# elif a == b or a == c or b == c:
# 	print("Равнобедренный")
# else:
#   print("Разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     elif day == 2:
#         print("Вторник")
#     elif day == 3:
#         print("Среда")
#     elif day == 4:
#         print("Четверг")
#     elif day == 5:
#         print("Пятница")
# if day == 6 or day == 7:
#     print("Выходной день - ", end="")
# if day == 6:
#     print("Суббота")
# elif day == 7:
#     print("Воскресенье")
# else:
#     print("Такого дня недели не существует!")

# x = int(input("Введите месяц (числом) - "))
# if 1 <= x <= 12:
#     if 3 <= x <= 5:
#         print("Весна")
#     elif 6 <= x <= 8:
#         print("Лето")
#     elif 9 <= x <= 11:
#         print("Осень")
#     else:
#         print("Зима")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
# 	if n == 1:
# 		print("На ветке", n, "ворона")
# 	elif 2 <= n <= 4:
# 		print("На ветке", n, "вороны")
# 	elif 5 <= n <= 9 or n == 0:
# 		print("На ветке", n, "ворон")
# else:
# 	print("Ошибка ввода")

# Тернарный оператор
# (True) Значение if условие else значение (False)
# number = 8
# abs_number = number if number >= 0 else -number
# print(abs_number)

# a, b = 10, 20
# get_min = a if a < b else b
# print(get_min)

# a, b = 20, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")


# a, b = 10, 0
# print(a / b if b != 0 else "на ноль делить нельзя")


#  Поиск максимального значения
# def max2(x, y):
#    if x > y:
#        return x
#    return y

# def max3(x, y, z):
#    return max2(x, max2(y, z))


# print(max3(1, 2, 3))
