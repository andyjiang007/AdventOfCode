# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:38:14 2023

@author: Andy
"""
import numpy as np

def day6_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day6.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    times = lines[0].split("Time:")[1].split(' ')
    times = [int(item) for item in times if len(item) > 0]
    distances = lines[1].split("Distance:")[1].split(' ')
    distances = [int(item) for item in distances if len(item) > 0]
    
    #print(times)
    #print(distances)
    
    result = 1
    for i in range(len(times)):
        middle_time = int(times[i] / 2)
        for press_time in range(middle_time):
            # the current distance is always the multiplication of the press time and the remaining time
            if press_time * (times[i] - press_time) > distances[i]:
                #print("press time: " + str(press_time))
                valid_count = 0
                if times[i] % 2 == 0:
                    # If time is even, we only count the middle point once
                    valid_count = (middle_time - press_time ) * 2 + 1
                else:
                    # If time is odd, we count every thing in between the middle time twice
                    valid_count = (middle_time - press_time + 1) * 2
                #print(valid_count)
                result *= valid_count
                break
    
    print("Day 6 P1 result: " + str(result))

    return

def day6_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day6.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    times = lines[0].split("Time:")[1].split(' ')
    time = np.int64(''.join([item for item in times if len(item) > 0]))
    distances = lines[1].split("Distance:")[1].split(' ')
    distance = np.int64(''.join([item for item in distances if len(item) > 0]))
    
    #print(time)
    #print(distance)
    
    result = 1
    # Using int64 to avoid overflow
    middle_time = np.int64(time / 2)
    for press_time in range(middle_time):
        if press_time * (time - press_time) > distance:
            #print("press time: " + str(press_time))
            valid_count = 0
            if time % 2 == 0:
                valid_count = (middle_time - press_time ) * 2 + 1
            else:
                valid_count = (middle_time - press_time + 1) * 2
            #print(valid_count)
            result *= valid_count
            break
    
    print("Day 6 P2 result: " + str(result))
    return


def main():
    day6_pt1()
    day6_pt2()

if __name__ == "__main__":
    main()
    