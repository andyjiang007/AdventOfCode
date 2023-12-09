# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:36:47 2023

@author: Andy
"""


def day9_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day9.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0

    for line in lines:
        numbers = [int(number) for number in line.split(' ')]
        last_numbers = []
        # Checking if all the numbers are 0
        while set(numbers) != {0}:
            last_numbers.append(numbers[-1])
            new_numbers = []
            for i in range(1, len(numbers)):
                new_numbers.append(numbers[i] - numbers[i - 1])
            numbers = new_numbers

        # The next number is simply the sum of all last numbers in previous rows
        #print("Adding " + str(sum(last_numbers)))
        result += sum(last_numbers)

    print("Day 9 P1 result: " + str(result))

    return


def day9_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day9.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0

    for line in lines:
        numbers = [int(number) for number in line.split(' ')]
        first_numbers = []
        while set(numbers) != {0}:
            first_numbers.append(numbers[0])
            new_numbers = []
            for i in range(1, len(numbers)):
                new_numbers.append(numbers[i] - numbers[i - 1])
            numbers = new_numbers

        # The previous number is the difference between the first numbers of even and odd rows
        final_num = sum(first_numbers[::2]) - sum(first_numbers[1::2])
        #print("Adding " + str(final_num))
        result += final_num

    print("Day 9 P2 result: " + str(result))
    return


def main():

    day9_pt1()
    day9_pt2()


if __name__ == "__main__":
    main()
