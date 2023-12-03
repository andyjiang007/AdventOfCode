# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:58:58 2023

@author: Andy
"""

dx = [1,-1, 0,1,-1, 0,1,-1]
dy = [0,0, 1,1,1, -1,-1,-1]

### Check whether if this number should be included
def checkInclude(lines, i, j):
    for direction in range(len(dx)):
        new_i = i + dy[direction]
        new_j = j + dx[direction]
        if new_i >= 0 and new_i < len(lines) and new_j >= 0 and new_j < len(lines[i]) \
            and not lines[new_i][new_j].isdigit() and lines[new_i][new_j] != '.':
                #print('Returning True for new_i: ' + str(new_i) +  '\tnew_j: ' + str(new_j))
                return True
    return False

### Find the complete number given a starting digit
def findAdjNums(lines, i, j):
    result = [(i, j)]
    index = j - 1
    while index >= 0 and lines[i][index].isdigit():
        result = [(i,index)] + result
        index -= 1
    
    index = j + 1
    while index < len(lines[i]) and lines[i][index].isdigit():
        result.append((i, index))
        index += 1
    
    return result

### Find the counting gear ratios given a gear position
def findGearRatio(lines, i, j):
    adj_nums = []
    # Need to record all the number positions that we already visited
    visited = set()
    for direction in range(len(dx)):
        new_i = i + dy[direction]
        new_j = j + dx[direction]
        if new_i >= 0 and new_i < len(lines) and new_j >= 0 and new_j < len(lines[i]) \
            and lines[new_i][new_j].isdigit() and (new_i, new_j) not in visited:
                #print('Found number at new_i: ' + str(new_i) +  '\tnew_j: ' + str(new_j))
                num_str = ''
                for (x, y) in findAdjNums(lines, new_i, new_j):
                    visited.add((x, y))
                    num_str += lines[x][y]
                #print(visited)
                adj_nums.append(int(num_str))
    
    if len(adj_nums) == 2:
        #print(adj_nums)
        return adj_nums[0] * adj_nums[1]
    return 0

def day3_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day3.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = 0
    
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]):
            #print("i: " + str(i) + "\tj: " + str(j))
            if lines[i][j].isdigit():
                include = checkInclude(lines, i, j)
                num_string = str(lines[i][j])
                j += 1
                while j < len(lines[i]) and lines[i][j].isdigit():
                    num_string += str(lines[i][j])
                    include |= checkInclude(lines, i, j)
                    j += 1
                
                if include:
                    #print('Adding num: ' + num_string)
                    result += int(num_string)
            j += 1
    
    print("Day 3 P1 result: " + str(result))

    return
    

def day3_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day3.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = 0
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # Find all gear positions
            if lines[i][j] == '*':
                #print("gear at i: " + str(i) + "\tj: " + str(j))
                result += findGearRatio(lines, i, j)
            j += 1
    
    print("Day 3 P2 result: " + str(result))
    
    return

def main():
    
    day3_pt1()
    day3_pt2()

if __name__ == "__main__":
    main()
    