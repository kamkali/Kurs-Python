from typing import Sequence


def mean(x):
    summary = 0
    for i in x:
        summary += i
    return summary / len(x)


def mean2(x: Sequence[float]):
    return sum(x) / len(x)


def mean_sdv(x: Sequence[float]) -> (float, float):
    return mean2(x), (mean2([i ** 2 for i in x]) - mean2(x) ** 2) ** (1 / 2)


def cars(models, colors):
    return [f"{color} {model}" for color, model in zip(colors, models)]


def cars_year(models, colors, year_start):
    return [f"{color} {model} {year_start+i}" for i, (color, model) in enumerate(zip(colors, models))]


if __name__ == '__main__':
    # print(mean([2, 2]))
    # print(mean2([1, 2, 2, 3]))

    print((mean_sdv([1, 2, 2, 3])))
    print((2 ** (1 / 2)) / 2)
    print(cars(models=['Volvo', 'Skoda', 'BMW'], colors=['Red', 'Blue', 'Green', 'Black']))
    print(cars_year(models=['Volvo', 'Skoda', 'BMW'], colors=['Red', 'Blue', 'Green', 'Black'], year_start=1994))

