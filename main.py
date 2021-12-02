'''
Want to do something cool here as I go to basically accesss any of the days from
a main root file in the project.
'''

from days.day01.puzzle import printPuzzle1
from days.day02.puzzle import printPuzzle2

puzzles = [
    printPuzzle1,
    printPuzzle2
]

inputString = 'Select day to run (1 - %s):'%(len(puzzles))
day = input(inputString)

findAndRunPuzzle = puzzles[int(day)-1]
if (findAndRunPuzzle):
    print('\n============\n')
    findAndRunPuzzle()
