import time
import math
import statistics as stat
from . import helpers as h


def solveFirstPart(crabs):
    # Median calculation for first
    median = stat.median(crabs)
    fuelCosts = [abs(median - fuel) for fuel in crabs]

    print('Final crab position: %s' % median)
    print('Cost of fuel to move: %s' % sum(fuelCosts))


def solveSecondPart(crabs):
    # Attempt mean solve for second
    maxPos = max(crabs)
    minFuel = math.inf  # start with highest possible
    toPos = 0

    print('Initial max position: ', maxPos)
    print('Initial min fuel cost: ', minFuel)

    for pos in range(maxPos):
        print('')
        print('==== Calculating on pos [', pos, ']')
        reqFuel = 0
        for crab in crabs:
            steps = abs(pos - crab)
            crabFuel = (steps+1) * steps / 2
            reqFuel += crabFuel
        if reqFuel < minFuel:
            minFuel = reqFuel
            toPos = pos
        print('==== Proposed fuel cost [%s] vs min [%s]' % (reqFuel, minFuel))

    print('')
    print('==== Lowest fuel cost found: %s fuel to pos %s' % (minFuel, toPos))


def printPuzzle7():
    crabs = h.fetchData()

    solveFirstPart(crabs)
    solveSecondPart(crabs)
