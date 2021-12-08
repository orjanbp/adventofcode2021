def fetchData():
    with open('./days/day07/data.txt') as file:
        data = file.readlines()
        return list(map(int, data[0].split(',')))
