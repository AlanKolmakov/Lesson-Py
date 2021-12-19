# ООП

class Point:
    """Класс для предоставления координат точек на плоскости"""
    x = 1
    y = 1

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        self.z = self.x + self.y
        print(self.z)

    def print_info(self):
        print(f"Координата x: {self.x}, Координата y: {self.y}, сумма: {self.z}")


p1 = Point()
# print(type(p1))
p1.x = 5
p1.y = 10
p1.set_coords(5, 10)
p1.print_info()
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
print("p1", p1.__dict__)
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
