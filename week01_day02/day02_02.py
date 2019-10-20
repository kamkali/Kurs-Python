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

    print("\nTUPLE:")
    ex = [(x, int(x / 3), x % 3) for x in my_list]
    print(ex)
    print()

    ex1 = [{'a': x, 'b': x // 3, 'c': x % 3} for x in my_list]
    print(ex1)

    print("dictionary comprehension")
    ex1_dict = {chr(ord('a') + i): x for i, x in enumerate(my_list)}
    print(ex1_dict)

    print("dictionary comprehension 2")
    sample_keys = ['str1', 'str2', 'str3', 'str4']
    ex1_dict_2 = {key: val for key, val in zip(sample_keys, my_list)}
    print(ex1_dict_2)

    d6 = [x for x in range(10) if x % 3 == 0]
    print(d6)

    d7 = [x for x in range(100) if x % 5 == 0]
    print(d7)

    d8 = {str(x): 'podzielne przez 5' for x in range(100) if x % 5 == 0}
    print(d8)

    # raczej długie
    d9 = {str(x): 'podzielne przez 5' if x % 5 == 0 else 'niepodzielne przez 5' for x in range(100)}
    print(d9)

    print()
    more_op = list(map(lambda x: str(x).count(str(1)), ex))
    print(more_op)


if __name__ == '__main__':
    one_liners()
