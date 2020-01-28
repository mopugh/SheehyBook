class Vector:
    def __init__(self, x, y):
        try:
            self.x = x
            self.y = y
        except ValueError:
            self.x = 0.0
            self.y = 0.0

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector(newx,newy)

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)


if __name__ == '__main__':
    u = Vector(3,4)
    v = Vector(3,6)

    print(u.norm())
    print(Vector(5,12).norm())
    print(u + v)
