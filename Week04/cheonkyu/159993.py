from collections import deque
def find_point(maps, point):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == point:
              return (i, j)

def bfs(maps, visited, start, end):
    q = deque()
    q.append([start, 1])
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        [cur, score] = q.popleft()
        for _x, _y in moves:
            pos = (cur[0] + _x, cur[1] + _y)
            x, y = pos
            if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]):
                continue
            if visited[x][y]:
                continue
            if maps[x][y] == 'X':
                continue
            visited[x][y] = True
            # print(pos)
            if end[0] == x and end[1] == y:
              # print('find', score)
              return score
            q.append([pos, score+1])
    return -1
def solution(maps):
    answer = 0
    start = find_point(maps, 'S')
    lever = find_point(maps, 'L')
    end = find_point(maps, 'E')
    visited = [[0] * len(maps[i]) for i in range(len(maps))]
    start_to_lever = bfs(maps, visited, start, lever)
    if start_to_lever == -1:
        return -1
    visited = [[0] * len(maps[i]) for i in range(len(maps))]
    lever_to_end = bfs(maps, visited, lever, end)
    if lever_to_end == -1:
        return -1
    answer = start_to_lever + lever_to_end
    return answer

# solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]) #	16
# solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]) #	-1

solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]) #	-1