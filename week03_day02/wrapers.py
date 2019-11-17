import functools
import time

ENABLE_WRAPPER = True

GLOBAL_TIME = time.ctime(time.time())


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


def wrapper_with_message(message):
    def proper_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return proper_wrapper


def time_wrapper(filename):
    def save_wrapper(func):
        @functools.wraps(func)
        def wraps(*args, **kwargs):
            with open(filename, 'a+') as f:
                f.write('function,time,' + GLOBAL_TIME + '\n')

                start_time = time.time()

                fun_result = func(*args, **kwargs)

                end_time = time.time() - start_time
                f.write(func.__qualname__ + ',' + str(end_time) + '\n')
                return fun_result

        return wraps

    return save_wrapper


@wrapper_with_message(message="Hello")
@time_wrapper(filename='times.csv')
def multiply(x, y):
    return x * y


@time_wrapper(filename='times.csv')
def long_func():
    for i in range(10 ** 8):
        i *= 2


def test_wrapper():
    # my_fun()
    # stime = time.time()
    # long_func()
    # dtime = time.time() - stime
    # print('Czas', dtime, 's')

    print(multiply(2, 3))
    long_func()


########################################################

if __name__ == '__main__':
    test_wrapper()
