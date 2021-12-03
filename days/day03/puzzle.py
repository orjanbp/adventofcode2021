'''
The submarine has been making odd noises, and the diagnostics of the problem is a
long list of binary numbers that, if decoded properly, can tell me some things about
the status of the submarine.

First thing I should check is Power Consumption. I can find that by using the report
to generate the binaries for the Gamma Rate and Epsilon Rate -- the Power Consumption
is these two values multiplied.

To find the gamma rate, I need to find the most common bit in each of the bit positions,
and the epsilon rate is the least common. That'll give me two binaries, which I then need
to decode, and then multiply.

So I guess if the first one would be 10110, then the second one has to be 01001. That
is convenient; I just need to find the first and then flip it to find the other.

Next after that, have to verify life support rating -- same setup but it's the oxygen generator
rating multiplied by CO2 scrubber rating.

Both the Oxygen Generator rating and CO2 Scrubber rating can be found in the same report,
but the approach for finding them are different:

I have to filter down the data bit by bit, and at each step filter down to the numbers whose
bit in that spot is the more or less common one (e.g. more common are 1, 0, 0, 1 ...)

- Oxygen Generator is the most common
- CO2 Scrubber is the least common
'''

from . import data
from . import helpers
import time


def findEpsilonValue(gamma):
    # bit-flip the gamma value; each 0 becomes 1 and vice versa
    epsilon = []
    for bit in gamma:
        epsilon.append(1 if (bit == 0) else 0)
    return epsilon


def findGammaValue(report):
    # the gamma value is basically the most found bit in each
    # of the given placements in each item on the report array
    gammaValue = []
    reportColumns = helpers.generateReportColumns(report)

    # for each column in the 2D matrix reportColumns, find the
    # main bit and then append it to our final gammaValue
    for column in reportColumns:
        mainBit = helpers.findMainBit(column)
        gammaValue.append(mainBit)

    return gammaValue


def findMostCommon(report):
    # this thing needs to drill down each bit in the set to the most
    # common; if it is 1 in the first, keep lines starting with 1, etc.
    reportLines = [helpers.splitLine(line) for line in report]
    reducedLines = reportLines

    # let's step through the data one bit placement at a time, reducing
    # the dataset each time for the next iteration
    position = 0
    while position < len(reportLines[0]):
        mainBit = helpers.findMainBit([line[position] for line in reducedLines])
        reducedLines = [line for line in reducedLines if int(line[position]) == mainBit]

        time.sleep(0.1)
        print('Potential matches found: ', len(reducedLines), end="\r")
        position += 1 

        if len(reducedLines) == 1:
            break

    return reducedLines


def findLeastCommon(report):
    # same drill down as findMostCommon, but reversed so that it drills
    # down to the least common value
    reportLines = [helpers.splitLine(line) for line in report]
    reducedLines = reportLines

    # let's step through the data one bit placement at a time, reducing
    # the dataset each time for the next iteration
    position = 0
    while position < len(reportLines[0]):
        mainBit = helpers.findMainBit([line[position] for line in reducedLines])
        reducedLines = [line for line in reducedLines if int(line[position]) != mainBit]

        time.sleep(0.1)
        print('Potential matches found: ', len(reducedLines), end="\r")
        position += 1

        if len(reducedLines) == 1:
            break

    return reducedLines


def printPuzzle3():
    print('## PARSE DIAGNOSTICS DATA ')
    print('## Commence parse ... ')

    time.sleep(0.01)
    print('')

    gammaValue = findGammaValue(data.diagnostics)
    epsilonValue = findEpsilonValue(gammaValue)
    gammaDecimal = helpers.binaryToDecimal(gammaValue)
    epsilonDecimal = helpers.binaryToDecimal(epsilonValue)
    print('Gamma Value: %s (%s)' % (gammaDecimal, gammaValue))
    print('Epsilon Value: %s (%s)' % (epsilonDecimal, epsilonValue))

    time.sleep(0.01)
    print('')

    powerConsumption = (gammaDecimal * epsilonDecimal)
    print('Power consumption: %s' % (powerConsumption))

    time.sleep(0.01)
    print('')

    print('## Narrowing down oxygen rating ... ')

    print('')
    [oxygenRating] = findMostCommon(data.diagnostics)
    print('Potential match? ', oxygenRating)
    print('Decoded value: ', helpers.binaryToDecimal(oxygenRating))

    time.sleep(0.01)
    print('')

    print('## Narrowing down CO2 scrubber rating ... ')

    print('')
    [scrubberRating] = findLeastCommon(data.diagnostics)
    print('Potential match? ', scrubberRating)
    print('Decoded value: ', helpers.binaryToDecimal(scrubberRating))

    time.sleep(0.01)
    print('')

    oxygenDecimal = helpers.binaryToDecimal(oxygenRating)
    scrubberDecimal = helpers.binaryToDecimal(scrubberRating)
    lifeSupportRating = (oxygenDecimal * scrubberDecimal)
    print('Life support rating: %s' % (lifeSupportRating))
