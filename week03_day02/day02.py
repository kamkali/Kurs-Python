# Class reminder
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)


def vector_test():
    v1 = Vector2D(3,4)
    print(v1)
    print(v1.abs())


if __name__ == '__main__':
    vector_test()
