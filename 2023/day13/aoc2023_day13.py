# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:56:42 2023

@author: Andy
"""


import numpy as np


def find_mirror(current_pattern, diff):
    # For every possible mirror position
    for i in range(1, len(current_pattern)):
        count = 0
        # Part 1 is the first half but in reverse for easy comparison
        part1 = reversed(current_pattern[:i])
        part2 = current_pattern[i:]
        for r1, r2 in zip(part1, part2):
            # Count the total number of different chars between 2 lists
            count += sum(c1 != c2 for c1, c2 in zip(list(r1), list(r2)))
            if count > diff:
                # Break early when the difference is already too large
                break
        if count == diff:
            return i
    return -1


def day13_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day13.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    current_pattern = []
    lines.append("")
    for line in lines:
        if len(line) == 0:
            # print(current_pattern)
            row_mirror = find_mirror(current_pattern, 0)
            #print("Row mirror: " + str(row_mirror))
            if row_mirror >= 0:
                # If we found a row mirror position, add it
                result += row_mirror * 100
            else:
                # Else transpose the input and try to find the mirror position
                pattern_matrix = [list(s) for s in current_pattern]
                # print(pattern_matrix)
                transposed_matrix = np.array(pattern_matrix).T
                # print(transposed_matrix)
                transposed_pattern = [''.join(row) for row in transposed_matrix]
                col_mirror = find_mirror(transposed_pattern, 0)
                #print("Col mirror: " + str(col_mirror))
                result += col_mirror
            current_pattern = []
        else:
            current_pattern.append(line)

    print("Day 13 P1 result: " + str(result))

    return


def day13_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day13.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    current_pattern = []
    lines.append("")
    for line in lines:
        if len(line) == 0:
            # print(current_pattern)
            row_mirror = find_mirror(current_pattern, 1)
            #print("Row mirror: " + str(row_mirror))
            if row_mirror >= 0:
                result += row_mirror * 100
            else:
                pattern_matrix = [list(s) for s in current_pattern]
                # print(pattern_matrix)
                transposed_matrix = np.array(pattern_matrix).T
                # print(transposed_matrix)
                transposed_pattern = [''.join(row) for row in transposed_matrix]
                col_mirror = find_mirror(transposed_pattern, 1)
                #print("Col mirror: " + str(col_mirror))
                result += col_mirror
            current_pattern = []
        else:
            current_pattern.append(line)

    print("Day 13 P2 result: " + str(result))
    return


def main():

    day13_pt1()
    day13_pt2()


if __name__ == "__main__":
    main()
