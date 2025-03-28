from collections import deque

# def bfs(computers, visited, start):
#     if visited[start[0]][start[1]]:
#         return 0
#     if visited[start[1]][start[0]]:
#         return 0
#     if computers[start[0]][start[1]] == 1:
#         visited[start[0]][start[1]] = True
#     else:
#         return 0
#     q = deque()
#     q.append(start)
#     print('-----')
#     # print(start)
#     moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     # moves = [(0, 1), (1, 0)]
#     # moves = [(0, 1)]
#     while q:
#         cur = q.popleft()
#         print(cur)
#         for _x, _y in moves:
#             pos = (cur[0] + _x, cur[1] + _y)
#             x, y = pos
#             if x < 0 or x >= len(computers) or y < 0 or y >= len(computers[0]):
#                 continue
#             if visited[x][y] == True:
#                 continue
#             # print(pos)
#             if computers[x][y] == 1:
#                 visited[x][y] = True
#                 # print(pos, (y,x))
#                 q.append(pos)
#             # q.append((y, x))
#     # print(visited)
#     return 1

def bfs(computers, visited, start):
    if visited[start][start]:
        return 0
    q = deque()
    q.append(computers[start])
    while q:
        cur = q.popleft()
        for i in range(len(cur)):
            if computers[start][i] == 1:
                visited[start][i] = True
                visited[i][start] = True
                bfs(computers, visited, i)
    return 1

def solution(n, computers):
    answer = 0
    visited = [[0] * len(computers[i]) for i in range(len(computers)) ]
    for i in range(len(computers)):
        answer += bfs(computers, visited, i)
    # print(answer)
    return answer


# solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2
# solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) # 1
# solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) # 1
# solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) # 3
# solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) # 2