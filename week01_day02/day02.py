models = ['volvo', 'toyota', 'BWM', 'Mitsubishi', 'Skoda', 'Ford']
colors = ['Red', 'Black', 'Sliver', 'Blue']
doors_count = [2, 3, 4]


def get_engine_list(minimum=1.0, maximum=2.2, step=0.1):
    engine_list = [minimum]
    while minimum < maximum:
        minimum += step
        minimum = round(minimum, 1)
        engine_list.append(minimum)
    return engine_list


engines = get_engine_list()
print(engines)
