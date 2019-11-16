from typing import Sequence, List, Dict


def multiply_by(my_list, multiplier):
    return [element * multiplier for element in my_list]


def name_people(first_names: List, second_names: List, ages: List) -> List:
    return [f"{name} {surname}, age = {str(age)}" for name, surname, age in zip(first_names, second_names, ages)]


def name_people2(first_names: List, second_names: List, ages: List):
    return [{'name': f"{name} {surname}", 'age': age} for name, surname, age in zip(first_names, second_names, ages)]


def main():
    print(multiply_by([2, 4, 6], 7))
    print(name_people(['Jan', 'Julia', 'Anna'], ['Kowalski', 'Nowak', 'Kowal'], [24, 31, 16]))
    print(name_people2(['Jan', 'Julia', 'Anna'], ['Kowalski', 'Nowak', 'Kowal'], [24, 31, 16]))


if __name__ == '__main__':
    main()
