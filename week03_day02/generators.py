def test_range():
    a = range(10)
    print(a)
    print(list(a))


def my_generator(filename='box_since_2000_simple.csv'):
    print('\tStart generator')
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(';')
        for line in enumerate(f):
            print("\tStart single line")
            line = line.strip()
            values = line.split(';')
            single_dict = {key: value for key, value in zip(keys, values)}
            yield single_dict
            print("\tEnd single line")


def reading_generator(file, keys):
    for line in file:
        print("\tStart single line")
        line = line.strip()
        values = line.split(';')
        single_dict = {key: value for key, value in zip(keys, values)}
        yield single_dict
        print("\tEnd single line")


def file_generator01(filename):
    print('\tStart generator')
    with open(filename, 'r') as file:
        print('\tOpened file')
        keys = file.readline().strip().split(';')
        yield from reading_generator(file, keys)


def test_generator():
    results = file_generator01(filename='box_since_2000_simple.csv')
    print(type(results))
    print('\tStart loop')
    for single_dict in results:
        print(single_dict)


def my_enumerate(to_enum, start=0):
    i = start
    for element in to_enum:
        yield i, element
        i += 1


def restrict(data, end):
    for d in data:
        if end != 0:
            yield d
            end -= 1


def test_my_enum():
    colors = ['white', 'black', 'red', 'blue', 'yellow']

    # for i, c in my_enumerate(colors, 7):
    #     print(i, c)

    for c in restrict(colors, 3):
        print(c)


if __name__ == '__main__':
    # test_range()
    # test_generator()
    test_my_enum()
