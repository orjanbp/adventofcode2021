'''
Want to do something cool here as I go to basically accesss any of the days from
a main root file in the project.
'''

from days.day01.puzzle import printPuzzle1
from days.day02.puzzle import printPuzzle2
from days.day03.puzzle import printPuzzle3
from days.day04.puzzle import printPuzzle4
from days.day05.puzzle import printPuzzle5

puzzles = [
    printPuzzle1,
    printPuzzle2,
    printPuzzle3,
    printPuzzle4,
    printPuzzle5
]

inputString = 'Select day to run (1 - %s):'%(len(puzzles))
day = input(inputString)

findAndRunPuzzle = puzzles[int(day)-1]
if (findAndRunPuzzle):
    print('\n============\n')
    findAndRunPuzzle()
