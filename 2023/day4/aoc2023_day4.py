# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:07:51 2023

@author: Andy
"""

def day4_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day4.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = 0
    
    for line in lines:
       split1 = line.split(': ')
       numbers = split1[1].split(' | ')
       winning_num = numbers[0].split(' ')
       #print(winning_num)
       card_num = numbers[1].split(' ')
       card_num_filtered = []
       for item in card_num:
        try:
            # Try to convert the item to an integer
            int(item)
            # If successful, add it to the filtered list
            card_num_filtered.append(item)
        except ValueError:
            # If it raises a ValueError, skip it
            continue
       #print(card_num_filtered)
       
       winning_count = len(set(winning_num) & set(card_num_filtered))
       #print(winning_count)
       if winning_count > 0:
           result += 2 ** (winning_count - 1)
    
    print("Day 4 P1 result: " + str(result))

    return

def getTotalWinningCards(winning_counts, winning_count_map, current_card):
    if current_card not in winning_count_map.keys():
        result = 1
        current_winning_count = winning_counts[current_card]
        # Use DP to iteratively find out sum of the total number of winning cards
        for i in range(current_card + 1, current_card + 1 + current_winning_count):
            if i in winning_count_map.keys():
                result += winning_count_map[i]
            else:
                result += getTotalWinningCards(winning_counts, winning_count_map, i)
        # Use a map to store all the already calculated total number of winning cards
        winning_count_map[current_card] = result
    
    #print('returning result for ' + str(current_card) + '\twhich is ' + str(winning_count_map[current_card]))
    return winning_count_map[current_card]

def day4_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day4.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = 0
    winning_counts = []
    winning_count_map = {}
    
    for line in lines:
       split1 = line.split(': ')
       numbers = split1[1].split(' | ')
       winning_num = numbers[0].split(' ')
       #print(winning_num)
       card_num = numbers[1].split(' ')
       card_num_filtered = []
       for item in card_num:
           try:
               # Try to convert the item to an integer
               int(item)
               # If successful, add it to the filtered list
               card_num_filtered.append(item)
           except ValueError:
               # If it raises a ValueError, skip it
               continue
       #print(card_num_filtered)
       
       winning_count = len(set(winning_num) & set(card_num_filtered))
       #print(winning_count)
       winning_counts.append(winning_count)
    
    # Starts from Card 1 or index 0
    for card_num in range(len(lines)):
        #print(card_num)
        result += getTotalWinningCards(winning_counts, winning_count_map, card_num)
    
    print("Day 4 P2 result: " + str(result))
    
    return

def main():
    
    day4_pt1()
    day4_pt2()

if __name__ == "__main__":
    main()
    