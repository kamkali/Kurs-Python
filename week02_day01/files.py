from typing import Sequence


def write_to_file_stupid_way():
    f = open('test_file.txt', 'w')
    f.write("TestTest")
    f.close()


def write_to_file_python_way():
    with open('test_file.txt', 'w') as f:
        f.write("Jan Kowalski\n")
        f.write("Jan Nowak\n")


def read_from_file(filename="test_file.txt"):
    with open(filename, 'r') as f:
        # nawet jak cos pojdzie nie tak to python sobie zrobi close()
        # i plik zamknie sie poprawnie
        full = f.read()
        print(f"full: \n{full}")

        with open(filename, 'r') as f:
            # nawet jak cos pojdzie nie tak to python sobie zrobi close()
            # i plik zamknie sie poprawnie
            line = f.readline()
            print(f"line: \n{line}")

        with open(filename, 'r') as f:
            # nawet jak cos pojdzie nie tak to python sobie zrobi close()
            # i plik zamknie sie poprawnie
            lines = f.readlines()
            print(f"line: \n{lines}")

        print()
        with open(filename, 'r') as f:
            # correct way
            print("correct way")
            for line in f:
                print(line, end='')


def my_print(*args, begin='', end=''):
    print(begin, end='')
    print(*args, end=end)
    # print(begin, end=end)
    # for word in args:
    #     print(word, end='')
    # print(end, end='')
    # print(begin + str(*args) + end, end='') # error


def write_cars(*args, filename):
    with open(filename, 'w') as f:
        for line in args:
            f.write(line + "\n")


def read_cars(filename) -> Sequence[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    # write_to_file_stupid_way()
    # write_to_file_python_way()
    # read_from_file()

    # print()
    # my_print('Ala', 'ma', 'kota', end=' haha\n', begin='moja funkcja: ')
    write_cars('Volvo', 'Skoda', 'BMW', filename='car_models.txt')
    print(read_cars(filename='car_models.txt'))
