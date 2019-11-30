import sys
import argparse
import os


def argparse_test():
    parser = argparse.ArgumentParser("Function Description using parsers")
    parser.add_argument('abc', help='abc help')
    parser.add_argument('-f', '--force', help='force operation')
    args = parser.parse_args()
    print(args)


def argparse_exercise():
    parser = argparse.ArgumentParser("Simply adder function")
    parser.add_argument('first_num', help='First number to add', type=float)
    parser.add_argument('second_num', help='Second number to add', type=float)
    parser.parse_args()


def square_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbose:
        print("the square of {} equals {}".format(args.square, answer))
    else:
        print(answer)


def test_os():
    dirname = '..'
    for filename in os.listdir(dirname):
        print(filename)


if __name__ == '__main__':
    # argparse_test()
    # argparse_exercise()
    # print("Result is:", float(sys.argv[1]) + float(sys.argv[2]))
    # square_argparse()
    test_os()