from . import data
import time


def findIncreases(array):
    # Loop through items in range and find if each is higher
    # than last item in range.
    last = array[0]  # starting with first item, nothing is before it
    increases = 0

    for i in array:
        if (i > last):
            increases += 1
        last = i
    
    return increases


def findSlidingWindows(array):
    # Find 3-piece sliding windows of the array; 0-2, 1-3, 2-4, etc.
    windows = []

    # Do this simple, why not, just need i-i+2 after all
    for i in range(len(array)):
        if (i < int(len(array)-2)):
            sumOfWindow = array[i] + array[i+1] + array[i+2]
            windows.append(sumOfWindow)

    return windows


def printPuzzle1():
    print('## OCEAN FLOOR DEPTH SCANNER ')
    print('## Commence depth search ... ')
    
    time.sleep(1)
    windowsOfThree = findSlidingWindows(data.depthMap)
    increases = findIncreases(windowsOfThree)
    
    print('## Total depth increases found: ', increases)
