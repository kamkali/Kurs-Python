from enum import Enum


class Building:
    class Floor:
        def __init__(self):
            self.is_ground = False
            self.rooms_number = 0

    def __init__(self):
        self.floors = [self.Floor]
        self.wall_colour = 'white'


class Color(Enum):
    RED = '#FF0000'
    GREEN = '#00FF00'
    BLUE = '#0000FF'


def test_building():
    build = Building()
    floor = Building.Floor()


def test_enum():
    cl = Color.RED
    print(cl.value, cl.name)


if __name__ == '__main__':
    # test_building()
    test_enum()