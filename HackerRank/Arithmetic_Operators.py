def print_sum_numbers(number1, number2):
    print(number1 + number2)


def print_difference_numbers(number1, number2):
    print(number1 - number2)


def print_product_numbers(number1, number2):
    print(number1 * number2)


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print_sum_numbers(a, b)
    print_difference_numbers(a, b)
    print_product_numbers(a, b)