from dataclasses import dataclass


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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # operator == override
    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y
        self_keys = self.__dict__.keys()
        other_keys = other.__dict__.keys()
        if self_keys == other_keys:
            return all([getattr(self, k) == getattr(other, k) for k in self_keys])


def vector_test():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(3, 4)

    # print(v1)
    # print(v1.abs())

    print(v1 == v2)
    v3 = v1 + v2
    v4 = Vector2D(6, 8)
    print(v3)
    print(v3 == v4)

    vv1 = Vector2DDataclass(3, 4)
    vv2 = Vector2DDataclass(3, 4)
    # dataclass implements equals method
    print(vv1 == vv2)


if __name__ == '__main__':
    vector_test()
