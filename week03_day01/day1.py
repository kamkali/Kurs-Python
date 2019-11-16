from typing import Sequence, List, Dict


def multiply_by(my_list, multiplier):
    return [element * multiplier for element in my_list]


def main():
    print(multiply_by([2, 4, 6], 7))


if __name__ == '__main__':
    main()
