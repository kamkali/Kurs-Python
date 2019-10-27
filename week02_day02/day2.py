from typing import List, Dict
import yaml


def read_csv(filename: str = 'athlete_events_since_2000.csv', c=';') -> List[Dict]:
    csv_list = []
    with open(filename, 'r') as f:
        keys = f.readline().strip().split(c)
        for line in f:
            values = line.strip().split(c)
            single_keys = {key: value for key, value in zip(keys, values)}
            csv_list.append(single_keys)
    return csv_list


def filter_records(input_data, key, value) -> List[Dict]:
    return [d for d in input_data if d[key] == value]


def save_csv(data: List[Dict], filename, sep):
    with open(filename, 'w') as f:
        f.write(sep.join(data[0].keys())+"\n")
        for record in data:
            f.write(sep.join(record.values()))
            f.write("\n")


if __name__ == '__main__':
    data: List[Dict] = read_csv('athlete_events_since_2000.csv', c=';')
    data = filter_records(data, key='Sport', value='Boxing')
    save_csv(data, filename='box_since_2000.csv', sep=';')
    print(yaml.dump(data[1:5]))

    # first_name = ['Kamil', 'Kuba', 'Pawel', 'Szymon', 'Ania', 'Agata', 'Ewa', 'Damian', 'Maryla', 'Asia']
    # ages = [25, 31, 44, 55, 67, 11, 23, 87, 99, 21]
    # height = [186.0, 172.0, 185.0, 182.0, 164.0, 172.0, 176.0, 176.0, 173.0, 165.0]
    #
    # print(first_name)
    # print(ages)
    # print(height)
    #
    # diction = [{'First Name': a, 'Age': b, 'Height': c} for a, b, c in zip(first_name, ages, height)]
    # print(diction)
    #
    # for d in diction:
    #     d['Age'] += 1
    #     d['First Name'] = d['First Name'].lower()
    #
    # print(diction)
