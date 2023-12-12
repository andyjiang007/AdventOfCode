# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:53:06 2023

@author: Andy
"""
from itertools import combinations
from functools import cache


def isValid(spring_list, expected_spring_group):
    combined_string = ''.join(spring_list).replace("?", ".")
    new_spring_groups = combined_string.split(".")
    # print(new_spring_groups)
    new_spring_groups_lengths = [len(item)
                                 for item in new_spring_groups if len(item) > 0]

    return new_spring_groups_lengths == expected_spring_group


# Brute-force solution that lists out all possible combinations and checks if theyr are valid
def possible_arrangements(spring_list, spring_group):
    result = 0
    num_known = len([item for item in spring_list if item == "#"])
    total_springs = sum(spring_group)
    num_left = total_springs - num_known
    unknown_index = [index for index,
                     item in enumerate(spring_list) if item == "?"]
    # print(unknown_index)

    combinations_list = list(combinations(unknown_index, num_left))
    # print(combinations_list)
    for combination in combinations_list:
        new_spring_list = spring_list.copy()
        for i in combination:
            new_spring_list[i] = '#'
        if isValid(new_spring_list, spring_group):
            result += 1

    return result


@cache
# Using Cache is required to finish running the solution within seconds
# Modified frpm https://github.com/ypisetsky/advent-of-code-2023/blob/main/day12.py
def possible_arrangements2(line, counts, pos, consecutive_count, sequence_count):
    # Check if we've reached the end of the line
    if pos == len(line):
        # If all sequences of '#' characters are finished, return 1 (valid pattern)
        ret = 1 if len(counts) == sequence_count else 0
    # If the current character is '#', continue counting
    elif line[pos] == '#':
        ret = possible_arrangements2(
            line, counts, pos + 1, consecutive_count + 1, sequence_count)
    # If the current character is '.' or all counts are finished, calculate the count
    elif line[pos] == '.' or sequence_count == len(counts):
        if sequence_count < len(counts) and consecutive_count == counts[sequence_count]:
            # If the count matches, start counting the next sequence
            ret = possible_arrangements2(
                line, counts, pos + 1, 0, sequence_count + 1)
        elif consecutive_count == 0:
            # If no consecutive '#' characters, continue counting
            ret = possible_arrangements2(
                line, counts, pos + 1, 0, sequence_count)
        else:
            # Invalid pattern
            ret = 0
    else:
        # Calculate counts when treating the current character as '#' or '.'
        hash_count = possible_arrangements2(
            line, counts, pos + 1, consecutive_count + 1, sequence_count)
        dot_count = 0
        if consecutive_count == counts[sequence_count]:
            dot_count = possible_arrangements2(
                line, counts, pos + 1, 0, sequence_count + 1)
        elif consecutive_count == 0:
            dot_count = possible_arrangements2(
                line, counts, pos + 1, 0, sequence_count)
        # Sum counts for valid patterns
        ret = hash_count + dot_count
    return ret


def day12_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day12.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    for line in lines:
        spring_list = list(line.split(' ')[0])
        spring_group = [int(num) for num in line.split(' ')[1].split(',')]

        # print(spring_list)
        # print(spring_group)
        result += possible_arrangements(spring_list, spring_group)

    print("Day 12 P1 result: " + str(result))

    return


def day12_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day12.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    for line in lines:
        spring_list = line.split(' ')[0]
        unfolded_spring_list = '?'.join([spring_list] * 5) + '.'

        spring_group = [int(num) for num in line.split(' ')[1].split(',')]
        unfolded_spring_group = spring_group.copy()
        for i in range(4):
            unfolded_spring_group.extend(spring_group)
        # print(unfolded_spring_list)
        # print(unfolded_spring_group)
        result += possible_arrangements2(unfolded_spring_list,
                                         tuple(unfolded_spring_group), 0, 0, 0)
        # print(result)

    print("Day 12 P2 result: " + str(result))
    return


def main():

    day12_pt1()
    day12_pt2()


if __name__ == "__main__":
    main()
