# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:09:40 2023

@author: Andy
"""
from enum import Enum
import functools
from collections import Counter


class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

card_value_map = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    }

card_value_map_pt2 = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0,
    }

def find_hand_type_pt1(hand):
    #print('***')
    hand_type = HandType.HIGH_CARD
    hand_frequency = Counter(hand)
    #print(hand_frequency)
    # Sort the frequency map by values in decending order
    sorted_frequency = sorted(hand_frequency.values(), reverse=True)
    #print(sorted_frequency)
    
    # Compare the frequency map to each hand type
    if sorted_frequency == [5]:
        hand_type = HandType.FIVE_OF_A_KIND
    elif sorted_frequency == [4, 1]:
        hand_type = HandType.FOUR_OF_A_KIND
    elif sorted_frequency == [3, 2]:
        hand_type = HandType.FULL_HOUSE
    elif sorted_frequency == [3, 1, 1]:
        hand_type = HandType.THREE_OF_A_KIND
    elif sorted_frequency == [2, 2, 1]:
        hand_type = HandType.TWO_PAIR
    elif sorted_frequency == [2, 1, 1, 1]:
        hand_type = HandType.ONE_PAIR
    #print(hand_type)
    return hand_type
    
def compare_hands_pt1(hand1, hand2):
    #print('***')
    hand1_type = find_hand_type_pt1(hand1)
    hand2_type = find_hand_type_pt1(hand2)
    
    if hand1_type == hand2_type:
        for i in range(len(hand1)):
            if card_value_map[hand1[i]] != card_value_map[hand2[i]]:
                return card_value_map[hand2[i]] - card_value_map[hand1[i]]
    return hand2_type.value - hand1_type.value

def day7_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day7.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = 0
    
    hands_map = {}
    for line in lines:
        cards = line.split(' ')[0]
        bid = line.split(' ')[1]
        hands_map[cards] = int(bid)
    #print(hands_map)
        
    hands = hands_map.keys()
    sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands_pt1))
    #print(sorted_hands)
    for i in range(len(sorted_hands)):
        result += hands_map[sorted_hands[i]] * (len(sorted_hands) - i)
    
    print("Day 7 P1 result: " + str(result))

    return

def find_hand_type_pt2(hand):
    #print('***')
    hand_type = HandType.HIGH_CARD
    hand_frequency = Counter(hand)
    #print(hand_frequency)
    sorted_frequency = sorted(hand_frequency.values(), reverse=True)
    #print(sorted_frequency)
    if 'J' in hand_frequency.keys():
        # If there is at least one Joker, take the max frequency from rest of the cards
        max_frequency = max([value for key, value in hand_frequency.items() if 'J' != key], default=0)
        if max_frequency + hand_frequency['J'] == 5:
            hand_type = HandType.FIVE_OF_A_KIND
        elif max_frequency + hand_frequency['J'] == 4:
            hand_type = HandType.FOUR_OF_A_KIND
        elif max_frequency + hand_frequency['J'] == 3:
            min_frequency = min([value for key, value in hand_frequency.items() if 'J' != key])
            if min_frequency == 2:
                hand_type = HandType.FULL_HOUSE
            else:
                hand_type = HandType.THREE_OF_A_KIND
        elif max_frequency + hand_frequency['J'] == 2:
            # Since there is at least one Joker, the max frequency for rest of the cards is also one
            # So it is only possible to have a one pair in this scenario
            hand_type = HandType.ONE_PAIR
    else:
        # If there is no Joker, compare the frequency map to each hand type
        if sorted_frequency == [5]:
            hand_type = HandType.FIVE_OF_A_KIND
        elif sorted_frequency == [4, 1]:
            hand_type = HandType.FOUR_OF_A_KIND
        elif sorted_frequency == [3, 2]:
            hand_type = HandType.FULL_HOUSE
        elif sorted_frequency == [3, 1, 1]:
            hand_type = HandType.THREE_OF_A_KIND
        elif sorted_frequency == [2, 2, 1]:
            hand_type = HandType.TWO_PAIR
        elif sorted_frequency == [2, 1, 1, 1]:
            hand_type = HandType.ONE_PAIR
    #print(hand_type)
    return hand_type

def compare_hands_pt2(hand1, hand2):
    #print('***')
    hand1_type = find_hand_type_pt2(hand1)
    hand2_type = find_hand_type_pt2(hand2)
    
    if hand1_type == hand2_type:
        for i in range(len(hand1)):
            if card_value_map_pt2[hand1[i]] != card_value_map_pt2[hand2[i]]:
                return card_value_map_pt2[hand2[i]] - card_value_map_pt2[hand1[i]]
    return hand2_type.value - hand1_type.value

def day7_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day7.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = 0
    
    hands_map = {}
    for line in lines:
        cards = line.split(' ')[0]
        bid = line.split(' ')[1]
        hands_map[cards] = int(bid)
    #print(hands_map)
        
    hands = hands_map.keys()
    sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands_pt2))
    #print(sorted_hands)
    for i in range(len(sorted_hands)):
        result += hands_map[sorted_hands[i]] * (len(sorted_hands) - i)
    
    print("Day 7 P2 result: " + str(result))
    return


def main():
    day7_pt1()
    #day7_pt2()

if __name__ == "__main__":
    main()
    