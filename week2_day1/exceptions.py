def divide_(x, y):
    """
    Jesli dzielenie przez zero to zwroc None
    """
    print(f"Dzielimy {x} przez {y}")
    try:
        val = x / y
    except ZeroDivisionError as e:
        print(f"Error: {e} – Dzielenie przez zero")
        val = None
    except TypeError as e:
        print(f"{e}")
        val = None
    else:
        print("Wszytko git")
    return val


def divide(x, y):
    """
    Jesli dzielenie przez zero to zwroc None
    """
    print(f"Dzielimy {x} przez {y}")
    try:
        val = x / y
    except Exception as e:
        print(f"Blad, komunikat = {e}")
        val = None
        return None
    else:
        print("Wszytko git")
    finally:
        print("Finally wykona sie zawsze. Nawet przy returnie i po dobrze zakonczonym programie")
    return val


def my_divide_exception(x, y):
    if y == 0:
        # raise Exception("NIE DZIEL PRZEZ ZERO")
        raise ValueError("NIE DZIEL PRZEZ ZERO")
    return x / y


if __name__ == '__main__':
    # print(divide(4, 2))
    # print()
    # print(divide(4, 0))
    # print()
    # print(divide(None, 2))
    # print()
    # print(divide(None, 0))

    print()
    my_divide_exception(2, 0)
