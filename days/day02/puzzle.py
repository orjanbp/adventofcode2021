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
