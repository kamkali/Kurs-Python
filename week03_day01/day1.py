from typing import Sequence, List, Dict


def multiply_by(my_list, multiplier):
    return [element * multiplier for element in my_list]


def name_people(first_names: List, second_names: List, ages: List) -> List:
    return [f"{name} {surname}, age = {str(age)}" for name, surname, age in zip(first_names, second_names, ages)]


def name_people2(first_names: List, second_names: List, ages: List):
    return [{'name': f"{name} {surname}", 'age': age} for name, surname, age in zip(first_names, second_names, ages)]


def write_ppl_to_file(my_list: List[Dict], filename, sep=','):
    with open(filename, 'w') as f:
        for i, element in enumerate(my_list, 1):
            first, last = element['name'].split()
            gender = 'F' if first[-1] == 'a' else 'M'
            age = str(element['age'])
            f.write(sep.join((str(i), first, last, gender, age)) + '\n')


def main():
    print(multiply_by([2, 4, 6], 7))
    print(name_people(['Jan', 'Julia', 'Anna'], ['Kowalski', 'Nowak', 'Kowal'], [24, 31, 16]))
    ppls = name_people2(['Jan', 'Julia', 'Anna'], ['Kowalski', 'Nowak', 'Kowal'], [24, 31, 16])
    print(ppls)
    write_ppl_to_file(ppls, 'result.csv', ',')


if __name__ == '__main__':
    main()
