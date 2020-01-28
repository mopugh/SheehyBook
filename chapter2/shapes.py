class Polygon:
    def __init__(self, sides, points):
        self._sides = sides
        self._points = list(points)
        if len(self._points) != self._sides:
            raise ValueError("Wrong number of points.")

    def sides(self):
        return self._sides

class Triangle(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 3, points)

    def __str__(self):
        return "I'm a triangle"

class Square(Polygon):
    def __init__(self, points):
        super().__init__(4, points)

    def __str__(self):
        return "I'm a square"
