# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 20:59:59 2023

@author: Andy
"""

from enum import Enum
from collections import deque


class Direction(Enum):
    NORTH = [-1, 0]  # Going north decreases the index for row
    SOUTH = [1, 0]
    EAST = [0, 1]
    WEST = [0, -1]

    @classmethod
    def opposite(cls, value):
        if value == Direction.NORTH:
            return Direction.SOUTH
        if value == Direction.SOUTH:
            return Direction.NORTH
        if value == Direction.EAST:
            return Direction.WEST
        if value == Direction.WEST:
            return Direction.EAST


pipe_direction_map = {
    '|': [Direction.NORTH, Direction.SOUTH],
    '-': [Direction.EAST, Direction.WEST],
    'L': [Direction.NORTH, Direction.EAST],
    'J': [Direction.NORTH, Direction.WEST],
    '7': [Direction.WEST, Direction.SOUTH],
    'F': [Direction.EAST, Direction.SOUTH],
    '.': [],
    # Initialize the starting point to be connected to all directions
    'S': [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST],
}


def isValid(pos, pipe_matrix):
    [pos_row, pos_col] = pos
    return 0 <= pos_col < len(pipe_matrix[0]) and 0 <= pos_row < len(pipe_matrix)


def day10_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day10.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    start_pos = []
    pipe_matrix = []

    for line in lines:
        pipe_row = [pipe_direction_map[char] for char in line]
        if 'S' in line:
            s_col = line.index('S')
            s_row = lines.index(line)
            start_pos = [s_row, s_col]
        pipe_matrix.append(pipe_row)

    # print(pipe_matrix)
    # print(start_pos)

    # Storing the steps needed to reach each point
    steps = [[int(1e6) for _ in range(len(pipe_matrix[0]))]
             for _ in range(len(pipe_matrix))]
    steps[start_pos[0]][start_pos[1]] = 0
    # Using a double-ended queue for BFS
    flood_queue = deque([start_pos])
    # print(flood_queue)
    while flood_queue:
        current_pos = flood_queue.popleft()
        current_row = current_pos[0]
        current_col = current_pos[1]
        # Only search for the connected directions from the current point
        connected_directions = pipe_matrix[current_row][current_col]
        for direction in connected_directions:
            # print("Going " + str(direction))
            [after_row, after_col] = [x + y for x,
                                      y in zip(current_pos, direction.value)]
            # print(steps)
            # Proceed only if the new position is within the matrix and has not been visited before
            if isValid([after_row, after_col], pipe_matrix) and steps[after_row][after_col] == int(1e6):
                possible_directions = pipe_matrix[after_row][after_col]
                from_direction = Direction.opposite(direction)
                # Check if the next position has the incoming direction connected
                if from_direction in possible_directions:
                    # Keep the lower steps-to-reach if there is alreay an existing one
                    steps[after_row][after_col] = min(
                        steps[after_row][after_col], steps[current_row][current_col] + 1)
                    flood_queue.append([after_row, after_col])

    flattened_steps = [
        item for sublist in steps for item in sublist if item != int(1e6)]
    # Final result should be the maximum steps possible for visited points
    result = max(flattened_steps)

    print("Day 10 P1 result: " + str(result))

    return


def day10_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day10.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    start_pos = []
    pipe_matrix = []

    for line in lines:
        pipe_row = [pipe_direction_map[char] for char in line]
        if 'S' in line:
            s_col = line.index('S')
            s_row = lines.index(line)
            start_pos = [s_row, s_col]
        pipe_matrix.append(pipe_row)

    # print(pipe_matrix)
    # print(start_pos)

    # Using a double-ended queue for BFS
    flood_queue = deque([start_pos])
    # Store all the visited points that is part of the loop
    the_loop = [start_pos]

    while flood_queue:
        current_pos = flood_queue.popleft()
        connected_directions = pipe_matrix[current_pos[0]][current_pos[1]]

        for direction in connected_directions:
            [after_row, after_col] = [x + y for x,
                                      y in zip(current_pos, direction.value)]
            # print("Going " + str(direction))
            # print([after_row, after_col])
            if isValid([after_row, after_col], pipe_matrix) and [after_row, after_col] not in the_loop:
                possible_directions = pipe_matrix[after_row][after_col]
                from_direction = Direction.opposite(direction)
                if from_direction in possible_directions:
                    # print("Adding " + str([after_row, after_col]))
                    the_loop.append([after_row, after_col])
                    flood_queue.append([after_row, after_col])

    # print(the_loop)
    north_of_start_pos = [x + y for x,
                          y in zip(start_pos, Direction.NORTH.value)]
    # If the point north to the starting point has South direction connected,
    # we need to update the connected directions of the starting point
    if isValid(north_of_start_pos, pipe_matrix) and Direction.SOUTH in pipe_matrix[north_of_start_pos[0]][north_of_start_pos[1]]:
        pipe_matrix[start_pos[0]][start_pos[1]] = [Direction.NORTH]
    else:
        pipe_matrix[start_pos[0]][start_pos[1]] = []

    # For each point in the matrix, from left to right,
    # store the total number of north connecting points that is part of the loop
    num_north_pipes = [
        [0 for _ in range(len(pipe_matrix[0]))] for _ in range(len(pipe_matrix))]
    for row in range(len(pipe_matrix)):
        count = 0
        for col in range(len(pipe_matrix[0])):
            if [row, col] not in the_loop:
                # print("updating " + str(row) + ", " + str(col))
                num_north_pipes[row][col] = count
            elif Direction.NORTH in pipe_matrix[row][col]:
                count += 1

    # print(num_north_pipes)
    # The final result is the total number of points that has odd number of north connected pipes
    result = sum(item %
                 2 != 0 for sublist in num_north_pipes for item in sublist)

    print("Day 10 P2 result: " + str(result))
    return


def main():

    day10_pt1()
    day10_pt2()


if __name__ == "__main__":
    main()
