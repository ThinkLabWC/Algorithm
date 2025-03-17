import sys
from collections import deque
si = sys.stdin.readline
n = int(si())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
sys.setrecursionlimit(100005)

for _ in range(n - 1):
    x, y = list(map(int, si().split()))
    tree[x].append(y)
    tree[y].append(x)


def dfs(tree, visted, x, parents):
    if visted[x]:
        return 
    visted[x] = True
    
    for item in tree[x]:
      if visted[item]:
          # print(x, 'parent', item)
          parents[x] = item
          continue
      dfs(tree, visted, item, parents)


def solution(tree):
    visited = [0] * (len(tree))
    parents = [0] * (len(tree))
    dfs(tree, visited, 1, parents)
    print(parents)
    for i in range(2, len(parents)):
        print(parents[i])

# tree = [
#   [],
#   [4, 6],
#   [4],
#   [5, 6],
#   [1, 2, 7],
#   [3],
#   [1, 3],
#   [4]
# ]
solution(tree)

# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
