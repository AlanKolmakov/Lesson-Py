# Парсинг сайтов
# from parse import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/type/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == "__main__":
#     main()

# Структуры данных

# a = [1, 2, 3, 4, 5, 4]  # <class 'list'> список
# print(type(a))
# b = {1, 2, 3, 4, 5, 6}  # <class 'set'> множество
# print(type(b))
# c = (1, 2, 3, 4, 5, 6)  # <class 'tuple'> кортеж
# print(type(c))
# d = {'a': 1, 'b': 2, 'c': 3}  # <class 'dict'> словарь
# print(type(d))

#  Связанные списки:
#     - односвязный (однонаправленный)  LinkedList
#     - двусвязный (двунаправленный

# x = 1
# y = 2
# z = 3
# a = [x, y, z]
#
# print("a:", id(a))
# print("a[0]:", id(a[0]))
# print("x =", id(x))
# print("a[1]:", id(a[1]))
# print("a[2]:", id(a[2]))

class Node:
    def __init__(self, elem):
        self.__data = elem  # элемент
        self.__next = None  # ссылка на следующий узел

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        val = self.head
        while val:  # val is not None:
            print(val.get_data(), end=" ")
            val = val.get_next()
        print()

    def add(self, item):
        tmp = Node(item)  # создаем элемент
        tmp.set_next(self.head)  # прикрепляем новый элемент к списку
        self.head = tmp  # адрес нового элемента помещаем в голову

    def append(self, item):
        new_item = Node(item)
        if self.head is None:
            self.head = new_item
            return

        end = self.head
        while end.get_next():  # доходим до последнего элемента
            end = end.get_next()
        end.set_next(new_item)

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def insert(self, position, item):
        if position > self.size():
            raise IndexError("Индекс находится за пределами списка.")

        current = self.head
        previous = None
        pos = 0
        if position == 0:
            self.add(item)
            return
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.get_next()
            previous.set_next(new_node)
            new_node.set_next(current)

    def search(self, item):  # поиск по значению
        current = self.head
        while current:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        if self.search(item):
            index = self.index(item)
            self.pop(index)

    def index(self, item):
        pos = 0
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return pos
            pos += 1
            current = current.get_next()
        return None

    def pop(self, position=None):
        current = self.head
        if position is None:
            current.get_data()
            self.head = current.get_next()
        elif position > self.size() - 1:
            raise IndexError("Индекс находится за пределами списка")
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.get_next()
                pos += 1
                current.get_data()
            previous.set_next(current.get_next())

    def reverse(self):
        p = self.head
        self.head = None
        while p is not None:
            p0, p = p, p.get_next()
            p0.set_next(self.head)
            self.head = p0


# temp = Node(93)
# print(temp.get_data())

temp = LinkedList()
temp.head = Node(93)
temp.list_print()
temp.add(31)
temp.add(77)
temp.list_print()

temp.append(26)
temp.append(54)
temp.list_print()
print(temp.size())
temp.insert(3, 17)
temp.list_print()
print(temp.search(17))
temp.pop(2)
temp.list_print()
print(temp.index(77))
temp.list_print()
temp.remove(17)
temp.list_print()

# двусвязный список

# class Node:
#     def __init__(self, elem, nxt=None, prev=None):
#         self.data = elem
#         self.prev = prev
#         self.next = nxt
#
#
# class DoubleLinkedList:
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail
#
#     def add(self, elem):
#         if self.head is None:
#             item = Node(elem)
#             self.head = item
#             self.tail = self.head
#         else:
#             item = Node(elem, self.head)
#             self.head.prev = item
#             self.head = self.head.prev
#
#     def print(self):
#         val = self.head
#         print("Список ссылок: ")
#         while val:
#             print(val.data)
#             val = val.next
#         print()
#
#     def is_empty(self):
#         return self.head is None and self.tail is None
#
#     def append(self, elem):
#         if self.tail is None:
#             self.add(elem)
#         else:
#             item = Node(elem, None, self.tail)
#             self.tail.next = item
#             self.tail = item
#
#     def pop(self):
#         if self.head == self.tail:
#             self.head = self.tail = None
#             return
#         self.tail = self.tail.prev
#         self.tail.next = None
#
#     def shift(self):
#         if self.head == self.tail:
#             self.head = self.tail = None
#             return
#         self.head = self.head.next
#         self.head.prev = None
#
#
# links = [
#     'http://site.ru',
#     'http://site.ru/news',
#     'http://site.ru/contacts',
#     'http://site.ru/about'
# ]
#
# link = DoubleLinkedList()
# for name in links:
#     link.add(name)
#
# while True:
#     if not link.is_empty():
#         link.print()
#     else:
#         print("Список ссылок пуст")
#     print('Меню')
#     print("1 - Добавить элемент в начало списка")
#     print("2 - Добавить элемент в конец списка")
#     print("3 - Удалить элемент их конца списка")
#     print("4 - Удалить элемент из начала списка")
#     print("0 - Выход")
#     operation = input('-> ')
#     if operation == '1':
#         a = input("Новая ссылка: ")
#         link.add(a)
#     elif operation == '2':
#         a = input("Новая ссылка: ")
#         link.append(a)
#     elif operation == '3':
#         link.pop()
#     elif operation == '4':
#         link.shift()
#     elif operation == '0':
#         print("Всего доброго!!!")
#         break

# Стек - "последний пришел - первым ушел" (LIFO).
# Очередь - "первым пришел - первым ушел" (FIFO).

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def __str__(self):
#         return f"{self.stack}"
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def size(self):
#         return len(self.stack)
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         return self.stack.pop()
#
#
# a = Stack()
# a.push(1)
# a.push(2)
# a.push(3)
# print(a)
# print(a.size())
# a.pop()
# a.pop()
# print(a)

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"{self.stack}"

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
