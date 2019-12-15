import math


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class ksztalt2D:
    def obwod(self) -> float:
        # pass
        raise NotImplemented

    def show(self):
        print(f"Obwod figury wynosi {self.obwod()}")


class Kolo(ksztalt2D):
    def __init__(self, Sr: Punkt, r=1):
        self.Sr: Punkt = Sr
        self.r: float = r

    def obwod(self) -> float:
        return 2 * self.r * math.pi


class Trojkat(ksztalt2D):
    def __init__(self, A: Punkt = None, B: Punkt = None, C: Punkt = None):

        self.A: Punkt = A
        self.B: Punkt = B
        self.C: Punkt = C

        if A is None:
            self.A: Punkt = Punkt(0, 0)
        if B is None:
            self.B: Punkt = Punkt(2, -2)
        if C is None:
            self.C: Punkt = Punkt(2, 2)
        self.__a: float = 0
        self.__b: float = 0
        self.__c: float = 0

        self.__boki()

    @classmethod
    def create_from_numbers(cls, Ax: float = 0, Ay: float = 0, Bx: float = 2, By: float = -2, Cx: float = 2,
                            Cy: float = 2):
        return cls(A=Punkt(Ax, Ay), B=Punkt(Bx, By), C=Punkt(Cx, Cy))

    def __boki(self):
        self.__a = self.B.distance(self.C)
        self.__b = self.C.distance(self.A)
        self.__c = self.A.distance(self.B)

    def get_a(self):
        return self.__a

    def set_A(self, A: Punkt):
        self.A = A
        self.__boki()

    def get_b(self):
        return self.__b

    def set_b(self, B: Punkt):
        self.B = B
        self.__boki()

    def get_c(self):
        return self.__c

    def set_c(self, C: Punkt):
        self.C = C
        self.__boki()

    def obwod(self) -> float:
        return self.__a + self.__b + self.__c

    def __repr__(self):
        return f'A{self.A}, B{self.B}, C{self.C}\na={self.__a}, b={self.__b}, c={self.__c}'


if __name__ == '__main__':
    p1 = Punkt(2, 2)
    p2 = Punkt(4, 4)
    p3 = Punkt(10, 20)
    t1 = Trojkat(p1, p2, p3)
    print(t1)
    t1.set_A(Punkt(3, 8))
    print(t1)

    with open('wyniki.txt', 'w') as f:
        data = f'{t1.get_a()}, {t1.get_b()}, {t1.get_c()}'
        f.write(data)

    t1.show()

    k1 = Kolo(p2, 2)

    k1.show()
