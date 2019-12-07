import pytest


def compute_delta(a, b, c):
    """
    Function to compute discriminant
    :param a: coefficient a
    :param b: coefficient b
    :param c: coefficient c
    :return: result of delta
    >>> compute_delta(1,0,-4)
    16
    """
    return b ** 2 - 4 * a * c


def square_roots(a, b, c):
    """
    Main function to compute roots of function
    :param a: coefficient a
    :param b: coefficient b
    :param c: coefficient c
    :return: (x1, x2) - tuple with roots
    :raise: ValueError - if delta is lower than 0
    >>> square_roots(1, 0, 100)
    Traceback (most recent call last):
        ...
    ValueError: Delta is lower than 0
    >>> square_roots(1, 0 , -9)
    (3.0, -3.0)
    """
    delta = compute_delta(a, b, c)
    if delta < 0:
        raise ValueError("Delta is lower than 0")
    elif delta == 0:
        return -b / (2 * a)
    else:
        x1, x2 = -(b - delta ** 0.5) / (2 * a), -(b + delta ** 0.5) / (2 * a)
        return x1, x2


@pytest.mark.parametrize('a, b, c, ret', [(1, 2, 3, -8), (1, 0, -9, 36)])
def test_delta(a, b, c, ret):
    assert compute_delta(a, b, c) == ret


@pytest.mark.parametrize('a, b, c, ret', [(1, 0, -9, (3.0, -3.0)), (1, 2, 1, -1)])
def test_square_roots(a, b, c, ret):
    assert square_roots(a, b, c) == ret


def test_square_roots_exception():
    with pytest.raises(ValueError):
        square_roots(1, 2, 3)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=False)
