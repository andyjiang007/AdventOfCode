# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:31:02 2023

@author: Andy
"""

# Mapping of words to digits
number_words_to_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def day1_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day1.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    result = 0
    
    for line in lines:
        #print(line)
        digits = ''.join([char for char in line if char.isdigit()])
        #print(digits)
        parsed_number = int(digits[0] + digits[-1])
        #print(parsed_number)
        result += parsed_number
        #print('***')
    
    print("Day 1 P1 result: " + str(result))

    return
    

def day1_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day1.txt', 'r', encoding='UTF-8')
    lines = inputFile.readlines()
    inputFile.close()
    
    result = 0
    
    for line in lines:
        #print(line)
        
# =============================================================================
# The problem is a bit ambiguious so my original thought is to replace the words in-place
# to avoid double translation on any overlapping words, but it seems this is a wrong assumption :/
#         line_len = len(line)
#         for index in range(line_len):
#             if index+3 <= len(line) and line[index:index+3] in number_words_to_digits:
#                 line = line[:index] + number_words_to_digits[line[index:index+3]] + line[index+3:]
#             elif index+4 <= len(line) and line[index:index+4] in number_words_to_digits:
#                 line = line[:index] + number_words_to_digits[line[index:index+4]] + line[index+4:]
#             elif index+5 <= len(line) and line[index:index+5] in number_words_to_digits:
#                 line = line[:index] + number_words_to_digits[line[index:index+5]] + line[index+5:]
# =============================================================================

        digits = ""
        for i in range(len(line)):
            if line[i].isdigit():
                digits += line[i]
            for key in number_words_to_digits:
                if line[i:i+len(key)] == key:
                    digits += str(number_words_to_digits[key])
                    
        #print(digits)
        parsed_number = int(digits[0] + digits[-1])
        #print(parsed_number)
        result += parsed_number
        #print('***')
    
    print("Day 1 P2 result: " + str(result))
    
    return

def main():
    day1_pt1()
    day1_pt2()

if __name__ == "__main__":
    main()
    