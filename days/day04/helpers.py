def readDataFile():
    file = open('./days/day04/data.txt')
    return file.readlines()


def getBingoBoards(restLines: list[str]):
    bingoBoards = []
    board = 0
    for line in restLines:
        if (line.strip() == ''):
            bingoBoards.append([])
            board += 1
        else:
            bingoBoards[board-1].append(line.split())
    return bingoBoards


def getBingoNumbers(bingoLine: str):
    return bingoLine.strip().split(',')

    