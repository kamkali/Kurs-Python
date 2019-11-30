import sys
import argparse


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


if __name__ == '__main__':
    # argparse_test()
    argparse_exercise()
    print("Result is:", float(sys.argv[1]) + float(sys.argv[2]))
