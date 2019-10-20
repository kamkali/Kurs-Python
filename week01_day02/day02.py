from typing import List, Sequence
import itertools

models = ['Volvo', 'Toyota', 'BWM', 'Mitsubishi', 'Skoda', 'Ford']
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


def print_models(models):
    print(models)


def print_models_with_number(models):
    for a, b in enumerate(models):
        print(str(a) + ": " + str(b))


def print_models_with_number2(models):
    for a, b in enumerate(models):
        print(f"{a}: {b}")


# wrong
def print_models_with_colors_unique(models: str, colours='') -> str:
    for a, b in zip(models, colours):
        print(a + " is " + b.lower())


# type adnotation -> ok
def print_models_with_colors_unique_f(models: List[str], colours: List[str]):
    for a, b in zip(models, colours):
        print(f"{a} is {str(b).lower()}")


# lipa
def print_models_every_pair(models: List[str], colours: List[str]):
    for x in range(len(models)):
        for y in range(len(colors)):
            print(models[x], colours[y])


def print_models_every_pair(models: List[str], colours: List[str]):
    for x in models:
        for y in colors:
            print(f"{x} : {y.lower()}")


def print_models_every_pair2(models: List[str], colours: List[str]):
    for m, c in itertools.product(models, colours):
        print(f"{m} is {c.lower()}")


if __name__ == '__main__':
    print(get_engine_list2(1.0, 2.3, 0.2))
    print_models(models)
    print()
    print_models_with_number(models)
    print_models_with_number2(models)
    print()
    print_models_with_colors_unique(models, colors)
    print_models_with_colors_unique_f(models, colors)
    print()
    print()
    print_models_every_pair(models, colors)
    print()
    print()
    print_models_every_pair2(models, colors)
