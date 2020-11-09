def multiply(x, y):
    """
    :param x:
    :param y:
    :return:

    # Wrong -->
    # >>> multiply(2,3)
    # 6
    # Ok -->
    >>> multiply(2,3)
    2 * 3 = 6
    6
    """
    result = x * y
    print(f'{x} * {y} = {result}')
    return result


def silnia(n: int) -> int:
    """
    Funkcja licząca silnie z liczby naturalnej n
    :param n: wjeściowa liczba naturalna
    :return: wynik silni

    >>> silnia(0)
    1
    >>> silnia(1)
    1
    >>> silnia(2)
    2
    >>> silnia(-1)
    Traceback (most recent call last):
        ...
    ValueError: N should be grater than 0
    """
    if n < 0:
        raise ValueError("N should be grater than 0")
    elif n == 0:
        return 1
    else:
        return n * silnia(n - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=False)
