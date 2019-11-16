import matplotlib.pyplot as plot
import numpy as np


class MyClass:
    def __init__(self):
        self.first_param = 10
        self.second_param = 20


class Person:
    def __init__(self, first_name, second_name, age=20):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def print_person_greeting(self):
        print(f"Hello, my name is {self.first_name} {self.second_name} and I am {self.age} years old")

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.age}'


class Point2D:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return f'P({self.x},{self.y})'

    def distance_to(self, p2):
        return ((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2) ** (1 / 2)

    def set_figure(self):
        fig = plot.figure()
        fig.suptitle("Point on figure")

        plot.plot(self.x, self.y, 'ro')

        plot.show()


class Point3D(Point2D):
    def __init__(self, _x, _y, _z):
        super().__init__(_x, _y)
        self.z = _z

    def __str__(self):
        return f"P({self.x},{self.y},{self.z})"


class Rectangle:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y


class RectangleInSpace:
    def __init__(self, point, rec):
        self.top_left: Point2D = point
        self.dimensions: Rectangle = rec

    # def intersection_over_union(self, other_rec_in_space):
    #     # TODO:
    #     def find_coordinates(p1, p2):
    #         left_top = Point2D(max(p1.top_left.x, p2.top_left.x), max(p1.top_left.y, p2.top_left.y))
    #
    #         right_top = Point2D(min(p1.top_left.x + p1.dimension.x, p2.top_left.x + p2.dimension.x),
    #                             min(p1.top_left.y, p2.top_left.y))
    #
    #         left_bottom = Point2D(left_top.x, max(p1.top_left.y - p1.dimension.y, p2.top_left.y - p2.dimension.y))
    #
    #         right_bottom = Point2D(right_top.x, left_bottom.y)
    #
    #         print(left_top, right_top, left_bottom, right_bottom)
    #
    #     find_coordinates(self, other_rec_in_space)


def class_testing():
    # print(MyClass)
    # my_object = MyClass()
    # print(my_object.first_param)
    #
    # person = Person('Jan', 'Kowalski', age=32)
    # person.print_person_greeting()
    # print()
    # print("Override '__str__' method which is to_string equivalent:")
    # print(person)
    #
    # print("\nPoint ex...")
    # punkt1 = Point2D(3, 4)
    # punkt1.x = 7
    #
    # punkt2 = Point2D(10, 8)
    #
    # distance = punkt1.distance_to(punkt2)
    # print(distance)
    #
    # p3 = Point3D(1, 2, 3)
    # print(p3)
    #
    # punkt2.set_figure()
    # p1 = Point2D(2, 3)
    # p2 = Point2D(2, 3)
    #
    # r1 = Rectangle(2, 2)
    # r2 = Rectangle(2, 2)
    #
    # rp1 = RectangleInSpace(p1, r1)
    # rp2 = RectangleInSpace(p2, r2)
    #
    # # rp1.intersection_over_union(rp2)


if __name__ == '__main__':
    class_testing()
