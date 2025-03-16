from collections import deque

def bfs(g, visited, x):
  queue = deque()
  visited[x] = True
  print(x)
  queue.append(g[x])
  while queue:
    nodes = queue.popleft()
    for y in range(len(nodes)):
      if visited[nodes[y]]:
        continue
      visited[nodes[y]] = True
      # print(y, nodes[y])
      queue.append(g[nodes[y]])
def solution(computers, n):
  visited = [False] * (n + 1)
  bfs(computers, visited, 1)
  # 1번 노드 제외
  print(visited.count(True) - 1)

computers = [
  [],
  [2, 5],
  [1, 3, 5],
  [2],
  [7],
  [1, 6],
  [5,],
  [4]
]
solution(computers, 7)
