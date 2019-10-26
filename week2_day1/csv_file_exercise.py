from typing import Sequence, List, Dict


def read_csv(filename: str = 'ski_jumping_2014_medals.csv') -> List[Dict]:
    csv_list = []
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            single_keys = {key: value for key, value in zip(keys, values)}
            csv_list.append(single_keys)
    return csv_list


def print_medals(filename: str = 'ski_jumping_2014_medals.csv'):
    with open(filename, 'r') as f:
        for line in f:
            name, *_, medal = line.strip().split(',')
            print(f"{name} got {medal.lower()} medal")


if __name__ == '__main__':
    # print_medals()
    data = read_csv()
    height_list = [d['Height'] for d in data]
    print(height_list)
    # read_csv('ski_jumping_2014_medals_extended.csv')
