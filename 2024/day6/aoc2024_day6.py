# Advent of Code 2024 - Day 6
# @author: Andy

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def day6_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day6.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    startRow = -1
    startCol = -1
    rowSize = len(lines)
    colSize = len(lines[0])
    for i in range(rowSize):
        for j in range(colSize):
            if lines[i][j] == "^":
                startRow = i
                startCol = j
                break
        if startRow != -1:
            break

    print(f"{startRow=}, {startCol=}")
    curRow, curCol = (startRow, startCol)
    direction = 0
    visited = set()
    while True:
        dx, dy = DIRECTIONS[direction]
        nextRow = curRow + dx
        nextCol = curCol + dy
        if 0 <= nextRow < rowSize and 0 <= nextCol < colSize:
            if lines[nextRow][nextCol] != "#":
                visited.add((nextRow, nextCol))
                curRow = nextRow
                curCol = nextCol
            else:
                # Turn 90 degrees
                direction += 1
                if direction >= len(DIRECTIONS):
                    direction = 0
        else:
            break
    print(f"{visited=}")
    result = len(visited)
    print("Day 6 P1 result: " + str(result))

    return


def day6_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day6.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = []
    startRow = -1
    startCol = -1
    rowSize = len(lines)
    colSize = len(lines[0])
    for i in range(rowSize):
        for j in range(colSize):
            if lines[i][j] == "^":
                startRow = i
                startCol = j
                break
        if startRow != -1:
            break

    print(f"{startRow=}, {startCol=}")
    for obsRow in range(rowSize):
        for obsCol in range(colSize):
            if lines[obsRow][obsCol] in ["#", "^"]:
                continue
            curRow, curCol = (startRow, startCol)
            direction = 0
            visited = set()
            while True:
                dx, dy = DIRECTIONS[direction]
                nextRow = curRow + dx
                nextCol = curCol + dy
                if 0 <= nextRow < rowSize and 0 <= nextCol < colSize:
                    if lines[nextRow][nextCol] == "#" or (
                        nextRow == obsRow and nextCol == obsCol
                    ):
                        # Turn 90 degrees
                        direction += 1
                        if direction >= len(DIRECTIONS):
                            direction = 0
                    else:
                        if (nextRow, nextCol, direction) in visited:
                            result.append((obsRow, obsCol))
                            print(
                                f"Hitting a loop at: {nextRow=}, {nextCol=}, {direction=}"
                            )
                            break
                        visited.add((nextRow, nextCol, direction))
                        curRow = nextRow
                        curCol = nextCol

                else:
                    break
            # print(f"{visited=}")
    print("Day 6 P2 result: " + str(len(result)))

    return


def main():
    day6_pt1()
    day6_pt2()


if __name__ == "__main__":
    main()
