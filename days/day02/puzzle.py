'''
Have the data, now I need to understand how to pilot the submarine.
The submarine can take a series of commands; [(forward|down|up) X],
where X is how many units to travel. 

Up and down changes depth, forward obviously moves forward. It already
has a course planned. 

The movement data is data.plannedRoute

First task, step through the planned movement and figure out what my 
depth and forward position will be after it is done. Then I need to
multiply those two together.

Second task, totally redo that first part to also track submarine aim,
which is where things get complicated. Because ...

- down X increases aim by X
- up X decreases aim by X
- forward X then becomes (forward += X, depth += X * aim)

'''

from . import data
import time


def splitDirAndDist(step):
    # return [dir: string, dist: int] of step
    [dir, dist] = step.split(' ')
    return [dir, int(dist)]


def summarizeMovement(route):
    # crunch the numbers on how far the submarine has moved; 
    # travelled is always increasing, depth fluctuates
    print('')
    print('Distance until destination:')

    aim = 0
    depth = 0
    travelled = 0

    for step in route:
        [dir, dist] = splitDirAndDist(step)
        if (dir == 'forward'):
            travelled += dist
            depth += (dist * aim)
        if (dir == 'down'):
            aim += dist
        if (dir == 'up'):
            aim -= dist

        print('[Aim: %s] [Depth: %s] [Travelled: %s] ' % (aim, depth, travelled), end='\r')
        time.sleep(0.001)

    return [travelled, depth]


def multiplyMovement(travelled, depth):
    # multiply and print movement multiplication
    time.sleep(0.05)
    print('')
    print('Multiplied: ', travelled * depth)


def printPuzzle2():
    print('## CALCULATE SUBMARINE MOVEMENT ROUTE ')
    print('## Commence calculations ... ')

    [travelled, depth] = summarizeMovement(data.plannedRoute)
    multiplyMovement(travelled, depth)
