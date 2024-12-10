# Advent of Code 2024 - Day 9
# @author: Andy


def day9_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day9.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    result = 0
    isFile = True
    diskMap = []
    fileNo = 0
    for char in lines[0]:
        if isFile:
            for i in range(int(char)):
                diskMap.append(fileNo)
            fileNo += 1
        else:
            for i in range(int(char)):
                diskMap.append(-1)
        isFile = not isFile
    # print(f"{diskMap=}")

    for i in range(len(diskMap) - 1, -1, -1):
        if diskMap[i] != -1:
            firstFree = diskMap.index(-1)
            if firstFree < i:
                diskMap[firstFree] = diskMap[i]
                diskMap[i] = -1
    # print(f"Updated: {diskMap}")
    for i in range(len(diskMap)):
        if diskMap[i] != -1:
            result += diskMap[i] * i

    print("Day 9 P1 result: " + str(result))

    return


def day9_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day9.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]
    inputFile.close()

    result = 0
    isFile = True
    fileMap = {}
    freeMap = {}
    totalFileLength = 0
    fileNo = 0
    for char in lines[0]:
        if isFile:
            if char != "0":
                fileMap[totalFileLength] = (int(char), fileNo)
            fileNo += 1
        else:
            if char != "0":
                freeMap[totalFileLength] = int(char)
        isFile = not isFile
        totalFileLength += int(char)
    # print(f"{fileMap=}")
    # print(f"{freeMap=}")

    for i in range(totalFileLength - 1, -1, -1):
        if i in fileMap.keys():
            fileLength, fileNo = fileMap[i]
            if fileLength <= 0:
                continue
            for j in range(i):
                if j in freeMap.keys() and freeMap[j] >= fileLength:
                    freeMap[j + fileLength] = freeMap[j] - fileLength
                    freeMap[j] = 0
                    fileMap[i] = (0, 0)
                    fileMap[j] = (fileLength, fileNo)
                    # print(f"Updating {i}:{fileMap[j]} and {j}:{freeMap[j]}")
                    break
    # print(f"Updated {fileMap=}")
    # print(f"Updated {freeMap=}")

    for i in range(totalFileLength):
        if i in fileMap.keys():
            fileLength, fileNo = fileMap[i]
            for index in range(i, i + fileLength):
                result += index * fileNo

    print("Day 9 P2 result: " + str(result))

    return


def main():
    day9_pt1()
    day9_pt2()


if __name__ == "__main__":
    main()
