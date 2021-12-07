from numbers import Number
from collections import Counter


def readDataFile():
    file = open('./days/day05/data.txt')
    return file.readlines()


def findVentVectors(line: str):
    start, end = line.strip().split(' -> ')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    return [(int(x1), int(y1)), (int(x2), int(y2))]


# still need to get comfortable with the [x for y in Z if ...]
# potential that Python has for iterating over lists
def lineToPoints(line: list[str], diags: bool):
    ((x1, y1), (x2, y2)) = findVentVectors(line)
    if x1 == x2:
        return [(x1, y) for y in (range(y1, y2+1) if y1 < y2 else range(y2, y1+1))]
    elif y2 == y1:
        return [(x, y1) for x in (range(x1, x2+1) if x1 < x2 else range(x2, x1+1))]
    elif diags:
        slope = round((y2-y1) / (x2-x1))
        intercept = y2-slope*x2
        return [(x, round(slope*x+intercept)) for x in (range(x1, x2+1) if x1 < x2 else range(x2, x1+1))]
    else:
        return []


def findOverlapPoints(flatPoints: list):
    occurrences = Counter(flatPoints)
    return [(point, count) for (point, count) in occurrences.items() if count > 1]
