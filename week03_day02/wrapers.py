import functools
import time

ENABLE_WRAPPER = True


def simple_wrapper(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print('STOP')
        return result

    if ENABLE_WRAPPER:
        return wrap
    else:
        return func


@simple_wrapper
def my_fun():
    print("Haha")


def time_wrapper(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        start_time = time.time()

        fun_result = func(*args, **kwargs)

        end_time = time.time() - start_time
        print('Time elapsed: ', end_time, 's')
        return fun_result

    if ENABLE_WRAPPER:
        return wraps
    else:
        return func


@time_wrapper
def long_func():
    for i in range(10 ** 8):
        i *= 2


def wrapper_with_message(message):
    def proper_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return proper_wrapper


@wrapper_with_message(message="Hello")
def multiply(x, y):
    return x * y


def test_wrapper():
    # my_fun()
    # stime = time.time()
    # long_func()
    # dtime = time.time() - stime
    # print('Czas', dtime, 's')

    print(multiply(2, 3))


########################################################

if __name__ == '__main__':
    test_wrapper()
