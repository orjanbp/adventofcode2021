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
'''

from . import data
import time


def binaryToDecimal(binary):
    # helper func to decode arrays of binary to decimal number
    binaryString = ''.join(str(i) for i in binary)
    return int(binaryString, 2)


def splitLine(line):
    # helper func to array-split a line, so "abc" = [a,b,c]
    return [num for num in line]


def findMainBit(column):
    # each column contains a long list of 0 and 1, of which this
    # finds and returns the most prominent of the two
    [zero, one] = [0, 0]

    for num in column:
        if (int(num) == 1):
            one += 1
        else:
            zero += 1

    return (1 if one > zero else 0)


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
    reportColumns = []

    # for each line, drill down and split its entries; putting
    # each placement into a corresponding array in the 2D matrix
    # that is reportColumns
    for line in report:
        split = splitLine(line)

        for i in range(len(split)):
            if not i < len(reportColumns):
                reportColumns.append([])
            reportColumns[i].append(split[i])

    # for each column in the 2D matrix reportColumns, find the
    # main bit and then append it to our final gammaValue
    for column in reportColumns:
        mainBit = findMainBit(column)
        gammaValue.append(mainBit)

    return gammaValue


def printPuzzle3():
    print('## PARSE DIAGNOSTICS DATA ')
    print('## Commence parse ... ')

    gammaValue = findGammaValue(data.diagnostics)
    epsilonValue = findEpsilonValue(gammaValue)

    gammaDecimal = binaryToDecimal(gammaValue)
    epsilonDecimal = binaryToDecimal(epsilonValue)

    powerConsumption = (gammaDecimal * epsilonDecimal)

    time.sleep(0.01)

    print('')
    print('Gamma Value: %s (%s)' % (gammaDecimal, gammaValue))
    print('Epsilon Value: %s (%s)' % (epsilonDecimal, epsilonValue))

    time.sleep(0.01)

    print('')
    print('Power consumption: %s' % (powerConsumption))
