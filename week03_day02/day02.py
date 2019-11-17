from dataclasses import dataclass
from matplotlib import pyplot as plt
from typing import List


# Class reminder
# 'decorator'
@dataclass()
class Vector2DDataclass:
    # \/ zamiast __init__
    x: float
    y: float = 0

    def __post_init__(self):
        self.dist = self.abs()

    def __str__(self):
        return f'({self.x},{self.y})'

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)


class Vector2D:
    def __init__(self, x, y, start=None):
        if start is None:
            start = [0, 0]
        self.x = x
        self.y = y
        self.start = [0, 0]

    def __str__(self):
        return f'({self.x},{self.y}) tail at point {self.start}'

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __add__(self, other):
        # isinstance wspiera dziedziczenie, czyli sprawdza czy other
        # jest obiektem kalsy Vector2D albo pochodnej
        if isinstance(other, Vector2D):
            x = self.x + other.x
            y = self.y + other.y
        elif isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y + other
        elif isinstance(other, list):
            if len(other) > 2:
                raise ValueError(f'Cannot add {self} and {other}')
            x = self.x + other[0]
            y = self.y + other[1]

        elif isinstance(other, tuple):
            if len(other) > 2:
                raise ValueError(f'Cannot add {self} and {other}')
            x = self.x + other[0]
            y = self.y + other[1]
        else:
            raise ValueError(f'Cannot add {self} and {other}')
        return Vector2D(x, y)

    # operator == override
    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y
        self_keys = self.__dict__.keys()
        other_keys = other.__dict__.keys()
        if self_keys == other_keys:
            return all([getattr(self, k) == getattr(other, k) for k in self_keys])
        else:
            return False

    def __len__(self):
        return self.abs()


class PlotVector2D:
    # def __init__(self):
    #     self.plot = plt.figure()

    @staticmethod
    def set_plot_v2d(vectors: List[Vector2D]):
        plt.figure()

        ax = plt.gca()
        for vec in vectors:
            ax.quiver(vec.start[0], vec.start[1], vec.x, vec.y, angles='xy', scale_units='xy', scale=1)

        ax.set_xlim([-1, max([v.x for v in vectors]) + 2])
        ax.set_ylim([-1, max([v.y for v in vectors]) + 2])

        plt.draw()
        plt.show()


def vector_test():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(3, 4)

    # print(v1)
    # print(v1.abs())

    print(v1 == v2)
    v3 = v1 + 5
    v4 = Vector2D(6, 8)
    print(v3)
    print(v3 == v4)

    print("\n", v1)
    v5 = v1 + [5, 6]
    print(v5)

    plot = PlotVector2D()
    plot.set_plot_v2d([v4, v5])

    # v6 = v1 + (5, 1)
    # print(v6)

    vv1 = Vector2DDataclass(3, 4)
    vv2 = Vector2DDataclass(3, 4)
    # dataclass implements equals method
    print(vv1 == vv2)


if __name__ == '__main__':
    vector_test()
