# Advent of Code 2024 - Day 5
# @author: Andy

from collections import defaultdict, deque


def day5_pt1():
    # Using readlines()
    inputFile = open("aoc2024_day5.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    dependencyMap = {}
    listToUpdate = []
    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            firstNum = int(a)
            secondNum = int(b)
            if secondNum in dependencyMap.keys():
                dependencyMap[secondNum].append(firstNum)
            else:
                dependencyMap[secondNum] = [firstNum]
        elif "," in line:
            pages = line.split(",")
            pagesList = []
            for page in pages:
                pagesList.append(int(page))
            listToUpdate.append(pagesList)
    print(f"{dependencyMap=}")
    print(f"{listToUpdate=}")

    for update in listToUpdate:
        valid = True
        for i in range(0, len(update)):
            numberAfter = set([int(num) for num in update[i + 1 :]])
            curNum = int(update[i])
            if curNum not in dependencyMap.keys():
                continue
            expectedBefore = set(dependencyMap[curNum])
            intersection = numberAfter & expectedBefore
            if len(intersection) > 0:
                valid = False
                break
        if valid:
            midNum = int(update[len(update) // 2])
            # print(f"Adding {midNum=}")
            result += midNum
    print("Day 5 P1 result: " + str(result))

    return


def reorder_with_dependencies(array, adjacency_dict):
    # Step 1: Compute in-degrees for each node
    in_degree = defaultdict(int)
    for node in adjacency_dict:
        if node not in array:
            continue
        if node not in in_degree:
            in_degree[node] = 0
        for neighbor in adjacency_dict[node]:
            if neighbor in array:
                in_degree[neighbor] += 1
    # print(f"{in_degree=}")
    # Step 2: Perform Topological Sort using Kahn's Algorithm
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_sort = []

    while queue:
        node = queue.popleft()
        topo_sort.append(node)

        for neighbor in adjacency_dict.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0 and neighbor not in topo_sort:
                queue.append(neighbor)
    # print(f"{topo_sort=}")
    if len(topo_sort) != len(array):
        raise ValueError(
            f"Cannot sort topologically: {len(topo_sort)=} vs. {len(array)=}"
        )

    return topo_sort


def day5_pt2():
    # Using readlines()
    inputFile = open("aoc2024_day5.txt", "r", encoding="UTF-8")
    lines = inputFile.readlines()
    inputFile.close()

    result = 0
    dependencyMap = {}
    listToUpdate = []
    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            firstNum = int(a)
            secondNum = int(b)
            if secondNum in dependencyMap.keys():
                dependencyMap[secondNum].append(firstNum)
            else:
                dependencyMap[secondNum] = [firstNum]
        elif "," in line:
            pages = line.split(",")
            pagesList = []
            for page in pages:
                pagesList.append(int(page))
            listToUpdate.append(pagesList)
    print(f"{dependencyMap=}")
    print(f"{listToUpdate=}")

    for update in listToUpdate:
        valid = True
        for i in range(0, len(update)):
            numberAfter = set([num for num in update[i + 1 :]])
            curNum = update[i]
            if curNum not in dependencyMap.keys():
                continue
            expectedBefore = set(dependencyMap[curNum])
            intersection = numberAfter & expectedBefore
            if len(intersection) > 0:
                valid = False
                # print(f"{i=}:\tFound invalid page {intersection=}")
                break
        if not valid:
            reorderedList = reorder_with_dependencies(update, dependencyMap)
            # print(f"{reorderedList=}")
            midNum = int(reorderedList[len(reorderedList) // 2])
            # print(f"Adding {midNum=}")
            result += midNum

    print("Day 5 P2 result: " + str(result))

    return


def main():
    day5_pt1()
    day5_pt2()


if __name__ == "__main__":
    main()
