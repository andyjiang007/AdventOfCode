# Advent of Code 2024 - Day 4
# @author: Andy


def day4_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day4.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    colSize = len(lines[0])
    rowSize = len(lines)
    for i in range(rowSize):
        for j in range(colSize):
            if lines[i][j] == "X":
                for dx, dy in DIRECTIONS:
                    valid = True
                    for step in range(3):
                        newRow = i + dx * (step + 1)
                        newCol = j + dy * (step + 1)
                        # print(f"{newRow=}, {newCol=}")
                        if 0 <= newRow < rowSize and 0 <= newCol < colSize:
                            if step == 0 and lines[newRow][newCol] != "M":
                                valid = False
                                break
                            if step == 1 and lines[newRow][newCol] != "A":
                                valid = False
                                break
                            if step == 2 and lines[newRow][newCol] != "S":
                                valid = False
                                break
                        else:
                            valid = False
                            break
                    if valid:
                        result += 1
                        print(f"Starting at ({i}, {j}) in direction ({dx}, {dy})")

    print("Day 4 P1 result: " + str(result))

    return


def day4_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day4.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    DIRECTIONS = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    colSize = len(lines[0])
    rowSize = len(lines)
    for i in range(rowSize):
        for j in range(colSize):
            if lines[i][j] == "A":
                valid = True
                xShape = []
                for dx, dy in DIRECTIONS:
                    newRow = i + dx
                    newCol = j + dy
                    # print(f"{newRow=}, {newCol=}")
                    if not (0 <= newRow < rowSize and 0 <= newCol < colSize):
                        valid = False
                        break

                    cell = lines[newRow][newCol]
                    if cell in {"M", "S"}:
                        xShape.append(cell)
                    else:
                        valid = False
                        break
                if valid:
                    print(f"{xShape=}")
                    firstHalf = xShape[:2]
                    secondHalf = xShape[2:]
                    if {"M", "S"} == set(firstHalf) and {"M", "S"} == set(secondHalf):
                        result += 1
                        print(f"Starting at ({i}, {j}) in direction ({dx}, {dy})")

    print("Day 4 P2 result: " + str(result))

    return


def main():
    day4_pt1()
    day4_pt2()


if __name__ == "__main__":
    main()
