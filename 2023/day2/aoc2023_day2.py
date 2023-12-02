# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:59:01 2023

@author: Andy
"""

def day2_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day2.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    result = 0
    
    for line in lines:
        max_red = 0
        max_green = 0
        max_blue = 0
        
        game_line = line.split(':')
        #print(split1)
        game_id = int(''.join([char for char in game_line[0] if char.isdigit()]))
        
        split2 = game_line[1].split(';')
        for game_set in split2:
            #print(game_set)
            balls = game_set.split(', ')
            for ball in balls:
                #print(ball)
                num = int(''.join([char for char in ball if char.isdigit()]))
                if "red" in ball:
                    max_red = max(max_red, num)
                elif "green" in ball:
                    max_green = max(max_green, num)
                elif "blue" in ball:
                    max_blue = max(max_blue, num)
        
        #print('red: ' + str(max_red) + '\tgreen: ' + str(max_green) + '\tblue: ' + str(max_blue))
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            result += game_id
    
    print("Day 2 P1 result: " + str(result))

    return
    

def day2_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day2.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    result = 0
    
    for line in lines:
        max_red = 0
        max_green = 0
        max_blue = 0
        
        game_line = line.split(':')
        #print(split1)

        split2 = game_line[1].split(';')
        for game_set in split2:
            #print(game_set)
            balls = game_set.split(', ')
            for ball in balls:
                #print(ball)
                num = int(''.join([char for char in ball if char.isdigit()]))
                if "red" in ball:
                    max_red = max(max_red, num)
                elif "green" in ball:
                    max_green = max(max_green, num)
                elif "blue" in ball:
                    max_blue = max(max_blue, num)
        
        #print('red: ' + str(max_red) + '\tgreen: ' + str(max_green) + '\tblue: ' + str(max_blue))
        # Instead of adding the game IDs, add the multiplications of maximum number of balls
        # for each color that were present
        result += max_red * max_green * max_blue
    
    print("Day 2 P2 result: " + str(result))
    
    return

def main():
    day2_pt1()
    day2_pt2()

if __name__ == "__main__":
    main()
    