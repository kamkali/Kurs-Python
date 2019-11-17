import functools
import time

ENABLE_WRAPPER = True


def main():
    test_wrapper()


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


def time_wraper(func):
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


@time_wraper
def long_func():
    for i in range(10 ** 8):
        i *= 2


def test_wrapper():
    my_fun()
    stime = time.time()
    long_func()
    dtime = time.time() - stime
    print('Czas', dtime, 's')


########################################################

if __name__ == '__main__':
    main()
