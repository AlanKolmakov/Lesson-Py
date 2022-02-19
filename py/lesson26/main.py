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
print(temp.search(18))
