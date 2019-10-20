def valid_number(a=None):
    a = a if a is not None else [1, 2, 3]
    print(a)
    valid_number(1)
    valid_number()


def one_liners():
    a = 10
    b = 3 if a == 10 else 8
    c = 3 if a == 11 else 8
    print(a, b, c)

    print("\nLIST 01")
    my_list = list(range(10, 40, 2))
    print(my_list)
    d = [2 * x for x in my_list]
    print(f"d = {d}")

    rest = [x % 3 for x in my_list]
    print(rest)

    more_op = list(map(lambda x: str(x).count(str(1)), rest))
    print(more_op)

if __name__ == '__main__':
    one_liners()
