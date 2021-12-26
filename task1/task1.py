import csv
import sys


def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python task1.py massive_lenth_argument step_lenth_argument")

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    steps = []

    steps.append(1)
    l = 1
    a = 0
    while a != 1:
        if l+m-1 <= n:
            l = l+m-1
            steps.append(l)
            a = l
            print(a)
        elif l+m-1 > n:
            l = l - n + m - 1
            steps.append(l)
            a = l
            print(a)

    print (*steps)
