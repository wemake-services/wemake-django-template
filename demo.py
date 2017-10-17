def get_square(obj):
    return obj.square()


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return self.radius ** 2 * 3.14


class Square(object):
    def __init__(self, size):
        self.size = size

    def square(self):
        return self.size ** 2


class Cube(Square):
    def square(self):
        return 6 * super().square()



assert get_square(Cube(1)) == 6
assert get_square(Square(2)) == 4
assert get_square(Circle(3)) == 28.26
