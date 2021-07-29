from __future__ import division


def print_numbers(number1, number2):
    print(number1 // number2)
    print(number1 / number2)


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print_numbers(a, b)
