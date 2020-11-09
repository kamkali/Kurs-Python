from typing import Dict
import pandas as pd


def read_file(file):
    with open(file, 'r') as f:
        text = f.read()
    return text


def save_data(data: Dict[str, int], filename):
    list_data = list(data)
    list_data.sort()
    with open(filename, 'w') as f:
        for key in list_data:
            line = key + ':' + str(data[key]) + '\n'
            f.write(line)


def create_hist(data):
    hist_dict = {}

    for letter in data:
        letter = letter.lower().strip()
        if letter in hist_dict.keys():
            hist_dict[letter] += 1
        elif letter.isalnum():
            hist_dict[letter] = 1

    return hist_dict


def change(text, filename_to_save):
    data = create_hist(text)
    print(data)
    count_list = [{'letter': key, 'count': value} for key, value in data.items()]
    count_list.sort(key=lambda c: c['count'], reverse=True)

    most_sig_char1 = count_list[0]['letter']
    most_sig_char2 = count_list[1]['letter']

    text_list = list(text)
    for i in range(len(text)):
        if text_list[i] == most_sig_char1:
            text_list[i] = most_sig_char2
        elif text_list[i] == most_sig_char2:
            text_list[i] = most_sig_char1

    text = ''.join(text_list)

    with open(filename_to_save, 'w') as f:
        f.write(text)


def reverse_text(text, filename_to_save):
    reversed_text = text[::-1]

    with open(filename_to_save, 'w') as f:
        f.write(reversed_text)


if __name__ == '__main__':
    data = read_file('literki.txt')
    result = create_hist(data)
    save_data(result, 'hist.txt')

    change(data, 'zamiana.txt')

    reverse_text(data, 'reverse.txt')
