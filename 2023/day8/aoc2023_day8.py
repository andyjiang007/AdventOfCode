# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:58:29 2023

@author: Andy
"""

import re
import itertools
import math


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


def day8_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day8.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    # Regular expression pattern for extracting nodes
    pattern = r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)"

    nodes_map = {}
    sequence = ""
    for line in lines:
        if line == lines[0]:
            sequence = line
        elif '=' in line:
            # Searching the string
            match = re.match(pattern, line)
            node_name, connected_node_left, connected_node_right = match.groups()

            nodes_map[node_name] = (connected_node_left, connected_node_right)
    # print(nodes_map)

    current_node = "AAA"
    sequence_index = 0
    while current_node != "ZZZ":
        # print(current_node)
        if sequence[sequence_index] == 'L':
            current_node = nodes_map[current_node][0]
        elif sequence[sequence_index] == 'R':
            current_node = nodes_map[current_node][1]

        sequence_index += 1
        if sequence_index >= len(sequence):
            sequence_index = 0

        result += 1

    print("Day 8 P1 result: " + str(result))

    return


def all_nodes_at_end(current_nodes):
    for node in current_nodes:
        if node[-1] != 'Z':
            return False
    return True


def day8_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day8.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    # Regular expression pattern for extracting nodes
    pattern = r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)"

    nodes_map = {}
    sequence = ""
    for line in lines:
        if line == lines[0]:
            sequence = line
        elif '=' in line:
            # Searching the string
            match = re.match(pattern, line)
            node_name, connected_node_left, connected_node_right = match.groups()

            nodes_map[node_name] = (connected_node_left, connected_node_right)
    # print(nodes_map)

    start_nodes = [node for node in nodes_map.keys() if node[-1] == 'A']
    num_steps_set = set()

    for start_node in start_nodes:
        num_steps = 0
        current_node = start_node
        # Use a cycle tool to keep iterating on the sequence
        for i in itertools.cycle(sequence):
            if current_node.endswith('Z'):
                # Break out of the loop when the end is reached
                # Record the first time a node has reached its end
                num_steps_set.add(num_steps)
                break

            if i == 'L':
                current_node = nodes_map[current_node][0]
            elif i == 'R':
                current_node = nodes_map[current_node][1]
            num_steps += 1
    # The result is the least common multiple between all number of steps to the end
    result = math.lcm(*num_steps_set)

    print("Day 8 P2 result: " + str(result))
    return


def main():
    day8_pt1()
    day8_pt2()


if __name__ == "__main__":
    main()
