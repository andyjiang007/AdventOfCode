# -*- coding: utf-8 -*-
"""
Created on 12/1/2024

@author: Andy
"""

import heapq


def day1_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day1.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    leftQueue = []
    rightQueue = []

    for line in lines:
        # print(line)
        first, second = line.split("   ")
        leftNum = int(first)
        rightNum = int(second)
        # print(f"{leftNum=}\t{rightNum=}")
        heapq.heappush(leftQueue, (leftNum, leftNum))
        heapq.heappush(rightQueue, (rightNum, rightNum))

    while leftQueue and rightQueue:
        _, leftNum = heapq.heappop(leftQueue)
        _, rightNum = heapq.heappop(rightQueue)
        result += abs(leftNum - rightNum)
    # print(leftQueue)
    # print(rightQueue)
    print("Day 1 P1 result: " + str(result))

    return


def day1_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day1.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0

    leftList = []
    rightList = []
    leftFreq = {}
    rightFreq = {}
    for line in lines:
        # print(line)
        first, second = line.split("   ")
        leftNum = int(first)
        rightNum = int(second)
        leftList.append(leftNum)
        rightList.append(rightNum)
        if leftNum in leftFreq:
            leftFreq[leftNum] += 1
        else:
            leftFreq[leftNum] = 1
        if rightNum in rightFreq:
            rightFreq[rightNum] += 1
        else:
            rightFreq[rightNum] = 1

    print(leftFreq)
    print(rightFreq)

    for key in leftList:
        if key in rightFreq.keys():
            result += rightFreq[key] * key

    print("Day 1 P2 result: " + str(result))

    return


def main():
    day1_pt1()
    day1_pt2()


if __name__ == "__main__":
    main()
