# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:50:34 2022

@author: Andy
"""

import time
from copy import deepcopy
import functools
import sys, re
import matplotlib.pyplot as plt

def day1():
    # Using readlines()
    inputFile = open('AOCday1.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    itemMap = {}
    index = 0
    currentItems = []
    totalCal = []
    
    for line in lines:
        if line == '\n':
            itemMap[index] = currentItems
            index = index+1
            totalCal.append(sum(currentItems))
            currentItems = []
        else:
            currentItems.append(int(line))

    
    totalCal.sort(reverse=True)
    
    print("Day 1 P1 result: " + str(totalCal[0]))
    
    top3 = totalCal[0] + totalCal[1] + totalCal[2]
    print("Day 1 P2 result: " + str(top3))
    return
    

def day2():
    # Opponent: A -> Rock, B-> Paper, C-> Scissor
    # Response: A -> Y/Paper, B-> X/Rock, C -> Z/Scissor
    # Score: Rock -> 1, Paper-> 2, Scissor-> 3
    # X: A-> 3, B-> 0, C-> 6
    # Y: A-> 6, B-> 3, C-> 0
    # Z: A-> 0, B-> 6, C-> 3
    
    inputFile = open('AOCday2.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    score = 0
    
    for line in lines:
        oppo = line.strip('\n').split(' ', 1)[0]
        you = line.strip('\n').split(' ', 1)[1]

        if you == 'X':
            score += 1
            if oppo == 'A':
                score += 3
            elif oppo == 'B':
                score += 0
            elif oppo == 'C':
                score += 6
        elif you == 'Y':
            score += 2
            if oppo == 'A':
                score += 6
            elif oppo == 'B':
                score += 3
            elif oppo == 'C':
                score += 0
        if you == 'Z':
            score += 3
            if oppo == 'A':
                score += 0
            elif oppo == 'B':
                score += 6
            elif oppo == 'C':
                score += 3

    print("Day 2 P1 result: " + str(score))
    
    
    score = 0
    for line in lines:
        oppo = line.strip('\n').split(' ', 1)[0]
        you = line.strip('\n').split(' ', 1)[1]

        # X-> 0: A-> 3, B-> 1, C-> 2
        # Y-> 3: A-> 1, B-> 2, C-> 3
        # Z-> 6: A-> 2, B-> 3, C-> 1
        if you == 'X':
            score += 0
            if oppo == 'A':
                score += 3
            elif oppo == 'B':
                score += 1
            elif oppo == 'C':
                score += 2
        elif you == 'Y':
            score += 3
            if oppo == 'A':
                score += 1
            elif oppo == 'B':
                score += 2
            elif oppo == 'C':
                score += 3
        if you == 'Z':
            score += 6
            if oppo == 'A':
                score += 2
            elif oppo == 'B':
                score += 3
            elif oppo == 'C':
                score += 1
                
    print("Day 2 P2 result: " + str(score))
    return


def day3():
    inputFile = open('AOCday3.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    print(ord('a') - ord('a') + 1)
    print(ord('A') - ord('A') + 27)
    score = 0
    
    for line in lines:
        middle = int(len(line)/2)
        comp1 = line[:middle]
        comp2 = line[middle:]
        
        charList = list(comp1)
        for char in charList:
            if comp2.find(char, 0) != -1:
                if ord(char) >= ord('a'):
                    score += ord(char) - ord('a') + 1
                else:
                    score += ord(char) - ord('A') + 27
                break
    
    print("Day 3 P1 result: " + str(score))
    
    score = 0
    i = 0
    currIntersection = set()
    for line in lines:
        line = line.strip('\n')
        
        if i == 0:
            currIntersection = set(list(line))
            i += 1
        elif i == 1:
            currIntersection = set(currIntersection) & set(list(line))
            i += 1
        else:
            currIntersection = set(currIntersection) & set(list(line))
            print(currIntersection)
            assert(len(currIntersection) == 1)
            badge = list(currIntersection)[0]
            if ord(badge) >= ord('a'):
                score += ord(badge) - ord('a') + 1
            else:
                score += ord(badge) - ord('A') + 27
            currIntersection = set()
            i = 0
    
    print("Day 3 P2 result: " + str(score))
    return

def day4():
    inputFile = open('AOCday4.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    result = 0
    overlap = 0
    
    for line in lines:
        line = line.strip('\n')
        e1 = line.split(',')[0]
        e2 = line.split(',')[1]
        
        e1Start = int(e1.split('-')[0])
        e1End = int(e1.split('-')[1])
        e2Start = int(e2.split('-')[0])
        e2End = int(e2.split('-')[1])
        
        assert(e1Start <= e1End)
        assert(e2Start <= e2End)
        
        if e1Start >= e2Start and e1Start <= e2End and e1End >= e2Start and e1End <= e2End:
            result += 1
            overlap += 1
        elif e2Start >= e1Start and e2Start <= e1End and e2End >= e1Start and e2End <= e1End:
            result += 1
            overlap += 1
        elif e1End >= e2Start and e1End <= e2End:
            overlap += 1
        elif e2End >= e1Start and e2End <= e1End:
            overlap += 1
        
    print("Day 4 P1 result: " + str(result))
    print("Day 4 P2 result: " + str(overlap))
    return


def day5():
    inputFile = open('AOCday5.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    stack1 = ['R', 'S', 'L', 'F', 'Q']
    stack2 = ['N', 'Z', 'Q', 'G', 'P', 'T']
    stack3 = ['S', 'M', 'Q', 'B']
    stack4 = ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q']
    stack5 = ['P', 'H', 'M', 'B', 'N', 'F', 'S']
    stack6 = ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G']
    stack7 = ['W', 'C', 'F']
    stack8 = ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M']
    stack9 = ['G', 'Z', 'D', 'L', 'C', 'N', 'R']
    
    stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9] 
    
    for line in lines:
        line = line.strip('\n')
        print(line)
        if line.find('move') == -1:
            continue
        
        numItem = int(line.split(' from ')[0].split(' ')[1])
        startStack = int(line.split(' from ')[1].split(' to ')[0])
        endStack = int(line.split(' from ')[1].split(' to ')[1])
        
        print("startStack: "+ str(stacks[startStack-1]))
        print("endStack: "+ str(stacks[endStack-1]))
        
        #for i in range(numItem):
        #    if len(stacks[startStack-1]) == 0:
        #        break
        #    currItem = stacks[startStack-1].pop()
        #    stacks[endStack-1].append(currItem)
            
        movingItems = stacks[startStack-1][-numItem:]
        for item in movingItems:
            stacks[endStack-1].append(item)
        stacks[startStack-1] = stacks[startStack-1][:-numItem]
        
        print("startStack: "+ str(stacks[startStack-1]))
        print("endStack: "+ str(stacks[endStack-1]))
    for stack in stacks:
        print(stack[-1])
    
    return


def day6():
    inputFile = open('AOCday6.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    assert(len(lines) == 1)
    chars = list(lines[0])
    windowSize = 14
    for i in range(windowSize, len(chars)):
        window = chars[i-windowSize:i]
        print(window)
        if (len(set(window)) == windowSize):
            print("Day 6 P1 result: " + str(i))
            break
    
    return

def day7():
    
    class Node:
        def __init__(self, name):
            self.name = name
            self.size = 0
            self.isDir = True
            self.children = []
            self.parent = None
            
    def findNode(root, name):
        for child in root.children:
            if child.name == name:
                return child
        return None
    
    def findSize(root):
        if root.size > 0:
            return root.size
        else:
            totalSize = 0
            for child in root.children:
                totalSize += findSize(child)
            root.size = totalSize
            return totalSize
        
    inputFile = open('AOCday7.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    root = Node('/')
    current = root
    for line in lines:
        line = line.strip('\n')
        if line.split(' ')[0] == '$':
            if line.split(' ')[1] == 'cd':
                name = line.split(' ')[2]
                # print(name)
                if (name == '/'): continue
                elif (name == '..'):
                    current = current.parent
                else:
                    current = findNode(current, name)
            elif line.split(' ')[1] == 'ls':
                continue
        else: # output of ls
            size = line.split(' ')[0]
            name = line.split(' ')[1]
            newNode = Node(name)
            if size.isnumeric():                
                newNode.size = int(size)
                newNode.isDir = False
                
            newNode.parent = current
            current.children.append(newNode)
    
    print("Total Dir size:" + str(findSize(root)))
    needed = findSize(root) - 40000000
    print("Total needed size:" + str(needed))
    stack = [root]
    result = 0
    result2 = float('inf')
    while len(stack) > 0:
        current = stack.pop()
        if current.isDir and current.size <= 100000:
            result += current.size
        if current.isDir and current.size >= needed:
            result2 = min(result2, current.size)
        for child in current.children:
            stack.append(child)
    
    print("Day 7 P1 result: " + str(result))
    print("Day 7 P2 result: " + str(result2))
    
    return

def day8():
    
    inputFile = open('AOCday8.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    def isVisible(trees, i, j):
        sameRow = trees[i]
        sameCol = [row[j] for row in trees]
        #print("i: " + str(i) + " j: " + str(j))

        if max(sameRow[:j]) + 1 <= trees[i][j]:
            print("left visible")
            return True
        if max(sameRow[j+1:]) + 1 <= trees[i][j]:
            print("right visible")
            return True
        if max(sameCol[:i]) + 1 <= trees[i][j]:
            print("up visible")
            return True
        if max(sameCol[i+1:]) + 1 <= trees[i][j]:
            print("down visible")
            return True
        return False
    
    def findScenicScore(trees, i, j):
        distUp = 1
        distDown = 1
        distLeft = 1
        distRight = 1
        if i == 2:
            print("i: " + str(i) + " j: " + str(j))
        sameRow = trees[i]
        sameCol = [row[j] for row in trees]
        
        index = i-1
        while index > 0 and sameCol[index] < trees[i][j]:
            distUp +=1
            index -= 1
        if i == 2:
            print(distUp)
        
        index = i+1
        while index < len(sameCol)-1 and sameCol[index] < trees[i][j]:
            distDown +=1
            index += 1
        
        index = j-1
        while index > 0 and sameRow[index] < trees[i][j]:
            distLeft +=1
            index -= 1
        
        index = j+1
        while index < len(sameRow)-1 and sameRow[index] < trees[i][j]:
            distRight +=1
            index += 1
        
        return distUp * distDown * distLeft * distRight
        
    trees = []
    for line in lines:
        line = line.strip('\n')
        line = list(line)
        line = [eval(i) for i in line]
        trees.append(line)
    row = len(trees)
    col = len(trees[0])
    
    vis = [[[False] for _ in range(row)] for _ in range(col)]
    for i in range(col):
        vis[0][i] = True
        vis[-1][i] = True
    for i in range(row):
        vis[i][0] = True
        vis[i][-1] = True
    
    maxScore = 0
    for i in range(1, row-1):
        for j in range(1, col-1):
            vis[i][j] = isVisible(trees, i, j)
            maxScore = max(maxScore, findScenicScore(trees, i, j))
    flat = sum(vis, [])
    print("Day 8 P1 result: " + str(flat.count(True)))
    print("Day 8 P2 result: " + str(maxScore))
    
    return

def day9():
    
    inputFile = open('AOCday9.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    def moveTail(head, tail, visited):
        #print("head: " + str(head))
        #print("tail: " + str(tail))
        if head == tail:
            return tail, visited
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            if head[0] > tail[0]:
                tail = (tail[0] + 1, tail[1])
            elif head[0] < tail[0]:
                tail = (tail[0] - 1, tail[1])
            if head[1] > tail[1]:
                tail = (tail[0], tail[1] + 1)
            elif head[1] < tail[1]:
                tail = (tail[0], tail[1] - 1)
        elif head[0] == tail[0]:
            if abs(head[1] - tail[1]) == 1:
                return tail, visited
            else:
                if head[1] > tail[1]:
                    tail = (tail[0], tail[1] + 1)
                else:
                    tail = (tail[0], tail[1] - 1)
        elif head[1] == tail[1]:
            if abs(head[0] - tail[0]) == 1:
                return tail, visited
            else:
                if head[0] > tail[0]:
                    tail = (tail[0] + 1, tail[1])
                else:
                    tail = (tail[0] - 1, tail[1])

        #print("new tail: " + str(tail))
        visited.add(tail)
        return tail, visited
    
    def moveRope(head, rope, visitedRope):
        curHead = head
        for i in range(9):
            knot, _ = moveTail(curHead, rope[i], set())
            curHead = deepcopy(rope[i])
            rope[i] = deepcopy(knot)
        print(rope)
        visitedRope.add(rope[-1])
        return rope, visitedRope
    
    head = (0, 0)
    tail = (0, 0)
    rope = [(0, 0) for _ in range(9)]
    visited = set()
    visitedRope = set()
    for line in lines:
        line = line.strip('\n')
        direction = line.split(' ')[0]
        distance = int(line.split(' ')[1])
        if direction == 'L':
            while distance > 0:
                head = (head[0] - 1, head[1])
                distance -= 1
                tail, visited = moveTail(head, tail, visited)
                rope, visitedRope = moveRope(head, rope, visitedRope)
        elif direction == 'R':
            while distance > 0:
                head = (head[0] + 1, head[1])
                distance -= 1
                tail, visited = moveTail(head, tail, visited)
                rope, visitedRope = moveRope(head, rope, visitedRope)
        elif direction == 'D':
            while distance > 0:
                head = (head[0], head[1] - 1)
                distance -= 1
                tail, visited = moveTail(head, tail, visited)
                rope, visitedRope = moveRope(head, rope, visitedRope)
        elif direction == 'U':
            while distance > 0:
                head = (head[0], head[1] + 1)
                distance -= 1
                tail, visited = moveTail(head, tail, visited)
                rope, visitedRope = moveRope(head, rope, visitedRope)
        print("new head: " + str(head))
        
    #print(visited)
    print("Day 9 P1 result: " + str(len(visited)))
    print("Day 9 P2 result: " + str(len(visitedRope)))
    
    return

def day10():
    
    inputFile = open('AOCday10.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    register = 1
    cycle = 1
    result = 0
    graph = [['.' for _ in range(40)] for _ in range (6)]
    for line in lines:
        line = line.strip('\n')
        if line == 'noop':
            if cycle % 40 == 20:
                result += cycle * register
            row = int(cycle / 40)
            col = cycle % 40
            if register + 1 == col or register == col or register + 2 == col:
                graph[row][col] = '#'
            
            cycle += 1
        else:
            for i in range(2):
                if cycle % 40 == 20:
                    result += cycle * register
                row = int(cycle / 40)
                col = cycle % 40
                if register + 1 == col or register == col or register + 2 == col:
                    graph[row][col] = '#'
                cycle += 1
            add = int(line.split(' ')[1])
            register += add
    
    print("Day 10 P1 result: " + str(result))
    print("Day 10 P2 result: ")
    for i in range (6):
        print(graph[i])
    return
    

def day11():
    
    class Monkey:
        item = []
        operation = ""
        operationNum = 0
        divisor = 0
        testTrue = 0
        testFalse = 0
        
        def __init__(self, item, operation, operationNum, divisor, testTrue, testFalse):
            self.item = item
            self.operation = operation
            self.operationNum = operationNum
            self.divisor = divisor
            self.testTrue = testTrue
            self.testFalse = testFalse
        
        def hasItem(self):
            return len(self.item) > 0
        
    monkey0 = Monkey([53, 89, 62, 57, 74, 51, 83, 97],
                     "*", 3, 13, 1, 5)
    monkey1 = Monkey([85, 94, 97, 92, 56],
                     "+", 2, 19, 5, 2)
    monkey2 = Monkey([86, 82, 82],
                     "+", 1, 11, 3, 4)
    monkey3 = Monkey([94, 68],
                     "+", 5, 17, 7, 6)
    monkey4 = Monkey([83, 62, 74, 58, 96, 68, 85],
                     "+", 4, 3, 3, 6)
    monkey5 = Monkey([50, 68, 95, 82],
                     "+", 8, 7, 2, 4)
    monkey6 = Monkey([75],
                     "*", 7, 5, 7, 0)
    monkey7 = Monkey([92, 52, 85, 89, 68, 82],
                     "^", 2, 2, 0, 1)
    monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
    numInspect = [0 for _ in range(8)]
    
    mod_all = 1
    for div_by in [m.divisor for m in monkeys]:
        mod_all *= div_by
    
    round = 1
    while round <= 10000:
        for i in range(8):
            thisMonkey = monkeys[i]
            #print("Monkey " + str(i) + ": " + str(thisMonkey.item))
            while len(thisMonkey.item) > 0:
                current = thisMonkey.item.pop(0)
                if thisMonkey.operation == "*":
                    current = current * thisMonkey.operationNum
                elif thisMonkey.operation == "+":
                    current = current + thisMonkey.operationNum
                else:
                    current = current * current
                #current = int(current / 3)
                current = current % mod_all
                
                if current % thisMonkey.divisor == 0:
                    #print("adding " + str(current) + " to Monkey " + str(thisMonkey.testTrue))
                    monkeys[thisMonkey.testTrue].item.append(current)
                else:
                    #print("adding " + str(current) + " to Monkey " + str(thisMonkey.testFalse))
                    monkeys[thisMonkey.testFalse].item.append(current)
                
                numInspect[i] += 1
            
        round += 1
        print(numInspect)
    
    print("Day 11 P1 result: " + str(numInspect))
    
    return

def day12():
    
    inputFile = open('AOCday12.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    heightMap = []
    startPos = [0, 0]
    endPos = [0, 0]
    
    def isValid(heightMap, currentPos, newPos):
        if newPos[0] >= 0 and newPos[0] < len(heightMap) and newPos[1] >= 0 and newPos[1] < len(heightMap[0]):
            if ord(heightMap[currentPos[0]][currentPos[1]]) +1 >= ord(heightMap[newPos[0]][newPos[1]]):
                return True
        return False
    
    def isBackValid(heightMap, currentPos, newPos):
        if newPos[0] >= 0 and newPos[0] < len(heightMap) and newPos[1] >= 0 and newPos[1] < len(heightMap[0]):
            if ord(heightMap[newPos[0]][newPos[1]]) +1 >= ord(heightMap[currentPos[0]][currentPos[1]]):
                return True
        return False
    
    for line in lines:
        line = line.strip('\n')
        line = [i for i in line]
        heightMap.append(line)
    
    #print(heightMap)
    
    for i in range(len(heightMap)):
        for j in range(len(heightMap[i])):
            if heightMap[i][j] == 'S':
                startPos = [i, j]
                heightMap[i][j] = 'a'
            elif heightMap[i][j] == 'E':
                endPos = [i, j]
                heightMap[i][j] = 'z'
                
    print(startPos)
    print(endPos)
    
    stack = []
    visited = []
    result = 0
    stack.append(startPos)
    
    while len(stack) > 0:
        size = len(stack)
        for i in range(size):
            current = stack.pop(0)
            if current == endPos:
                print("Day 12 P1 result: " + str(result))
                break
            # Move up
            newPos = [current[0], current[1] - 1]
            if isValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
            # Move down
            newPos = [current[0], current[1] + 1]
            if isValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
            # Move left
            newPos = [current[0] - 1, current[1]]
            if isValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
            # Move right
            newPos = [current[0] + 1, current[1]]
            if isValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
                
        result += 1
        
    stack.clear()
    stack.append(endPos)
    visited.clear()
    result = 0
    while len(stack) > 0:
        size = len(stack)
        for i in range(size):
            current = stack.pop(0)
            if heightMap[current[0]][current[1]] == 'a':
                stack.clear()
                print("Day 12 P2 result: " + str(result))
                break
            # Move up
            newPos = [current[0], current[1] - 1]
            if isBackValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
            # Move down
            newPos = [current[0], current[1] + 1]
            if isBackValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
            # Move left
            newPos = [current[0] - 1, current[1]]
            if isBackValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
            # Move right
            newPos = [current[0] + 1, current[1]]
            if isBackValid(heightMap, current, newPos) and newPos not in visited:
                visited.append(newPos)
                stack.append(newPos)
                
        result += 1
        
    return


def day13():
    
    inputFile = open('AOCday13.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    def compare(left, right):
        if type(left) is int:
            if type(right) is int:
                if left < right:
                    return 1
                elif left == right:
                    return 0
                else:
                    return -1
            if type(right) is list:
                return compare([left], right)
        if type(left) is list:
            if type(right) is int:
                return compare(left, [right])
            if type(right) is list:
                if len(left) == 0:
                    if len(right) > 0:
                        return 1
                    else:
                        return 0
                else:
                    if len(right) > 0:
                        compareResult = compare(left[0], right[0])
                        if compareResult == 0:
                            return compare(left[1:], right[1:])
                        else:
                            return compareResult
                    else:
                        return -1
    
    left = []
    right = []
    packets = []
    index = 0
    result = 0
    for line in lines:
        line = line.strip('\n')
        index += 1
        if index % 3 == 0:
            compareResult = compare(left, right)
            print("Compare result for index: " + str(index) + " is\t" + str(compareResult))
            if compareResult == 1:
                #print(str(left))
                #print(str(right))
                result += int(index/3)
            left.clear()
            right.clear()
            continue
        
        if index % 3 == 1:
            left = eval(line)
            packets.append(deepcopy(left))
        elif index % 3 == 2:
            right = eval(line)
            packets.append(deepcopy(right))
        
    print("Day 13 P1 result: " + str(result))
    
    packets.append([[2]])
    packets.append([[6]])
    
    sortedPackets = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)
    #print(sortedPackets)
    
    index1 = sortedPackets.index([[2]]) + 1
    index2 = sortedPackets.index([[6]]) + 1
    #print(index1)
    #print(index2)
    print("Day 13 P2 result: " + str(index1 * index2))
    
def day14():
    
    inputFile = open('AOCday14.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    def moveSand(currentSand, rocks, sands):
        x = currentSand[0]
        y = currentSand[1]
        down = [x, y+1]
        downLeft = [x-1, y+1]
        downRight = [x+1, y+1]
        if down not in rocks and down not in sands:
            #print("moving down")
            return down
        elif downLeft not in rocks and downLeft not in sands:
            #print("moving down left")
            return downLeft
        elif downRight not in rocks and downRight not in sands:
            #print("moving down right")
            return downRight
        else:
            return currentSand
        
    rocks = []
    for line in lines:
        #print('***')
        line = line.strip('\n')
        points = line.split(' -> ')
        lastPoint = []
        for point in points:
            #print(point)
            point = eval('[' + point + ']')
            if len(lastPoint) > 0:
                if point[0] == lastPoint[0]:
                    x = point[0]
                    starty = min(point[1], lastPoint[1])
                    endy = max(point[1], lastPoint[1]) + 1
                    for y in range(starty, endy):
                        rocks.append([x, y])
                if point[1] == lastPoint[1]:
                    y = point[1]
                    startx = min(point[0], lastPoint[0])
                    endx = max(point[0], lastPoint[0]) + 1
                    for x in range(startx, endx):
                        rocks.append([x, y])
            lastPoint = deepcopy(point)
            #print(rocks)
            
    print(len(rocks))
    sands = []
    currentSand = [500, 0]
    while currentSand[1] < 200:
        lastSand = deepcopy(currentSand)
        currentSand = moveSand(currentSand, rocks, sands)
        if currentSand == lastSand:
            #print("New sand: " + str(currentSand))
            sands.append(currentSand)
            # Start with a new sand
            currentSand = [500, 0]
    #print(sands)
    print("Day 14 P1 result: " + str(len(sands)))
    
    bottomY = max([i[1] for i in rocks]) + 2
    print("Bottom Y: " + str(bottomY))
    for x in range(-500, 1500):
        rocks.append([x, bottomY])
    
    sands.clear()
    currentSand = [500, 0]
    while currentSand[1] < 200:
        lastSand = deepcopy(currentSand)
        currentSand = moveSand(currentSand, rocks, sands)
        if currentSand == lastSand:
            #print("New sand: " + str(currentSand))
            sands.append(currentSand)
            # Start with a new sand
            if currentSand == [500, 0]:
                break
            currentSand = [500, 0]
    #print(sands)
    
    
    print("Day 14 P2 result: " + str(len(sands)))
    return
    
def day15():
    
    inputFile = open('AOCday15.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    sensors = []
    minX = float('inf')
    maxX = -1 * float('inf')
    for line in lines:
        #print('***')
        line = line.strip('\n')
        positions = line.split('=')
        sensor = []
        for pos in positions:
            intString = re.sub(r"\D", "", pos)
            if len(intString) > 0:
                sensor.append(int(intString))
        minX = min(minX, sensor[0], sensor[2])
        maxX = max(maxX, sensor[0], sensor[2])
        sensor = [sensor[0], sensor[1], abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])]
        sensors.append(sensor)
        
    print(sensors)
    
    # for every point in the row, find the cloest sensor
    # if the sensor's beacon is closer to it, then that position is impossible
    
    result = 0
    y = 2_000_000
    print(minX)
    print(maxX)
    for x in range(-1000, 5_000_000):
        for i in range(len(sensors)):
            dist = abs(sensors[i][0] - x) + abs(sensors[i][1] - y)
            if dist <= sensors[i][2]:
                result += 1
                break
            
    result -= 1 # for beacon at x=31358, y=2000000
    print("Day 15 P1 result: " + str(result))
    
    timeNow = time.time()
    for x in range(2_595_657, 4_000_001):
        if x % 1_000 == 0:
            print(str(x) + " x complete with time: " + str(time.time() - timeNow))
            timeNow = time.time()
        for y in range(2753392, 2_800_001):
            possible = True
            for i in range(len(sensors)):
                dist = abs(sensors[i][0] - x) + abs(sensors[i][1] - y)
                if dist <= sensors[i][2]:
                    possible = False
                    break
            if possible:
                print("Day 15 P2 result: " + str(x*4_000_000 + y))
                return
    
def day16():
    
    class Valve:
        def __init__(self, name, rate, connected):
            self.name = name
            self.rate = rate
            self.connected = connected
        def __repr__(self):
            return "Valve: " + self.name + " rate = " + str(self.rate) + " connected to: " + str(self.connected) + "\n"

    
    inputFile = open('AOCday16.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    valves = dict()
    for line in lines:
        line = line.strip()
        (name, rate, connected) = re.findall('Valve (\w+) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* ([\w\s,]*)', line)[0]
        #print(name)
        #print(rate)
        #print(connected)
        
        newValve = Valve(name, int(rate), connected.split(', '))
        valves[name]=newValve
        
    #print(valves)
    
    q = [(0, 'AA', [], 0)]
    TIME = 30
    states = set()
    ps = {i: {} for i in range(TIME+1)}
    while q:
        time, current, p, pp = q.pop(0)
        #print(time)
        tup = (time, current, pp, len(p)) # accurate: tuple(sorted(p))
        if tup in states: 
            continue
        states.add(tup)
        if time == TIME + 1: 
            break
        # rate increase for all opened valves
        ip = sum([valves[valveName].rate for valveName in p])
        # create a new tuple based on the sorted valve names as index
        tt = tuple(sorted(p))
        
        # if time is not reaching 30, update dynamic programming values to the max possible one
        if time <= TIME: 
            ps[time][tt] = max(ps[time].get(tt, 0), pp)
        # if the current valve is not opened yet and the rate is > 0, add it to the queue
        if current not in p and valves[current].rate > 0:
            q.append((time+1, current, p+[current], pp+ip))
        # for all connected valves, add them without opening the current one
        for connectedV in valves[current].connected: 
            q.append((time+1, connectedV, p, pp+ip))
    ans = max(ps[30].values())
    print("Day 16 P1 result: " + str(ans))
    
    # for the case of working with an elephant, we only have 26 time
    # the most efficient results could only be possible by using the results that do not have any overlap the final opened valves
    ans = max(ans, max(ps[26][i] + ps[26][j] for i in ps[26] for j in ps[26] if not set(i) & set(j)))
    print("Day 16 P2 result: " + str(ans))
    
    
def day17():
    
    inputFile = open('AOCday17.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    def isValid(rockPos, rocksAtRest):
        for rock in rockPos:
            x, y = rock
            if x < 0 or x > 6 or y < 0:
                return False
            if rock in rocksAtRest:
                return False
        return True
        
    def move(rock, direction):
        x, y = rock
        dx, dy = direction
        return (x + dx, y + dy)
    
    def drop(rockPos, jetDir, jetTime, rocksAtRest):
        # find the starting Y position
        allHeights = [y for (_, y) in rocksAtRest]
        if len(allHeights) == 0:
            maxHeight = -1
        else:
            maxHeight = max(allHeights)
        rockPos = [move(rock, (0, maxHeight + 4)) for rock in rockPos]
        
        while True:
            # move to left or right
            jetIndex = jetTime % len(jetDir)
            newPos = [move(rock, dirMap[jetDir[jetIndex]]) for rock in rockPos]
            # if all rocks have legal positions, move it
            if isValid(newPos, rocksAtRest):
                #print("moving " + str(rockPos) + " to " + jetDir[jetIndex])
                rockPos = deepcopy(newPos)

            #print(rockPos)
            jetTime += 1
            
            # move down
            newPos = [move(rock, (0, -1)) for rock in rockPos]
            # if all rocks have legal positions, move it; otherwise, stop moving
            if isValid(newPos, rocksAtRest):
                rockPos = deepcopy(newPos)
                #print("moving " + str(rockPos) + " down")
            else:
                break
            #print(rockPos)
            
        return jetTime, rocksAtRest + rockPos
    
    rocks = [
        [(2, 0), (3, 0), (4, 0), (5, 0)],
        [(2, 1), (3, 0), (3, 1), (3, 2), (4, 1)],
        [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
        [(2, 0), (2, 1), (2, 2), (2, 3)],
        [(2, 0), (2, 1), (3, 0), (3, 1)]
    ]
    dirMap = { '<': (-1, 0), '>': (1, 0)}
    jetDirs = []
    for line in lines:
        line = line.strip()
        jetDirs = [i for i in line]
    
    #print(dirs)
    jetTime = 0
    rocksAtRest = []
    for i in range(2022):
        jetTime, rocksAtRest = drop(rocks[i % len(rocks)], jetDirs, jetTime, rocksAtRest)
        #print(rocksAtRest)
    
    #print(rocksAtRest)
    #plt.scatter(*zip(*rocksAtRest))
    print("Day 17 P1 result: " + str(max([y for (_, y) in rocksAtRest]) + 1))
    
    for i in range(1_000_000_000_000):
        jetTime, rocksAtRest = drop(rocks[i % len(rocks)], jetDirs, jetTime, rocksAtRest)
        if i % 1000 == 0:
            print(str(i) + " Done!")
    # or find the repeating pattern
    print("Day 17 P2 result: " + str(max([y for (_, y) in rocksAtRest]) + 1))
    
def day18():
    
    inputFile = open('AOCday18.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    cubes = []
    for line in lines:
        line = line.strip('\n')
        cubes.append(eval('(' + line + ')'))
    
    #print(cubes)
    addedCube = []
    result = 0
    for cube in cubes:
        x, y, z = cube
        exposedSides = 6
        if (x-1, y, z) in addedCube:
            exposedSides -= 2
        if (x+1, y, z) in addedCube:
            exposedSides -= 2
        if (x, y-1, z) in addedCube:
            exposedSides -= 2
        if (x, y+1, z) in addedCube:
            exposedSides -= 2
        if (x, y, z-1) in addedCube:
            exposedSides -= 2
        if (x, y, z+1) in addedCube:
            exposedSides -= 2
        result += exposedSides
        addedCube.append(cube)
    
    print("Day 18 P1 result: " + str(result))
    
    min_x = min(x for (x, _, _) in cubes)-1
    max_x = max(x for (x, _, _) in cubes)+1
    min_y = min(y for (_, y, _) in cubes)-1
    max_y = max(y for (_, y, _) in cubes)+1
    min_z = min(z for (_, _, z) in cubes)-1
    max_z = max(z for (_, _, z) in cubes)+1
    
    visited = set() | set(cubes)
    queue = [(min_x, min_y, min_z)]
    print(max_x, max_y, max_z)
    #lava = set()
    result = 0
    while queue:
        x, y, z = queue.pop(0)
        # skip invalid cubes
        if not (x in range(min_x, max_x+1) and y in range(min_y, max_y+1) and z in range(min_z, max_z+1)):
            continue
        # if already visited, skip
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        #print((x, y, z))
        # for all possible cube directions
        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            # if the next cube is not a droplet, add it to the queue
            if (x+dx, y+dy, z+dz) not in cubes:
                queue.append((x+dx, y+dy, z+dz))
            else: # else add current to lava becuase it is a droplet next to lava
                result +=1
        #print(result)
    print("Day 18 P2 result: " + str(result))
    
def day19():
    
    class Blueprint:
        def __init__(self, index, oreRobotReq, clayRobotReq, oreForORobot, clayForORobot, oreForGRobot, obsidianForGRobot):
            self.index = int(index)
            self.oreRobotReq = int(oreRobotReq)
            self.clayRobotReq = int(clayRobotReq)
            self.obsidianRobotReq = (int(oreForORobot), int(clayForORobot))
            self.geodeRobotReq = (int(oreForGRobot), int(obsidianForGRobot))
            self.numOreRobot = 1
            self.numClayRobot = 0
            self.numObsRobot = 0
            self.numGeodeRobot = 0
            self.ore = 0
            self.clay = 0
            self.obsidian = 0
            self.geode = 0
            self.time = 0
        def __repr__(self):
            return "\nBlueprint " + str(self.index) +  " at time " + str(self.time) +\
                "\n\tOre robot count: " + str(self.numOreRobot) + ": Clay robot count: " + str(self.numClayRobot) + ": Obsidian robot count: " + str(self.numObsRobot) + ": Geode robot count: " + str(self.numGeodeRobot) +\
                "\n\tOre count: " + str(self.ore) + ": Clay count: " + str(self.clay) + ": Obsidian count: " + str(self.obsidian) + ": Geode count: " + str(self.geode)
                

    def findGeode(blueprint, time):
        ro = blueprint.oreRobotReq
        rc = blueprint.clayRobotReq
        (roo, roc) = blueprint.obsidianRobotReq
        (rgo, rgob) = blueprint.geodeRobotReq
        q = [((0, 0, 0, 0, 0, 0, 0, 1), time)]
        states = set()
        ans = 0
        mco = max(rgo, roo, rc, ro)
        while q:
            tup = q[0][0]
            (g, gb, os, osb, c, cb, o, ob), t = q.pop(0)
        
            # t is the time you have left, so simplifying the resources will yield the same outcome
            o = min(o, t*mco)
            c = min(c, t*roc)
            os = min(os, t*rgob)
        
            # even if we create one new geode robot at a time, it's pointless
            ans = max(g, ans)
            if 2*ans > 2*(g+gb*t) + (t**2-t): continue
        
            if tup in states: continue
            states.add(tup)
            if t == 1:
                ans = max(g+gb, ans)
                continue
        
            g2, os2, c2, o2 = g+gb, os+osb, c+cb, o+ob
            # buy geodebot, high priority
            if o >= rgo and os >= rgob:
                q.append(((g2, gb+1, os2-rgob, osb, c2, cb, o2-rgo, ob), t-1))
            # buy obsibot
            if o >= roo and c >= roc:
                q.append(((g2, gb, os2, osb+1, c2-roc, cb, o2-roo, ob), t-1))
            # buy claybot
            if o >= rc:
                q.append(((g2, gb, os2, osb, c2, cb+1, o2-rc, ob), t-1))
            # buy orebot
            if o >= ro:
                q.append(((g2, gb, os2, osb, c2, cb, o2-ro, ob+1), t-1))
            # buy nothing
            q.append(((g2, gb, os2, osb, c2, cb, o2, ob), t-1))
        return ans
    
    inputFile = open('AOCday19.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    blueprints = []
    for line in lines:
        line = line.strip()
        (index, oreRobot, clayRobot, oreForORobot, clayForORobot, oreForGRobot, obsidianForGRobot) =\
            re.findall('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', line)[0]
        blueprints.append(Blueprint(index, oreRobot, clayRobot, oreForORobot, clayForORobot, oreForGRobot, obsidianForGRobot))
    
    #print(blueprints)
    
    result = 0
    print(findGeode(blueprints[0], 24))
    #for blueprint in blueprints:
    #    result += findGeode(blueprint, 24) * blueprint.index
        
    print("Day 19 P1 result: " + str(result))
    
    result = 1
    result *= findGeode(blueprints[0], 32)
    result *= findGeode(blueprints[1], 32)
    result *= findGeode(blueprints[2], 32)
        
    print("Day 19 P2 result: " + str(result))

def day20():
    
    inputFile = open('AOCday20.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    # keep their original order for indicies
    numbers = []
    indices = []
    i = 0
    for line in lines:
        line = line.strip('\n')
        numbers.append(int(line))
    
    #numbers = [1, 2, -3, 3, -2, 0, 4]
    #print(len(numbers))
    indices = [i for i in range(len(numbers))]
    
    # method 2
    coords = [(idx, int(item)) for idx, item in enumerate(numbers)]
    _len = len(coords)
    
    for i in range(len(numbers)):
        originalIndex = indices[i]
        #print("originalIndex: " + str(originalIndex))
        #newIndex = indices[i] + numbers[i]
        newIndex = (indices[i] + numbers[i] + len(numbers) - 1) % (len(numbers) - 1)
        #print("newIndex: " + str(newIndex))
        
        # if the new pos is greater than the current pos, move forward
        if newIndex > originalIndex:
            # moving from the first to last to the left
            for move in range(originalIndex + 1, newIndex + 1):
                realIndex = indices.index(move)
                indices[realIndex] -= 1
            indices[i] = newIndex
        # else move backward
        elif newIndex < originalIndex:
            # moving from the last to first to the right
            for move in range(originalIndex - 1, newIndex - 1, -1):
                realIndex = indices.index(move)
                indices[realIndex] += 1
            indices[i] = newIndex
        
        #print("index: " + str(i))
        #print(indices)
        #print([numbers[indices.index(order)] for order in range(len(numbers))])
        
        # method 2
        pos, coord = [(p, coord) for p, coord in enumerate(coords) if coord[0] == i][0]
        new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

        coords.pop(pos)
        coords.insert(new_pos, coord)
        
        #print(coords)
        method1 = [numbers[indices.index(order)] for order in range(len(numbers))]
        method2 = [num for p, num in coords]
        assert(len(method1) == len(method2))
        #diff = False
        #for z in range(len(method1)):
        #    if method1[z] != method2[z]:
        #        print("index: " + str(z) + " method 1: " + str(method1[z]) + " method 2: " + str(method2[z]))
        #        diff = True
        #if diff: return
        #print("***")
    
    zeroIndex = indices[numbers.index(0)]
    onekIndex = (zeroIndex + 1_000) % len(numbers)
    twokIndex = (zeroIndex + 2_000) % len(numbers)
    threekIndex = (zeroIndex + 3_000) % len(numbers)
    
    print(zeroIndex)
    print(numbers[indices.index(onekIndex)])
    print(numbers[indices.index(twokIndex)])
    print(numbers[indices.index(threekIndex)])
    result = numbers[indices.index(onekIndex)] + numbers[indices.index(twokIndex)] + numbers[indices.index(threekIndex)]
    print("Day 20 P1 result: " + str(result))
    
    zero_pos = [p for p, item in enumerate(coords) if item[1] == 0][0]
    print("***")
    print(zero_pos)
    #print(coords)
    print(coords[(zero_pos + 1000) % _len][1])
    print(coords[(zero_pos + 2000) % _len][1])
    print(coords[(zero_pos + 3000) % _len][1])
    
    key = 811589153
    coords = [(idx, int(item) * key) for idx, item in enumerate(numbers)]

    for _ in range(10):
        for i in range(_len):
            pos, coord = [(p, coord) for p, coord in enumerate(coords) if coord[0] == i][0]
            new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

            coords.pop(pos)
            coords.insert(new_pos, coord)

    zero_pos = [p for p, item in enumerate(coords) if item[1] == 0][0]
    print("***")
    print(zero_pos)
    print(coords[(zero_pos + 1000) % _len][1])
    print(coords[(zero_pos + 2000) % _len][1])
    print(coords[(zero_pos + 3000) % _len][1])
        
def day21():
    
    class Node:
        def __init__(self, name, operation, dependency, value):
            self.name = name
            self.operation = operation
            self.dependency = dependency
            self.value = value
        def __repr__(self):
            return " Node: " + self.name + " operation: " + str(self.operation) + \
                " dependency: " + str(self.dependency) + " value: " + str(self.value) + "\n"
    
    def evalNode(node, allNodes):
        if float(node.value) > -1 * float('inf'):
            return int(node.value)
        else:
            dep1 = evalNode(allNodes[node.dependency[0]], allNodes)
            dep2 = evalNode(allNodes[node.dependency[1]], allNodes)
            result = int(eval(str(dep1) + node.operation + str(dep2)))
            node.value = result
            return result
    
    def findHumn(node, allNodes):
        if len(node.dependency) == 0 :
            return node.name == "humn"
        else:
            dep1 = findHumn(allNodes[node.dependency[0]], allNodes)
            dep2 = findHumn(allNodes[node.dependency[1]], allNodes)
            return node.name == "humn" or dep1 or dep2
                                 
    
    inputFile = open('AOCday21.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    nodes = {}
    for line in lines:
        line = line.strip('\n')
        name, rest = line.split(": ")
        value = -1 * float('inf')
        dependency = []
        operation = ""
        if len(rest.split(" ")) > 1:
            dep1, operation, dep2 = rest.split(" ")
            dependency = [dep1, dep2]
        else:
            value = int(rest)
        
        nodes[name] = Node(name, operation, dependency, value)
        
    result = evalNode(nodes['root'], nodes)
    print(nodes)
    print("Day 21 P1 result: " + str(result))
    
    current = nodes['root']
    print(current)
    target = 0
    if findHumn(nodes[current.dependency[0]], nodes):
        target = evalNode(nodes[current.dependency[1]], nodes)
        print("target is from " + current.dependency[1])
        current = nodes[current.dependency[0]]
    else:
        target = evalNode(nodes[current.dependency[0]], nodes)
        print("target is from " + current.dependency[0])
        current = nodes[current.dependency[1]]
    print(target)
    
    while current.name != 'humn':
        otherNum = 0
        assert((findHumn(nodes[current.dependency[0]], nodes) and findHumn(nodes[current.dependency[1]], nodes)) == False)
        if findHumn(nodes[current.dependency[0]], nodes): # num2 is  known
            otherNum = evalNode(nodes[current.dependency[1]], nodes)
            if current.operation == '+':
                target -= otherNum
            if current.operation == '-':
                target += otherNum
            if current.operation == '*':
                target //= otherNum
            if current.operation == '/':
                target *= otherNum
            print("evaluating " + current.dependency[1])
            current = nodes[current.dependency[0]]
        else: # num1 is known
            otherNum = evalNode(nodes[current.dependency[0]], nodes)
            if current.operation == '+':
                target -= otherNum
            if current.operation == '-':
                target = otherNum - target
            if current.operation == '*':
                target //= otherNum
            if current.operation == '/':
                target = otherNum // target
            print("evaluating " + current.dependency[0])
            current = nodes[current.dependency[1]]
        print("other num: " + str(otherNum))
        print("new target: " + str(target))
    
    print("Day 21 P2 result: " + str(target))
    

def main():
    day21()

if __name__ == "__main__":
    main()
    
    