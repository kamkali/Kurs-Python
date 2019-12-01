""" 1.Przeczytaj plik
    2. Utwórz osobny folder dla każdego wydarzenia (kolumna 'Games')
    3. W odpowiednim folderze utwórz osobny plik json dla każdego kraju """
import os
import json
import pathlib
import shutil


def read_csv_games(filename='box_since_2000.csv'):
    with open(filename, 'r') as f:
        f.readline()
        for column in f:
            yield column.split(sep=';').pop(8)


def read_csv_country(filename='box_since_2000.csv'):
    with open(filename, 'r') as f:
        for column in f:
            yield column.split(sep=';').pop(6)


def read_csv(filename='box_since_2000.csv'):
    with open(filename, 'r') as f:
        keys = f.readline().split(sep=';')
        for row in f:
            yield {key: row.split(sep=';')[i] for i, key in enumerate(keys)}


def mkdirs_with_game():
    for one_rec in read_csv('box_since_2000.csv'):
        os.makedirs("games/" + one_rec['Games'], exist_ok=True)
        save_yaml(one_rec, "games/" + one_rec['Games'])


def save_yaml(data, root_dir):
    with open(os.path.join(root_dir, data['Team'] + '.yaml'), 'a+') as f:
        f.write(f'- {json.dumps(data)}\n')


def copy_refactor_name():
    path = 'games/'
    os.makedirs(path + '_ALL_/', exist_ok=True)
    for directory in os.listdir(path):
        dirpath = os.path.join(path, directory)
        for file in os.listdir(dirpath):
            filepath = os.path.join(dirpath, file)
            pathparts = pathlib.Path(filepath).parts
            newpath = pathparts[-3] + '/_ALL_/' + pathparts[-1][:-5].lower() + '_' + pathparts[-2].replace(' ', '_') + '.yaml'
            shutil.copy2(filepath, newpath)


if __name__ == '__main__':
    # for r in read_csv():
    # print(r)
    # mkdirs_with_game()
    copy_refactor_name()
