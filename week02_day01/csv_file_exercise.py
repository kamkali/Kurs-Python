from typing import Sequence, List, Dict
import day1
import json


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


def test_json():
    data: List[Dict] = read_csv('ski_jumping_2014_medals.csv')
    type_data(data)

    data_str = json.dumps(data)
    print(type(data_str), data_str)

    data2 = json.loads(data_str)
    print(type(data2), data2)

    with open("json_data.json", 'w') as f:
        json.dump(data, f)

    with open("json_data.json", 'r') as f:
        json.load(f)


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

    data_str = str(data).replace("'", '"')
    with open("json_example.json", 'w') as f:
        f.write(data_str)

    # with open("json_example2.json", 'w') as f:
    #     f.write(json.)

    test_json()
