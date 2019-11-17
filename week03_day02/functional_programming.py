def double_x(x):
    return 2 * x


def triple_x(x):
    return 3 * x


def modify_x(x, func):
    result = func(x)
    return result


def quadratic_eq(a, b, c):
    def delta(a, b, c):
        return b ** 2 - 4 * a * c

    x1 = -(b + delta(a, b, c) ** 0.5) / 2
    x2 = -(b - delta(a, b, c) ** 0.5) / 2

    return x1, x2


def test01():
    result = modify_x(7, double_x)
    print(result)
    result = modify_x(7, triple_x)
    print(result)

    print(quadratic_eq(1, 0, -9))

    other_ref_to_fun = modify_x

    # lambda tylko jednolinijkowa
    result = other_ref_to_fun(2, lambda x: 4 * x)

    print(result)


def test_lambda():
    func01 = lambda: print("haha")
    func01()

    func02 = lambda: ['red', 'green']
    result = func02()
    print(result)

    func03 = lambda x, y: x + y
    print(func03(2, 5))

    func04 = lambda x, y=1: x + y
    print(func04(1))

    data = [{'name': "Jan", 'age': 15},
            {'name': 'Adam', 'age': 54},
            {'name': 'Anna', 'age': 21}]

    data.sort(key=lambda x: x['age'])
    print(data)
    print(sorted(data, key=lambda x: x['name']))


def choose_func(name):
    options = {'double': double_x, 'triple': triple_x}
    return options.get(name, lambda x: x * 4)


def test_choose_function():
    result = choose_func('double')(7)
    print(result)
    result = choose_func('triple')(7)
    print(result)
    result = choose_func('no_in_dict_so_use_default_value')(7)
    print(result)


class XYZ:
    def __init__(self, x, y, func):
        self.x = x
        self.y = y
        self.func = func

    def do(self):
        return self.func(self.x, self.y)


def test_class():
    x = XYZ(2, 3, lambda x, y: x ** y)
    print(x.do())

    x.x = 5
    print(x.do())


if __name__ == '__main__':
    # test01()
    # test_lambda()
    # test_choose_function()
    test_class()
