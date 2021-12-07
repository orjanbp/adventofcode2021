from collections import Counter


def fetchData():
    with open('./days/day06/data.txt') as file:
        data = file.readlines()
        return [int(item) for item in data[0].split(',')]


def countFishByAge(fish):
    count = Counter(fish)
    return count

def sumAllFish(lists: list[list[str]]):
    return sum([fish for list in lists for fish in list])
    