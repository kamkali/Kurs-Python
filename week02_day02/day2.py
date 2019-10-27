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


def save_csv(input_data: List[Dict], filename, sep):
    with open(filename, 'w') as f:
        keys = input_data[0].keys()
        f.write(sep.join(keys) + "\n")
        for record in input_data:
            values = [str(record[key]) for key in keys]
            f.write(sep.join(values) + "\n")


def get_unique(input_data, key):
    unique_set = set()
    for record in input_data:
        unique_set.add(record[key])
    return unique_set


def get_unique2(input_data, key):
    return set([record[key] for record in input_data])


def remove_column(input_list: List[Dict], key) -> List[Dict]:
    new_list = []
    for record in input_list:
        record.pop(key)
        new_list.append(record)
    return new_list


def remove_column2(input_list: List[Dict], key) -> List[Dict]:
    return [record.pop(key) for record in input_list]


def remove_column_no_duplicate(input_list: List[Dict], key):
    for data in input_list:
        data.pop(key)


def remove_column_dict(input_dict, key):
    for d in input_dict:  # --> dostaje liste
        remove_column_no_duplicate(d, key=key)


def str_to_float(input_data: str):
    return float(input_data) if input_data != '' else None


def str_to_int(input_data: str):
    data_float = str_to_float(input_data)
    return int(data_float) if data_float is not None else None


def type_data(list_data: List[Dict]):
    for d in list_data:
        d['ID'] = int(d['ID']) if d['ID'] != '' else None
        d['Age'] = int(float(d['Age'])) if d['Age'] != '' else None
        d['Year'] = int(float(d['Year'])) if d['Year'] != '' else None
        d['Height'] = float(d['Height']) if d['Height'] != '' else None
        d['Weight'] = float(d['Weight']) if d['Weight'] != '' else None


def type_data_simply(list_data: List[Dict]):
    for d in list_data:
        d['ID'] = str_to_int(d['ID'])
        d['Age'] = str_to_int(d['Age'])
        d['Year'] = str_to_int(d['Year'])
        d['Height'] = str_to_float(d['Height'])
        d['Weight'] = str_to_float(d['Weight'])


def result_per_country(input_list: List[Dict], year: int):
    new_dict = {}
    type_data_simply(input_list)
    filtered_list = filter_records(input_list, key='Year', value=year)
    unique_country_keys = get_unique2(filtered_list, 'Team')

    for d in unique_country_keys:
        new_dict[d] = [record for record in filtered_list if record['Team'] == d]

    # with open('results_per_country.yaml', 'w') as f:
    #     f.write(yaml.dump(new_dict))

    return new_dict


def get_podium(input_list: List[Dict]):
    return [{'Medal': team['Medal'], 'Name': team['Name']} for team in input_list if team['Medal'] != '']


def get_medal_result(input_list: List[Dict]):
    team_score = 0
    bronze, silver, gold = 1, 3, 5
    for score in input_list:
        if score['Medal'] == 'Gold':
            team_score += gold
        elif score['Medal'] == 'Silver':
            team_score += silver
        else:
            team_score += bronze
    return team_score


def get_medal_result_simply(input_list: List[Dict]):
    score_multiplier = {'Bronze': 1, 'Silver': 3, 'Gold': 5}
    list_of_scores = [score_multiplier.get(person['Medal']) for person in input_list]
    return sum(list_of_scores)


def medals_per_team(input_dict):
    medals_per_single_team = {}
    for team, result in input_dict.items():
        people_on_the_podium = get_podium(result)
        medals_per_single_team[team] = {'Podium': people_on_the_podium, 'Score': get_medal_result_simply(people_on_the_podium)}

    # with open('podium_tmp.yaml', 'w') as f:
    #     f.write(yaml.dump(medals_per_single_team))

    # print(medals_per_single_team)
    return medals_per_single_team


def sort_teams(input_medal_dict):
    result = [{'Team': key, 'Score': value['Score'], 'Podium': value['Podium']}
              for key, value in input_medal_dict.items()]
    result.sort(key=lambda x: x['Score'], reverse=True)
    return result


# def sorting_key(element):
#     return element['Score']
#
#
# def sort_teams(input_medals_per_team):
#     result = [{'Team': key, 'Score': value['Score'], 'Podium': value['Podium']}
#               for key, value in input_medals_per_team.items()]
#     result.sort(key=sorting_key, reverse=True)
#     return result


def find_best_team(data: List[Dict], year):
    result_per_team = result_per_country(data, year=year)
    medals_in_team = medals_per_team(result_per_team)
    result = sort_teams(medals_in_team)

    with open("team_sorted_result.yaml", 'w') as f:
        f.write(yaml.dump(result))


if __name__ == '__main__':
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

    # data: List[Dict] = read_csv('athlete_events_since_2000.csv', c=';')
    # data = filter_records(data, key='Sport', value='Boxing')
    # save_csv(data, filename='box_since_2000.csv', sep=';')

    country_data = read_csv(filename='box_since_2000.csv')
    unique_country = get_unique2(country_data, key="Team")
    # print(yaml.dump(list(unique_country)), len(unique_country))
    # print(unique_country)

    removed_data = read_csv(filename='box_since_2000.csv')
    removed_data = remove_column(removed_data, key="Sport")
    save_csv(removed_data, filename="box_since_2000_simple.csv", sep=';')

    # remove_data2 = read_csv(filename='box_since_2000.csv')
    # remove_data2 = remove_column(remove_data2, key="Sport")
    # save_csv(remove_data2, filename="box_since_2000_simple_2.csv", sep=';')

    # type_data(remove_data)
    # print(remove_data)
    # type_data_simply(remove_data)
    # print(remove_data)
    # per_country = result_per_country(removed_data, 2016)
    # medals = medals_per_team(per_country)
    # sort_teams(medals)
    find_best_team(removed_data, 2016)
