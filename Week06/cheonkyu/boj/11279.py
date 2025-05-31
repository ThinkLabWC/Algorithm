from sys import stdin
import heapq
n = int(stdin.readline())

heap = []
for _ in range(0, n):
  num = int(stdin.readline())
  if num == 0:
    if heap:
      a = heapq.heappop(heap)
      print(a * -1)
    else:
      print(0)
  else:
    heapq.heappush(heap, num * -1)
