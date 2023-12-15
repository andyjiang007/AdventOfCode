# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:24:30 2023

@author: Andy
"""


# Lens class that holds its label and focal length info
class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

    def __str__(self):
        return f"Label: {self.label}, Focal Length: {self.focal_length}"


def calculate_hash(string):
    val = 0
    for char in list(string):
        # Conver the character to its ASCII value
        val += ord(char)
        val *= 17
        val %= 256

    return val


def day15_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day15.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    for line in lines:
        seq_list = line.split(',')
        for seq in seq_list:
            result += calculate_hash(seq)

    print("Day 15 P1 result: " + str(result))

    return


def day15_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day15.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()

    result = 0
    box_list = [[] for _ in range(256)]

    for line in lines:
        seq_list = line.split(',')
        for seq in seq_list:
            if '=' in seq:
                # If this is an assignment operation, get the label by spliting from '='
                label = seq.split('=')[0]
                box_num = calculate_hash(label)
                focal_length = int(seq.split('=')[1])
                #print("Adding label " + label + " in box " + str(box_num))

                found = False
                for lens in box_list[box_num]:
                    # Go through the lens in the box, replace the existing one with the same label
                    if lens.label == label:
                        lens.focal_length = focal_length
                        found = True
                        break
                if not found:
                    # Add a new Lens if not found in the box
                    box_list[box_num].append(Lens(label, focal_length))

            elif '-' in seq:
                # If this is a removal operation, all chars until the last one is the label
                label = seq[:-1]
                box_num = calculate_hash(label)
                #print("Removing label " + label + " in box " + str(box_num))
                for index, lens in enumerate(box_list[box_num]):
                    # Go through the lens in the box and remove the existing one with the same label
                    if lens.label == label:
                        box_list[box_num].pop(index)
                        break

    for box_index, box in enumerate(box_list):
        for lens_index, lens in enumerate(box):
            result += (box_index + 1) * (lens_index + 1) * lens.focal_length

    print("Day 15 P2 result: " + str(result))
    return


def main():

    day15_pt1()
    day15_pt2()


if __name__ == "__main__":
    main()
