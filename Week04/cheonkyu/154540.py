from collections import deque

def bfs(maps, visited, start):
    if maps[start[0]][start[1]] == 'X':
        return 0
    if visited[start[0]][start[1]]:
        return 0
    visited[start[0]][start[1]] = True
    q = deque()
    q.append(start)
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    result = int(maps[start[0]][start[1]])
    # result = 0
    while q:
        cur = q.popleft()
        for _x, _y in moves:
            pos = (cur[0] + _x, cur[1] + _y)
            x, y = pos
            if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]):
                continue
            if visited[x][y]:
                continue
            if maps[x][y] == 'X':
                continue
            result += int(maps[x][y])
            q.append(pos)
            # print(pos)
            visited[x][y] = True
    # print(result)
    return result

def solution(maps):
    answer = []
    visited = [[0] * len(maps[i]) for i in range(len(maps))]
    
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
          score = bfs(maps, visited, (i, j))
          if score > 0:
              answer.append(score)
    answer.sort()
    if not answer:
        return [-1]
    # print(answer)
    return answer

solution(["X591X","X1X5X","X231X", "1XXX1"]) #	[1, 1, 27]
# solution(["XXX","XXX","XXX"]) # [-1]


# print((1,1) + (0,2))
# a = [1, 2, 3]
# b = [3, 4, 5]
# print([sum(x) for x in zip(a,b)])