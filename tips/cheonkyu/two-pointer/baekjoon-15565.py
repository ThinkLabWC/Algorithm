import sys
def solution(toy, target):
  R = -1
  answer = float('inf')
  cnt = 0
  
  for L in range(len(toy) - target + 1):
    if toy[L] != 1:
      continue
    while R + 1 < len(toy) and cnt < target:
      R += 1
      if toy[R] == 1:
        cnt += 1
    # print(L, R, cnt)
    if cnt == target:
      answer = min(answer, R - L + 1)
    if toy[L] == 1:
      cnt -= 1
  if answer == float('inf'):
    print(-1)
  else:
    print(answer)
# solution([1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1], 4) 
# solution([1, 2, 2, 2, 2, 1, 2, 2, 2, 1], 2) 
# print(sum([1, 2, 2, 2, 1, 2, 1, 2, 2, 1]))
solution([2,2,2,2,1,2], 2) 