# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:00:24 2023

@author: Andy
"""

seed_to_soil_seed = []
seed_to_soil_soil = []

soil_to_fert_soil = []
soil_to_fert_fert = []

fert_to_water_fert = []
fert_to_water_water = []

water_to_light_water = []
water_to_light_light = []

light_to_temp_light = []
light_to_temp_temp = []

temp_to_humi_temp = []
temp_to_humi_humi = []

humi_to_loc_humi = []
humi_to_loc_loc = []

seed_to_location = {}

# Map a seed num to its final location index
def findLocation(seed):
    #print("Starting with seed: " + str(seed))
    if seed in seed_to_location.keys():
        return seed_to_location[seed]
    
    current_index = seed
    for mapping_index in range(len(seed_to_soil_seed)):
        if seed_to_soil_seed[mapping_index][0] <= current_index < seed_to_soil_seed[mapping_index][1]:
            current_index = seed_to_soil_soil[mapping_index][0] + (current_index - seed_to_soil_seed[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(soil_to_fert_soil)):
        if soil_to_fert_soil[mapping_index][0] <= current_index < soil_to_fert_soil[mapping_index][1]:
            current_index = soil_to_fert_fert[mapping_index][0] + (current_index - soil_to_fert_soil[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(fert_to_water_fert)):
        if fert_to_water_fert[mapping_index][0] <= current_index < fert_to_water_fert[mapping_index][1]:
            current_index = fert_to_water_water[mapping_index][0] + (current_index - fert_to_water_fert[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(water_to_light_water)):
        if water_to_light_water[mapping_index][0] <= current_index < water_to_light_water[mapping_index][1]:
            current_index = water_to_light_light[mapping_index][0] + (current_index - water_to_light_water[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(light_to_temp_light)):
        if light_to_temp_light[mapping_index][0] <= current_index < light_to_temp_light[mapping_index][1]:
            current_index = light_to_temp_temp[mapping_index][0] + (current_index - light_to_temp_light[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(temp_to_humi_temp)):
        if temp_to_humi_temp[mapping_index][0] <= current_index < temp_to_humi_temp[mapping_index][1]:
            current_index = temp_to_humi_humi[mapping_index][0] + (current_index - temp_to_humi_temp[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(humi_to_loc_humi)):
        if humi_to_loc_humi[mapping_index][0] <= current_index < humi_to_loc_humi[mapping_index][1]:
            current_index = humi_to_loc_loc[mapping_index][0] + (current_index - humi_to_loc_humi[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    #print("Returning location: " + str(current_index))
    seed_to_location[seed] = current_index
    return current_index

def day5_pt1():

    # Using readlines()
    inputFile = open('aoc2023_day5.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = float('inf')
    
    seeds = []

    mapping_index = -1
    for i in range(len(lines)):
        if i == 0:
            split1 = lines[i].split(': ')
            seeds = split1[1].split(' ')
        elif len(lines[i]) == 0:
            mapping_index += 1
        elif 'map' in lines[i]:
            continue
        else:
            numbers = lines[i].split(' ')
            dest_start = int(numbers[0])
            dest_end = int(numbers[0]) + int(numbers[2])
            source_start = int(numbers[1])
            source_end = int(numbers[1]) + int(numbers[2])
            if mapping_index == 0:
                seed_to_soil_seed.append((source_start, source_end))
                seed_to_soil_soil.append((dest_start, dest_end))
            elif mapping_index == 1:
                soil_to_fert_soil.append((source_start, source_end))
                soil_to_fert_fert.append((dest_start, dest_end))
            elif mapping_index == 2:
                fert_to_water_fert.append((source_start, source_end))
                fert_to_water_water.append((dest_start, dest_end))
            elif mapping_index == 3:
                water_to_light_water.append((source_start, source_end))
                water_to_light_light.append((dest_start, dest_end))
            elif mapping_index == 4:
                light_to_temp_light.append((source_start, source_end))
                light_to_temp_temp.append((dest_start, dest_end))
            elif mapping_index == 5:
                temp_to_humi_temp.append((source_start, source_end))
                temp_to_humi_humi.append((dest_start, dest_end))
            elif mapping_index == 6:
                humi_to_loc_humi.append((source_start, source_end))
                humi_to_loc_loc.append((dest_start, dest_end))
    
    for seed in seeds:
        result = min(result, findLocation(int(seed)))
        
    print(seed_to_soil_seed)
    print(seed_to_soil_soil)
    print("Day 5 P1 result: " + str(result))

    return

# Map a location num to its original seed index
def findLocationInverse(location):
    #print("Starting with location: " + str(location))
    
    current_index = location
    for mapping_index in range(len(humi_to_loc_loc)):
        if humi_to_loc_loc[mapping_index][0] <= current_index < humi_to_loc_loc[mapping_index][1]:
            current_index = humi_to_loc_humi[mapping_index][0] + (current_index - humi_to_loc_loc[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(temp_to_humi_humi)):
        if temp_to_humi_humi[mapping_index][0] <= current_index < temp_to_humi_humi[mapping_index][1]:
            current_index = temp_to_humi_temp[mapping_index][0] + (current_index - temp_to_humi_humi[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(light_to_temp_temp)):
        if light_to_temp_temp[mapping_index][0] <= current_index < light_to_temp_temp[mapping_index][1]:
            current_index = light_to_temp_light[mapping_index][0] + (current_index - light_to_temp_temp[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(water_to_light_light)):
        if water_to_light_light[mapping_index][0] <= current_index < water_to_light_light[mapping_index][1]:
            current_index = water_to_light_water[mapping_index][0] + (current_index - water_to_light_light[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(fert_to_water_water)):
        if fert_to_water_water[mapping_index][0] <= current_index < fert_to_water_water[mapping_index][1]:
            current_index = fert_to_water_fert[mapping_index][0] + (current_index - fert_to_water_water[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(soil_to_fert_fert)):
        if soil_to_fert_fert[mapping_index][0] <= current_index < soil_to_fert_fert[mapping_index][1]:
            current_index = soil_to_fert_soil[mapping_index][0] + (current_index - soil_to_fert_fert[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    
    for mapping_index in range(len(seed_to_soil_soil)):
        if seed_to_soil_soil[mapping_index][0] <= current_index < seed_to_soil_soil[mapping_index][1]:
            current_index = seed_to_soil_seed[mapping_index][0] + (current_index - seed_to_soil_soil[mapping_index][0])
            #print("updated current index: " + str(current_index))
            break
    #print("Returning seed: " + str(current_index))
    return current_index

def day5_pt2():

    # Using readlines()
    inputFile = open('aoc2023_day5.txt', 'r', encoding='UTF-8')
    # Need to strip the extra newline char to make sure it is not counted as part of the input
    lines = [s.strip('\n') for s in inputFile.readlines()]
    inputFile.close()
    
    result = float('inf')
    
    seeds = []

    mapping_index = -1
    for i in range(len(lines)):
        if i == 0:
            split1 = lines[i].split(': ')
            seeds = split1[1].split(' ')
        elif len(lines[i]) == 0:
            mapping_index += 1
        elif 'map' in lines[i]:
            continue
        else:
            numbers = lines[i].split(' ')
            dest_start = int(numbers[0])
            dest_end = int(numbers[0]) + int(numbers[2])
            source_start = int(numbers[1])
            source_end = int(numbers[1]) + int(numbers[2])
            if mapping_index == 0:
                seed_to_soil_seed.append((source_start, source_end))
                seed_to_soil_soil.append((dest_start, dest_end))
            elif mapping_index == 1:
                soil_to_fert_soil.append((source_start, source_end))
                soil_to_fert_fert.append((dest_start, dest_end))
            elif mapping_index == 2:
                fert_to_water_fert.append((source_start, source_end))
                fert_to_water_water.append((dest_start, dest_end))
            elif mapping_index == 3:
                water_to_light_water.append((source_start, source_end))
                water_to_light_light.append((dest_start, dest_end))
            elif mapping_index == 4:
                light_to_temp_light.append((source_start, source_end))
                light_to_temp_temp.append((dest_start, dest_end))
            elif mapping_index == 5:
                temp_to_humi_temp.append((source_start, source_end))
                temp_to_humi_humi.append((dest_start, dest_end))
            elif mapping_index == 6:
                humi_to_loc_humi.append((source_start, source_end))
                humi_to_loc_loc.append((dest_start, dest_end))
    
    print(seeds)
    seed_ranges = list(zip(seeds[::2], seeds[1::2]))
    # Start from location 0 and use a inverse lookup to find the first valid seed
    # This method takes ~20 mins to finish so there could be more efficient ways
    for location in range(int(1e9)):
        if location % 100000 == 0:
            print("Processing location: " + str(location))
        start_seed = findLocationInverse(location)
        for seed_start, size in seed_ranges:
            if int(seed_start) <= start_seed < int(seed_start) + int(size):
                result = location
                print("Day 5 P2 result: " + str(result))
                return
    


def main():
    
    day5_pt1()
    day5_pt2()

if __name__ == "__main__":
    main()
    