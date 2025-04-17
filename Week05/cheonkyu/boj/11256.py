n = int(input())
def solution():
  data = list(map(int, input().split()))

  boxs = []
  for i in range(0, data[1]):
    [a, b] = map(int, input().split())
    boxs.append(a * b)

  candy = data[0]
  boxs = sorted(boxs, reverse=True)
  for i in range(len(boxs)):
    if candy <= 0:
      print(i)
      break
    candy -= boxs[i]

for i in range(0, n):
  solution()
# 20 5
# 3 4
# 2 5
# 1 8
# 3 3
# 2 5
