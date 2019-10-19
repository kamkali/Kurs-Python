# unit conversion
def convert_from_m_to_cm(meters):
    return meters * 100


def convert_to_m(value, unit='m'):
    if unit == 'm':
        return value
    elif unit == 'cm':
        return value / 100
    elif unit == 'km':
        return value * 1000
    elif unit == 'miles':
        return value * 1609.344
    elif unit == 'inch':
        return value * 0.0254
    else:
        print("Not implemented unit:")
        # raise NotImplemented()


print(convert_from_m_to_cm(1.98))
print()
print(convert_to_m(12))
print(convert_to_m(12, 'cm'))
print(convert_to_m(12, 'km'))
print(convert_to_m(12, 'miles'))
print(convert_to_m(12, 'inch'))
print(convert_to_m(12, 'ich'))

print()


def convert_course(x, unit='m'):
    multiplier = {'m': 1, 'cm': 0.01, 'km': 1000, 'mile': 1609, 'inch': 0.0254}
    return x * multiplier.get(unit, 1)


# rownanie kwadratowe
def square_function(a=1, b=0, c=0):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        x1 = x2 = -b / 2 * a
    else:
        sqr_delta = delta ** (1 / 2)

        x1 = (-b - sqr_delta) / 2 * a
        x2 = (-b + sqr_delta) / 2 * a
    return x1, x2


print(square_function(1, 6, 10))
print(square_function(1, 6, 9))
print(square_function(1, 0, -9))
