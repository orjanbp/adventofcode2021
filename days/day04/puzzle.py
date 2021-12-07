
from . import helpers


def readAndParseData():
    lines = helpers.readDataFile()
    # first line are the bingo numbers, so let's get those
    bingoNumbers = helpers.getBingoNumbers(lines[0])
    bingoBoards = helpers.getBingoBoards(lines[1:])

    return bingoNumbers, bingoBoards


def checkLine(line: list):
    completed = True
    for place in line:
        if place.isdigit():
            completed = False
    return completed


def checkHorizCompletion(board: list):
    for line in board:
        if (checkLine(line)):
            return True


def checkVertCompletion(board: list):
    boardCols = [[], [], [], [], []]
    for line in board:
        for i, place in enumerate(line):
            boardCols[i].append(place)
    for col in boardCols:
        if (checkLine(col)):
            return True


def checkDiagCompletion(board: list):
    diags = [[], []]
    boardSize = len(board[0]) - 1
    for i in range(5):
        diags[0].append(board[i][i])
        diags[1].append(board[boardSize-i][boardSize-i])
    for line in diags:
        if(checkLine(line)):
            return True


def markOffBoard(numbers: list, board: list):
    markBoard = board
    for time, number in enumerate(numbers):
        for row, lines in enumerate(board):
            for col, place in enumerate(lines):
                if (place == number):
                    markBoard[row][col] = 'X'

        horizDone = checkHorizCompletion(markBoard)
        vertDone = checkVertCompletion(markBoard)
        diagDone = checkDiagCompletion(markBoard)

        if (horizDone or vertDone or diagDone):
            return time, number


def findSumOfRemainder(sumBoard):
    flatten = []
    for line in sumBoard:
        for place in line:
            if place.isdigit():
                flatten.append(place)

    sum = 0
    for num in flatten:
        sum += int(num)

    return sum


def printPuzzle4():
    bingoNumbers, bingoBoards = readAndParseData()

    fastTime = 0
    fastBoard = 0
    fastWin = 0

    slowTime = 0
    slowBoard = 0
    slowWin = 0
    
    # find fastest solve
    for i, board in enumerate(bingoBoards):
        time, number = markOffBoard(bingoNumbers, board)
        if (fastTime == 0) or (time < fastTime):
            fastTime = time
            fastBoard = i
            fastWin = number
        if (time > slowTime):
            slowTime = time
            slowBoard = i
            slowWin = number

    print('')
    print('## Fastest Completion')
    print('Completed in %s on board %s, last number %s'%(fastTime, fastBoard, fastWin))
    print(fastBoard, bingoBoards[fastBoard])

    print('')
    print('## Slowest Completion')
    print('Completed in %s on board %s, last number %s'%(slowTime, slowBoard, slowWin))
    print(slowBoard, bingoBoards[slowBoard])

    fastSum = findSumOfRemainder(bingoBoards[fastBoard])
    slowSum = findSumOfRemainder(bingoBoards[slowBoard])

    fastMult = int(fastSum) * int(fastWin)
    slowMult = int(slowSum) * int(slowWin)

    print('')
    print('Fast sum [%s] - times win number [%s]'%(fastSum, fastMult))
    print('Slow sum [%s] - times win number [%s]'%(slowSum, slowMult))
