# , 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8
chess = [1, 1, 2, 2, 2, 8]
n = list(map(int, input().split()))
result = []
for i in range(0, len(chess)):
  result.append(str(chess[i] - n[i]))
print(' '.join(result))