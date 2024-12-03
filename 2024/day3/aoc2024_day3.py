# -*- coding: utf-8 -*-
"""
Created on 12/2/2024

@author: Andy
"""

import re


def day3_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day3.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in lines:
        matches = re.findall(pattern, line)
        # print(matches)
        for a, b in matches:
            result += int(a) * int(b)

    print("Day 3 P1 result: " + str(result))

    return


def day3_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day3.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    apply = True
    for line in lines:
        mul_matches = re.finditer(mul_pattern, line)
        # print(re.findall(mul_pattern, line))
        mul_pos = []
        mul_numbers = {}
        for mul in mul_matches:
            mul_pos.append(mul.start())
            a, b = mul.groups()
            mul_numbers[mul.start()] = (int(a), int(b))

        do_matches = re.finditer(do_pattern, line)
        # print(re.findall(do_pattern, line))
        do_pos = []
        for do in do_matches:
            do_pos.append(do.start())
        dont_matches = re.finditer(dont_pattern, line)
        # print(re.findall(dont_pattern, line))
        dont_pos = []
        for dont in dont_matches:
            dont_pos.append(dont.start())

        for i in range(len(line)):
            if i in do_pos:
                apply = True
            elif i in dont_pos:
                apply = False
            elif i in mul_pos:
                if apply:
                    a, b = mul_numbers[i]
                    result += a * b
                    # print(f"Adding {a=} * {b=}")
            # print(f"{i=}\t{apply=}")

    print("Day 3 P2 result: " + str(result))


def main():
    day3_pt1()
    day3_pt2()


if __name__ == "__main__":
    main()
