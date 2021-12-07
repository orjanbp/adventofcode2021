from . import helpers
import time


def advanceDays(days, adultFish: list, youngFish: list):
    popAdult = adultFish.pop(0)
    popYoung = youngFish.pop(0)

    adultFish = adultFish + [popAdult + popYoung]
    youngFish = youngFish + [popAdult + popYoung]

    print('Population for day ', days, ' =====')
    print(adultFish, youngFish)

    time.sleep(0.1)

    if (days > 0):
        return advanceDays(days - 1, adultFish, youngFish)
    else:
        return [adultFish, youngFish]


def printPuzzle6():
    data = helpers.fetchData()

    adultFish = [0] * 7
    youngFish = [0] * 9

    countedFish = helpers.countFishByAge(data[:])
    for i in countedFish.keys():
        adultFish[i+1] = countedFish[i]

    print(adultFish)

    print('## Calculating lanternfish population ...')
    print('')

    daysToAdvance = 256
    allFish = advanceDays(daysToAdvance, adultFish, youngFish)
    sum = helpers.sumAllFish(allFish)

    print('Final fish count: ', sum)
