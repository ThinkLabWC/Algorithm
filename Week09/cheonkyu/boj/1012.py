from collections import deque

T = int(input())

def init():
  [M, N, K] = list(map(int, input().split()))
  m = [[0] * N for i in range(M)]
  visited = [[0] * N for i in range(M)]

  for i in range(K):
    [x, y] = list(map(int, input().split()))
    m[x][y] = 1
  return [m, visited]

def bfs(m, visited, x, y): 
  if m[x][y] == 0:
    return 0
  if visited[x][y]:
    return 0
  visited[x][y] = 1
  q = deque()
  q.append((x, y))
  moved = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  while q:
    current = q.popleft()
    for move in moved:
      next = (current[0] + move[0], current[1] + move[1])
      _x = next[0]
      _y = next[1]
      if _x < 0 or _x >= len(visited) or _y < 0 or _y >= len(visited[0]):
        continue
      if m[_x][_y] == 0:
        continue
      if visited[_x][_y]:
        continue
      visited[_x][_y] = 1
      # print(q)
      q.append((_x, _y))
  return 1

for _ in range(T):
  [m, visited] = init()
  total = 0
  for x in range(0, len(m)):
    for y in range(0, len(m[0])):
      total += bfs(m, visited, x, y)
  print(total)