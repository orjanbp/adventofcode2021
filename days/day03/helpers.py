def binaryToDecimal(binary):
    # helper func to decode arrays of binary to decimal number
    binaryString = ''.join(str(i) for i in binary)
    return int(binaryString, 2)


def splitLine(line):
    # helper func to array-split a line, so "abc" = [a,b,c]
    return [num for num in line]


def generateReportColumns(report):
    # for each line, drill down and split its entries; putting
    # each placement into a corresponding array in the 2D matrix
    # that is reportColumns
    reportColumns = []

    # drill through the report, line by line, to make columns
    for line in report:
        split = splitLine(line)

        # split line up, putting each bit into each column
        for i in range(len(split)):
            if not i < len(reportColumns):
                reportColumns.append([])
            reportColumns[i].append(split[i])

    return reportColumns


def findMainBit(column):
    # each column contains a long list of 0 and 1, of which this
    # finds and returns the most prominent of the two
    [zero, one] = [0, 0]

    for num in column:
        if (int(num) == 1):
            one += 1
        else:
            zero += 1

    return (1 if one >= zero else 0)
