# Advent of Code {YEAR} - Day {DAY}
# @author: Andy


def day{DAY}_pt1():
    # Using readlines()
    inputFile = open("aoc{YEAR}_day{DAY}.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    result = 0

    print("Day {DAY} P1 result: " + str(result))

    return


def day{DAY}_pt2():
    # Using readlines()
    inputFile = open("aoc{YEAR}_day{DAY}.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    result = 0

    print("Day {DAY} P2 result: " + str(result))

    return

def main():
    day{DAY}_pt1()
    day{DAY}_pt2()


if __name__ == "__main__":
    main()
