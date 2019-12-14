def triangle(h: int, a: int, char='*'):
    for i in range(0, h):
        j = round(i * (a / h))
        print(char * j if j != 0 else char)


def fibonacci(n: int):
    if n < 0:
        raise ValueError('N is lower than zero')
    if n == 0:
        return 0
    if n == 1:
        return 1

    first, second = 0, 1
    for _ in range(n - 1):
        first, second = second, first + second
    return second


def pesel_info(pesel_nr: str):
    if len(pesel_nr) != 11:
        raise RuntimeError("Wrong pesel format")

    birth_date, series_nr, fcs = pesel_nr[:6], pesel_nr[6:10], pesel_nr[-1]

    def calculate_fcs(pesel_nr: str):
        calculated_fcs = 0
        wage = [9, 7, 3, 1]
        pesel_nr = pesel_nr[:-1]
        i = 0
        for num in pesel_nr:
            calculated_fcs += int(num) * wage[i]
            i = i + 1 if i < 3 else 0
        return calculated_fcs % 10

    def find_sex(series_nr: str):
        female_sex = [0, 2, 4, 6, 8]
        return "F" if int(series_nr[-1]) in female_sex else "M"

    def format_bith_date(birth_date: str):
        year = birth_date[0:2]
        day = birth_date[4:6]
        month = birth_date[2:4]
        val = int(month) // 20
        month = str(int(month % 20)) if (int(month) % 20) > 10 else "0" + str(int(month) % 20)
        century_dict = {0: "19", 1: "20", 3: "21", 4: "18"}
        return f'{century_dict[val] + year}.{month}.{day}'

    fcs = int(fcs)
    if fcs != calculate_fcs(pesel_nr):
        raise RuntimeError(f"Calculated checksum differs from given one (should be {calculate_fcs(pesel_nr)})")

    # return birth_date, series_nr, fcs, find_sex(series_nr)
    return f"{format_bith_date(birth_date)}-{find_sex(series_nr)}"


if __name__ == '__main__':
    # print(fibonacci(19))
    print(pesel_info('98250710932'))
