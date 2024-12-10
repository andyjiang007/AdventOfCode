# Advent of Code 2024 - Day 8
# @author: Andy

from itertools import combinations


def day8_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day8.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    result = 0
    antennaMap = {}
    allAntenna = set()
    rowSize = len(lines)
    colSize = len(lines[0])
    for row in range(rowSize):
        for col in range(colSize):
            if lines[row][col] != ".":
                freq = lines[row][col]
                allAntenna.add((row, col))
                if freq in antennaMap.keys():
                    antennaMap[freq].append((row, col))
                else:
                    antennaMap[freq] = [(row, col)]
    # print(f"{antennaMap=}")

    allNode = set()
    for antenna in antennaMap.keys():
        allCombo = list(combinations(antennaMap[antenna], 2))
        # print(f"{allCombo=}")
        for combo in allCombo:
            firstRow, firstCol = combo[0]
            secondRow, secondCol = combo[1]
            dx = firstRow - secondRow
            dy = firstCol - secondCol
            node1Row = firstRow + dx
            node2Row = secondRow - dx
            node1Col = firstCol + dy
            node2Col = secondCol - dy
            if 0 <= node1Row < rowSize and 0 <= node1Col < colSize:
                allNode.add((node1Row, node1Col))
            if 0 <= node2Row < rowSize and 0 <= node2Col < colSize:
                allNode.add((node2Row, node2Col))

    print(f"{allNode=}")
    result = len(allNode)
    print("Day 8 P1 result: " + str(result))

    return


def day8_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day8.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    result = 0
    antennaMap = {}
    allAntenna = set()
    rowSize = len(lines)
    colSize = len(lines[0])
    for row in range(rowSize):
        for col in range(colSize):
            if lines[row][col] != ".":
                freq = lines[row][col]
                allAntenna.add((row, col))
                if freq in antennaMap.keys():
                    antennaMap[freq].append((row, col))
                else:
                    antennaMap[freq] = [(row, col)]
    # print(f"{antennaMap=}")

    allNode = set(allAntenna)
    for antenna in antennaMap.keys():
        allCombo = list(combinations(antennaMap[antenna], 2))
        # print(f"{allCombo=}")
        for combo in allCombo:
            firstRow, firstCol = combo[0]
            secondRow, secondCol = combo[1]
            dx = firstRow - secondRow
            dy = firstCol - secondCol
            nodeRow = firstRow + dx
            nodeCol = firstCol + dy
            while 0 <= nodeRow < rowSize and 0 <= nodeCol < colSize:
                # print(
                #     f"Adding {nodeRow=}, {nodeCol=} from {firstRow=}, {firstCol=} and {secondRow=}, {secondCol=}"
                # )
                allNode.add((nodeRow, nodeCol))
                nodeRow += dx
                nodeCol += dy
            nodeRow = secondRow - dx
            nodeCol = secondCol - dy
            while 0 <= nodeRow < rowSize and 0 <= nodeCol < colSize:
                allNode.add((nodeRow, nodeCol))
                nodeRow -= dx
                nodeCol -= dy

    print(f"{allNode=}")
    result = len(allNode)

    print("Day 8 P2 result: " + str(result))

    return


def main():
    day8_pt1()
    day8_pt2()


if __name__ == "__main__":
    main()
