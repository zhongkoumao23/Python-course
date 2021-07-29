import math
import os
import random
import re
import sys


def logic(number):
    if number % 2 != 0:
        print("Weird")
    elif 2 <= number <= 5:
        print("Not Weird")
    elif 6 <= number <= 20:
        print("Weird")
    elif number >= 20:
        print("Not Weird")


if __name__ == '__main__':
    n = int(raw_input().strip())
    logic(n)
