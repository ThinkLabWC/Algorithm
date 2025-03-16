from collections import deque

def bfs(maps, visited, start):
    dic = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    [x, y] = start
    visited[x][y] = 1
    queue = deque()
    queue.append(start)
    # tmp =[0,0,0]
    count = 0
    while queue:
        # count += len(queue)
        cur = queue.popleft()
        for d in dic:
            new_pos = [cur[0] + d[0], cur[1] + d[1]]
            if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(maps) or new_pos[1] >= len(maps[0]):
              continue
            if visited[new_pos[0]][new_pos[1]]:
                continue
            if maps[new_pos[0]][new_pos[1]] == 0:
                continue
            # print(new_pos)
            # count += 1
            # visited[new_pos[0]][new_pos[1]] = min(count, visited[new_pos[0]][new_pos[1]]) if visited[new_pos[0]][new_pos[1]] != 0 else count
            visited[new_pos[0]][new_pos[1]] = visited[cur[0]][cur[1]] + 1
            # print(maps[new_pos[0]][new_pos[1]])
            queue.append(new_pos)
            # tmp[0] += 1
            # print(count)
            
            if new_pos[0] == len(maps) - 1 and new_pos[1] == len(maps[0]) - 1:
              print(count, new_pos)
    print(count)

# def dfs(maps, visited, start, count):
#     dic = [(0, 1), (1, 0), (-1, 0), (0, -1)]
#     [x, y] = start
#     visited[x][y] = count
    
#     for d in dic:
#         cur = start
#         new_pos = [cur[0] + d[0], cur[1] + d[1]]
#         if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(maps) or new_pos[1] >= len(maps[0]):
#             continue
#         if visited[new_pos[0]][new_pos[1]]:
#             continue
#         if maps[new_pos[0]][new_pos[1]] == 0:
#             continue
#         count += 1
#         # print(count)
#         # visited[new_pos[0]][new_pos[1]] = min(count, visited[new_pos[0]][new_pos[1]]) if visited[new_pos[0]][new_pos[1]] != 0 else count
#         visited[new_pos[0]][new_pos[1]] = min(count, visited[new_pos[0]][new_pos[1]]) if visited[new_pos[0]][new_pos[1]] != 0 else count
#         # print(visited[new_pos[0]][new_pos[1]])
#         dfs(maps, visited, new_pos, count)

def solution(maps):
    answer = 0
    visited = [[0] * len(maps[0]) for i in range(len(maps))]
    bfs(maps, visited, [0,0])
    # print(visited)
    # # print(visited)
    # # dfs(maps, visited, [0,0], 1)
    # # print(maps)
    # # print(visited)
    if visited[len(maps) - 1][len(maps[0]) - 1] == 0:
        answer =  -1
    else:
        answer = visited[len(maps) - 1][len(maps[0]) - 1]
    print(answer)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) #	11
# solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]) # -1