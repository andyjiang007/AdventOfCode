# Advent of Code 2024 - Day 7
# @author: Andy

from itertools import product


def day7_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day7.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    for line in lines:
        target, values = line.strip().split(": ")
        valueList = values.split(" ")
        print(f"{valueList=}")
        combinations = list(product("+*", repeat=(len(valueList) - 1)))
        print(f"{combinations=}")

        for combo in combinations:
            value = int(valueList[0])
            i = 1
            for operation in combo:
                if operation == "*":
                    value *= int(valueList[i])
                elif operation == "+":
                    value += int(valueList[i])
                i += 1
            if value == int(target):
                print(f"Found matching combination: {combo}")
                result += value
                break

    print("Day 7 P1 result: " + str(result))

    return


def day7_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day7.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    for line in lines:
        target, values = line.strip().split(": ")
        valueList = values.split(" ")
        # print(f"{valueList=}")
        combinations = list(product("+*|", repeat=(len(valueList) - 1)))
        # print(f"{combinations=}")

        for combo in combinations:
            value = int(valueList[0])
            i = 1
            for operation in combo:
                if operation == "*":
                    value *= int(valueList[i])
                elif operation == "+":
                    value += int(valueList[i])
                elif operation == "|":
                    value = str(value) + valueList[i]
                    value = int(value)
                i += 1
                if value > int(target):
                    break
            if value == int(target):
                print(f"Found matching combination: {combo}")
                result += value
                break

    print("Day 7 P2 result: " + str(result))

    return


def main():
    day7_pt1()
    day7_pt2()


if __name__ == "__main__":
    main()
