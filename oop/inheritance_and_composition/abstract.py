# Use Abstract Base Class to enforce class constraints
from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side * self.side


# g = GraphicShape()

c = Circle(10)
print(c.calc_area())
s = Square(15)
print(s.calc_area())