from typing import Sequence, List, Dict
import day1


def print_medals(filename: str = 'ski_jumping_2014_medals.csv'):
    with open(filename, 'r') as f:
        for line in f:
            name, *_, medal = line.strip().split(',')
            print(f"{name} got {medal.lower()} medal")


def read_csv(filename: str = 'ski_jumping_2014_medals.csv') -> List[Dict]:
    csv_list = []
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(',')
        for line in f:
            values = line.strip().split(',')
            single_keys = {key: value for key, value in zip(keys, values)}
            csv_list.append(single_keys)
    return csv_list


def type_data(list_data: List[Dict]):
    for d in list_data:
        d['Age'], d['Height'], d['Weight'] = int(float(d['Age'])), float(d['Height']), float(d['Weight'])


if __name__ == '__main__':
    # print_medals()
    data = read_csv()
    type_data(data)
    height_list = [d['Height'] for d in data]
    print(height_list)

    h_mean = day1.mean_sdv(height_list)
    h_mean = round(h_mean[0], 2), round(h_mean[1], 2)
    print(h_mean)
    # read_csv('ski_jumping_2014_medals_extended.csv')
