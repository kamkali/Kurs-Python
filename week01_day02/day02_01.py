import sys
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
def print_models_with_colors_unique(models: str, colours=''):
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
        for y in colours:
            print(f"{x} : {y.lower()}")


def print_models_every_pair2(models: List[str], colours: List[str]):
    for m, c in itertools.product(models, colours):
        print(f"{m} is {c.lower()}")


def get_list_of_car(models: List[str], colors: List[str]):
    list = []
    for a, b in zip(models, colors):
        dictionary = {'model': a, 'color': b.lower()}
        list.append(dictionary)
    return list


def get_list_of_car_operations(models: List[str], colors: List[str]):
    list = []
    for a, b in zip(models, colors):
        dictionary = {'model': a, 'color': b.lower()}
        list.append(dictionary)
    list.sort(key=lambda x: x['model'])
    return list


def get_models(list_of_dicts):
    list = []
    for x in list_of_dicts:
        list.append(x.get('model'))
    return list


def get_models_short(list_of_dicts: List[dict]):
    return [diction['model'] for diction in list_of_dicts]


def get_models_2(list_of_dicts: List[dict]):
    list = []
    for i, x in enumerate(list_of_dicts):
        list.append({'id': i, 'model': x['model']})
    return list


def get_models_2_short(list_of_dicts):
    return [{'id': i, 'model': d['model']} for i, d in enumerate(list_of_dicts)]


def get_model_colour_unique_ex(model: List[str], colour: List[str]) -> List[dict]:
    return [{'model': m, 'color': c.lower()} for m, c in zip(model, colour)]


def rect(a, b):
    return a * b


def stars():
    list_of_tuples_or_lists = [(1, 2), (4, 10), [10, 18]]
    for d in list_of_tuples_or_lists:
        print(rect(*d))


def fibonacci_while(n=1):
    if n >= 1:
        f0 = 0
        f1 = 1
        fibonacci_list = [f0, f1]
        while n - 2 > 0:
            fibonacci_list.append(f0 + f1)
            f0, f1 = f1, f0 + f1
            n -= 1
    else:
        print("Wrong usage! N lower than 1")

    return fibonacci_list


def fibonacci_for(n=1):
    fibonacci_list = []
    if n >= 1:
        f0 = 0
        f1 = 1
        fibonacci_list = [f0, f1]
        for _ in range(n - 2):
            fibonacci_list.append(f0 + f1)
            f0, f1 = f1, f0 + f1
    else:
        print("Wrong usage! N lower than 1")

    return fibonacci_list


def draw_rectangle(height=3, width=3, char='*'):
    for _ in range(height):
        for _ in range(width):
            sys.stdout.write(char)
        print()


def draw_triangle(height=3, char='*'):
    for i in range(height):
        sys.stdout.write(char * (i + 1))
        print()


if __name__ == '__main__':
    print(fibonacci_while(10))
    print(fibonacci_for(10))
    draw_rectangle(3, 100, "-")
    print()
    draw_triangle(3, "*")
    print(get_model_colour_unique_ex(models, colors))
    stars()
    print(get_list_of_car(models, colors))
    x = get_list_of_car_operations(models, colors)
    print(x)
    print(get_models(x))
    print(get_models_short(x))
    print(get_models_2(x))
    print(get_models_2_short(x))
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
