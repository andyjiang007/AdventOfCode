# Advent of Code 2024 - Day 10
# @author: Andy

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def day10_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day10.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    startLocation = []
    rowSize = len(lines)
    colSize = len(lines[0])
    for i in range(rowSize):
        for j in range(colSize):
            if lines[i][j] == "0":
                startLocation.append((i, j))
    # print(f"{startLocation=}")

    result = 0
    for endPos in startLocation:
        queue = [endPos]
        visited = set()
        height = 0
        endPos = set()
        # print(f"Starting from {endPos}")
        while queue:
            queueSize = len(queue)
            for i in range(queueSize):
                curRow, curCol = queue.pop(0)
                # print(f"{curRow=}, {curCol=}")
                if (curRow, curCol) in visited:
                    continue
                if int(lines[curRow][curCol]) == 9:
                    endPos.add((curRow, curCol))
                    continue
                visited.add((curRow, curCol))

                for direction in DIRECTIONS:
                    (dx, dy) = direction
                    newRow = curRow + dx
                    newCol = curCol + dy
                    if (
                        0 <= newRow < rowSize
                        and 0 <= newCol < colSize
                        and int(lines[newRow][newCol]) == height + 1
                    ):
                        queue.append((newRow, newCol))
            # print(f"{queue=} after {height=}")
            height += 1

        # print(f"{endPos=}")
        result += len(endPos)

    print("Day 10 P1 result: " + str(result))

    return


def day10_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day10.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    startLocation = []
    rowSize = len(lines)
    colSize = len(lines[0])
    for i in range(rowSize):
        for j in range(colSize):
            if lines[i][j] == "0":
                startLocation.append((i, j))
    # print(f"{startLocation=}")

    result = 0
    for endPos in startLocation:
        queue = [endPos]
        height = 0
        rating = 0
        # print(f"Starting from {endPos}")
        while queue:
            queueSize = len(queue)
            for i in range(queueSize):
                curRow, curCol = queue.pop(0)
                # print(f"{curRow=}, {curCol=}"
                if int(lines[curRow][curCol]) == 9:
                    rating += 1
                    continue

                for direction in DIRECTIONS:
                    (dx, dy) = direction
                    newRow = curRow + dx
                    newCol = curCol + dy
                    if (
                        0 <= newRow < rowSize
                        and 0 <= newCol < colSize
                        and int(lines[newRow][newCol]) == height + 1
                    ):
                        queue.append((newRow, newCol))
            # print(f"{queue=} after {height=}")
            height += 1

        # print(f"{rating=}")
        result += rating

    print("Day 10 P2 result: " + str(result))

    return


def main():
    day10_pt1()
    day10_pt2()


if __name__ == "__main__":
    main()
