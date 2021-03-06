# Некорректно заданы условия задачи (отсутствует переменная, задающая количество шагов), либо некорректно приведены примеры ожидаемых ответов (последний шаг не оканчивается на первом элементе в обоих примерах).
# Плюс в примере 2 некорректно указан круговой массив при заданных входных данных (в массиве по заданным условиям не должна присутствовать цифра 6), не говоря уже о синтаксисе написания.
# Задание выполнено с условиями:
# 1. Отсутствует ограничение количества шагов. 
# 2. Конец пути достигается на шаге, предшествующем шагу, концом которого становится первый элемент кругового массива.

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
            if l > 1:
                steps.append(l)
            a = l
        elif l+m-1 > n:
            l = l - n + m - 1
            if l > 1:
                steps.append(l)
            a = l

    print (*steps)


main ()
