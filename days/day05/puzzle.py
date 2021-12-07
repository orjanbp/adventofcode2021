import time
from . import helpers


def readAndParseVentData(diags: bool):
    lines = helpers.readDataFile()

    straightPoints = [helpers.lineToPoints(line, diags) for line in lines]
    flatPoints = [point for sublist in straightPoints for point in sublist]

    overlap = helpers.findOverlapPoints(flatPoints)
    print('Overlaps found: ', len(overlap))


def printPuzzle5():
    print('Find straight line overlaps ==')
    readAndParseVentData(diags=False)
    print('')
    print('Find diagonal overlaps ==')
    readAndParseVentData(diags=True)
