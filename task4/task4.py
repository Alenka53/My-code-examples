# В задании не указан формат файла с входными данными. Задание выполнено для входного файла формата csv.

import csv
import sys
import math

def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python task4.py nums.csv")

    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file)
        nums = list(reader)

    l = len(nums)

    n = []
    for j in range(0, l, 1):
        i = int(nums[j][0])
        n.append(i)

    s = sum(n)

    average = math.trunc(s/l)

    steps = []
    for j in range(0, l, 1):
        i = n[j] - average
        if i >= 0:
            steps.append(i)
        else:
            steps.append(-i)

    answer = sum(steps)
    print(answer)


main()
