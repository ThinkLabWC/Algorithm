from collections import deque

def bfs(g, visited, x, y):
  queue = deque()
  visited[x][y] = True
  queue.append((x, y))
  move = [(-1,0),(1,0),(0, 1), (0, -1)]
  c = 0
  while queue:
    pos = queue.popleft()
    [px, py] = pos
    for m in move:
      (nx, ny) = m
      # print(px + nx)
      # print(g)
      if (px + nx) < 0 or (py + ny) < 0 or (py + ny) >= len(g[0]) or (px + nx) >= len(g):
        continue
      # print(py + ny, len(g[0]), (py + ny) > len(g[0]))
      if visited[px + nx][py + ny]:
        continue

      if g[px + nx][py + ny] == 1:
        visited[px + nx][py + ny] = True
        c += 1
        # print(px + nx, py + ny)
        queue.append((px + nx, py + ny))
      else:
        continue
  # print(c)
  return c

def solution():
  map = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
  ]
  visited = [[0] * len(map[i]) for i in range(len(map))]
  home_count = []
  for i in range(len(map)):
    for j in range(len(map[i])):
      if map[i][j] and not visited[i][j]:
        total = bfs(map, visited, i, j)
        total += 1
        home_count.append(total)
  print(len(home_count), home_count)

solution()

