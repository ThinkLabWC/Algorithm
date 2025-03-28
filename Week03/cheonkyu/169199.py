from collections import deque
import math

def find_start(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                return (i, j)

def bfs(board, visited, start):
    visited[start[0]][start[1]] = 1
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append(start)
    result = math.inf
    while q:
        cur = q.popleft()
        if board[cur[0]][cur[1]] == 'G':
            result = min(result, visited[cur[0]][cur[1]])
            break
        for x, y in move:
            new_cur = cur
            while (new_cur[0] + x >= 0 and new_cur[0] + x < len(board)) and (new_cur[1] + y >= 0 and new_cur[1] + y < len(board[0])):
                if board[new_cur[0] + x][new_cur[1] + y] == 'D':
                    break
                else:
                    new_cur = (new_cur[0] + x, new_cur[1] + y)
            if new_cur[0] < 0 or new_cur[0] >= len(board):
                continue
            if new_cur[1] < 0 or new_cur[1] >= len(board[0]):
                continue
            if new_cur == cur:
                continue
            if visited[new_cur[0]][new_cur[1]] >= 1:
                continue
            # print(new_cur, board[new_cur[0]][new_cur[1]], visited[cur[0]][cur[1]])
            visited[new_cur[0]][new_cur[1]] = visited[cur[0]][cur[1]] + 1
            if board[new_cur[0]][new_cur[1]] == 'G':
                result = min(result, visited[cur[0]][cur[1]])
                break
            q.append(new_cur)
    if result == math.inf:
        return -1
    return result

def solution(board):
    start = find_start(board)
    visited = [[0] * len(board[i]) for i in range(len(board))]
    answer = bfs(board, visited, start)
    return answer

# solution(["...D..R"]) #	7
# solution(["...D..R", ".D.G...", "....D.D"]) #	7
solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]) #	7
# solution([".D.R", "....", ".G..", "...D"]) #	-1