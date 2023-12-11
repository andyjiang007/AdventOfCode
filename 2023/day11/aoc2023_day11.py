# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:59:42 2023

@author: Andy
"""
import numpy as np


# Calculate the distance based on position index
def distance(start_pos, end_pos):
    return abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])


# Calculate the distance based on position index
# and check if there are any expansions in between
def distance_expand(start_pos, end_pos, expand_rows, expand_cols):
    #print("Start pos: " + str(start_pos) + "\tEnd pos: " + str(end_pos))
    result = abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
    for row in expand_rows:
        if start_pos[0] < row < end_pos[0] or end_pos[0] < row < start_pos[0]:
            result += int(1e6) - 1
            #print("Expanding row: " + str(row))
    for col in expand_cols:
        if start_pos[1] < col < end_pos[1] or end_pos[1] < col < start_pos[1]:
            result += int(1e6) - 1
            #print("Expanding col: " + str(col))
    return result


def day11_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day11.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [list(s.strip('\n')) for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    galaxy_pos = []
    new_lines = []

    # Expand the rows when needed
    for line in lines:
        if '#' not in line:
            new_lines.append(line)
        new_lines.append(line)

    # print(new_lines)
    expanded_matrix = []
    # Transpose the 2D array
    transposed_array = np.array(new_lines).T
    # print(transposed_array)
    # Expand the columns when needed
    for col in transposed_array:
        if '#' not in col:
            expanded_matrix.append(col)
        expanded_matrix.append(col)

    # Transpose it back to the original orientation
    expanded_matrix = np.array(expanded_matrix).T
    # print(expanded_matrix)

    # Get the positions of all the galaxies
    for i in range(len(expanded_matrix)):
        line = expanded_matrix[i]
        if '#' in line:
            g_cols = [index for index, char in enumerate(line) if char == '#']
            for g_col in g_cols:
                galaxy_pos.append([i, g_col])

    # print(galaxy_pos)

    for start in range(len(galaxy_pos)):
        for end in range(start + 1, len(galaxy_pos)):
            result += distance(galaxy_pos[start], galaxy_pos[end])

    print("Day 11 P1 result: " + str(result))

    return


def day11_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day11.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [list(s.strip('\n')) for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    galaxy_pos = []
    expansion_rows = []
    expansion_cols = []
    # Record all the rows that should be expanded
    for i in range(len(lines)):
        if '#' not in lines[i]:
            expansion_rows.append(i)

    lines_t = np.array(lines, dtype=str).T
    # Record all the cols that should be expanded
    for i in range(len(lines_t)):
        if '#' not in lines_t[i]:
            expansion_cols.append(i)
    # print(expansion_rows)
    # print(expansion_cols)

    # Get the positions of all the galaxies
    for i in range(len(lines)):
        line = lines[i]
        if '#' in line:
            g_cols = [index for index, char in enumerate(line) if char == '#']
            for g_col in g_cols:
                galaxy_pos.append([i, g_col])

    # print(galaxy_pos)

    for start in range(len(galaxy_pos)):
        for end in range(start + 1, len(galaxy_pos)):
            result += distance_expand(galaxy_pos[start],
                                      galaxy_pos[end], expansion_rows, expansion_cols)

    print("Day 11 P2 result: " + str(result))
    return


def main():

    day11_pt1()
    day11_pt2()


if __name__ == "__main__":
    main()
