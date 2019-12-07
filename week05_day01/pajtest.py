import pytest
from week05_day01 import w5d1


# def test_01():
#     assert 1 == 1
#     assert 1 == 2, 'Opcjonalny opis'


# def more_values_to_test(filename):
#     values = []
#     with open(filename, 'r') as f:
#         for line in f:
#             split = line.strip().split(',')
#             val = int(split[0]), int(split[1])
#             values.append(val)
#     return values


# @pytest.mark.parametrize przyjmuje 2 argumenty:
# stringa z nazwami argumentow rozdzielanymi przecinkami
# liste tupli z wartosciami
@pytest.mark.parametrize('arg, val',
                         [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24)])  # + more_values_to_test('test_silnia_values.csv'))
def test_silnia_correct(arg, val):
    assert w5d1.silnia(arg) == val


def test_silnia_incorrect():
    # match jest opcjonalne
    with pytest.raises(ValueError):
        w5d1.silnia(-1)


# fixture sluzy do przygotowania danych do testow
# argumenty sa opcjonalne
# scope okresla jak czesto ma sie wykonac ta funkcja
# params pozwala na parametryzowanie funkcji
# jesli uzywamy params, to funkcja musi przyjmowac argument o nazwie request
# request.param to aktualna wartosc z listy params
@pytest.fixture(scope='session', params=['Volvo', 'Skoda', 'Audi'])
def prepare_data(request):
    # jakies laczenie sie z baza danych itp
    # generalnie duze przygotowanie obiektu
    print('\nSTART_PREPARE_DATA')
    yield request.param
    print('\nSTOP_PREPARE_DATA')


def test_prepared_data(prepare_data):
    assert prepare_data in ['Volvo', 'Skoda', 'BMW', 'Toyota', 'Audi']


def test_prepared_data2(prepare_data):
    assert len(prepare_data) < 100


if __name__ == '__main__':
    pass
