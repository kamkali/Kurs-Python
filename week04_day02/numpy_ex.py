import numpy as np
import logger


def operations(x):
    print('\n', type(x))
    print(x)
    for i in x:
        print('\t', i)

    print('mul', 2 * x)

    x[0] = 100
    print("replace first el.", x)

    print()


def test_array():
    my_list = [3, 5, 7]
    np_arr = np.array(my_list)
    operations(my_list)
    operations(np_arr)

    # nie da sie na liscie
    print(np_arr + 3)

    print('gt', np_arr > 6)
    print('gt', (np_arr > 6) & (np_arr < 10))


"""
1. Funkcja dostaje liste albo tablice numpy
2. Do każdego el. doda 5
3. Od elementów większych niż 10 odejmie 3
4. Podniesie każdy element do kwadratu 
"""


@logger.log_exec_time
def numpy_ex_where(input_data):
    np_array = np.asarray(input_data)
    np_array = np.where(np_array > 10, np_array - 3, np_array)
    return np_array


@logger.log_exec_time
def numpy_ex(input_data):
    np_array = np.asarray(input_data)
    np_array[np_array > 10] -= 3
    return np_array


def matrix_fun(input_matrix):
    arr_2d = np.array(input_matrix)
    mul_arr = arr_2d[:, 0] * arr_2d[:, 1]
    return np.sum(mul_arr)


if __name__ == '__main__':
    # test_array()
    # logger.logger_setup()
    test_list = [10, 4, -2]
    # test_np_arr = np.array([10, 4, -2])

    # numpy_ex_where(test_list)
    # numpy_ex(test_list)

    test_list_2d = [[10, 4],
                    [-2, 8],
                    [1, 5],
                    [7, 2]]

    print(matrix_fun(test_list_2d))
