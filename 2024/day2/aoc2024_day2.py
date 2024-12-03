# -*- coding: utf-8 -*-
"""
Created on 12/1/2024

@author: Andy
"""

import copy


def day2_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day2.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    for line in lines:
        numbers = line.split(" ")
        numbers = [int(num) for num in numbers]
        increasing = True
        safe = True
        for i in range(1, len(numbers)):
            cur = numbers[i]
            prev = numbers[i - 1]
            if abs(cur - prev) > 3 or abs(cur - prev) < 1:
                safe = False
                break
            else:
                if i == 1 and cur < prev:
                    increasing = False
                elif cur < prev and increasing:
                    safe = False
                    break
                elif cur > prev and not increasing:
                    safe = False
                    break
        if safe:
            result += 1

    print("Day 2 P1 result: " + str(result))

    return


def day2_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day2.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    for line in lines:
        numbers = line.split(" ")
        numbers = [int(num) for num in numbers]
        for removed in range(len(numbers)):
            updated = copy.deepcopy(numbers)
            updated.pop(removed)
            increasing = True
            safe = True
            for i in range(1, len(updated)):
                cur = updated[i]
                prev = updated[i - 1]
                if abs(cur - prev) > 3 or abs(cur - prev) < 1:
                    safe = False
                    break
                else:
                    if i == 1 and cur < prev:
                        increasing = False
                    elif cur < prev and increasing:
                        safe = False
                        break
                    elif cur > prev and not increasing:
                        safe = False
                        break
            if safe:
                result += 1
                print(f"Safe: {line}")
                break

    print("Day 2 P2 result: " + str(result))

    return


def main():
    day2_pt1()
    day2_pt2()


if __name__ == "__main__":
    main()
