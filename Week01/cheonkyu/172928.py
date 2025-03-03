def getIndex(strings, substr):
    for i, string in strings:
        if substr in string:
            break
    return i or 0

def findStart(data):
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if "S" == data[i][j]:
                return (i, j)
    return (0, 0)

def checkRange(data, y, x):
    if x < 0 or y < 0:
        return False
    try:
        data[y][x]
        return True
    except Exception:
        return False
    
def checkStop(data, a, b):
    for i in range(a, b + 1):
        if data[i] == 'X':
          return True
    return False

def solution(park, routes):
    data = []
    for block in park:
        data.append(list(block))
    for route in routes:
        [direction, step] = route.split(' ')
        (y, x) = findStart(data)
        if direction == 'E':
            if not checkRange(data, y, x + int(step)):
                continue
            if checkStop(data[y], x, x + int(step)):
                continue
            tmp = data[y][x + int(step)]
            data[y][x + int(step)] = data[y][x]
            data[y][x] = tmp
        elif direction == 'W':
            if not checkRange(data, y, x - int(step)):
                continue
            if checkStop(data[y], x - int(step), x):
                continue
            tmp = data[y][x - int(step)]
            data[y][x - int(step)] = data[y][x]
            data[y][x] = tmp
        elif direction == 'S':
            if not checkRange(data, y + int(step), x):
                continue
            tmpList = []
            for i in range(0, len(data)):
                tmpList.append(data[i][x])
            if checkStop(tmpList, y, y + int(step)):
                continue
            tmp = data[y + int(step)][x]
            data[y + int(step)][x] = data[y][x]
            data[y][x] = tmp
        elif direction == 'N':
            if not checkRange(data, y - int(step), x):
                continue
            tmpList = []
            for i in range(0, len(data)):
                tmpList.append(data[i][x])
            if checkStop(tmpList,  y - int(step), y):
                continue
            tmp = data[y - int(step)][x]
            data[y - int(step)][x] = data[y][x]
            data[y][x] = tmp
    [a, b] = findStart(data)
    answer = [a, b]
    return answer

# solution(["SXO", "OXX", "OOO"] , ["E 4", "S 4", "N 4", "S 1", "S 1", "E 2"])
# solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1", "S 1", "E 2"])
# solution(["SXO", "XOO", "OOO"], ["W 1"])
# solution(["SOOXO", "OOOXO", "OXOOO", "XOOOO"], ["E 2", "S 2", "W 2", "S 1", "W 1"])
# solution(["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"])
# solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])
# solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])
# solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])
# solution(["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"])
solution(["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"])
