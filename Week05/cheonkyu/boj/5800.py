n = int(input())

data = []
for _ in range(n):
  data.append(list(map(int, input().split())))

def solution(data):
  for i in range(0, len(data)):
    tmp = sorted(data[i][1:])
    max_val = max(tmp)
    min_val = min(tmp)
    
    gap = 0
    for j in range(1, len(tmp)):
        gap = max(tmp[j] - tmp[j-1], gap)
    print(f"Class {i + 1}")
    print(f"Max {max_val}, Min {min_val}, Largest gap {gap}")

solution(data)