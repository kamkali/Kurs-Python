models = ['volvo', 'toyota', 'BWM', 'Mitsubishi', 'Skoda', 'Ford']
colors = ['Red', 'Black', 'Sliver', 'Blue']
doors_count = [2, 3, 4]


def get_engine_list(minimum=1.0, maximum=2.2, step=0.1):
    engine_list = [minimum]
    while minimum <= maximum:
        minimum += step
        if minimum <= maximum:
            minimum = round(minimum, 1)
            engine_list.append(minimum)
    return engine_list


def get_engine_list2(minimum=1.0, maximum=2.2, step=0.1):
    engine_list = []
    while minimum <= maximum:
        minimum = round(minimum, 1)
        engine_list.append(minimum)
        minimum += step
    return engine_list


engines = get_engine_list(1.0, 2.3, 0.2)
print(engines)
print()
print(get_engine_list2(1.0, 2.3, 0.2))
