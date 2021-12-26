# Некорректно заданы условия задания - не указывается формат входного файла.

# Задание выполнено с условиями: 
# 1 - вводные файлы предоставляются в формате csv,
# 2 - в случае дробных значений координат они указываются в формате десятичных дробей с "." (точкой) в качестве разделителя целой и дробной частей.

import csv
import sys
import math

def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python circle_coordinates(csv) dots_coordinates(csv)")


    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        circle = list(reader)

    cx = float(circle[0][0])
    cy = float(circle[0][1])
    cr = float(circle[1][0])

    with open(sys.argv[2], 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        dots = list(reader)

    a = len(dots)

    if a < 1:
        print("No dots' coordinates found")
        quit(main)
    elif a > 100:
        print("Maximum quantity of dots = 100")
        quit(main)

    for i in range(0, a, 1):
        x = float(dots[i][0])
        y = float(dots[i][1])
        r = math.sqrt((x - cx)**2 + (y - cy)**2)
        if r == cr:
            print(0)
        elif r > cr:
            print(2)
        elif r < cr:
            print(1)

main()
