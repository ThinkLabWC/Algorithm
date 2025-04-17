N = int(input())

# 간달프의 군대의 각 종족의 점수는 다음과 같다.

# 호빗 - 1
# 인간 - 2
# 엘프 - 3
# 드워프 - 3
# 독수리 - 4
# 마법사 - 10
# 사우론의 군대의 점수는 다음과 같다.

# 오크 - 1
# 인간 - 2
# 워그(늑대) - 2
# 고블린 - 2
# 우럭하이 - 3
# 트롤 - 5
# 마법사 - 10
for i in range(0, N):
  a = list(map(int, input().split(' ')))
  b = list(map(int, input().split(' ')))

  score_a = 0
  score_a += a[0] * 1
  score_a += a[1] * 2
  score_a += a[2] * 3
  score_a += a[3] * 3
  score_a += a[4] * 4
  score_a += a[5] * 10


  score_b = 0
  score_b += b[0] * 1
  score_b += b[1] * 2
  score_b += b[2] * 2
  score_b += b[3] * 2
  score_b += b[4] * 3
  score_b += b[5] * 5
  score_b += b[6] * 10

  if score_a < score_b:
    print(f"Battle {i + 1}: Evil eradicates all trace of Good")
  elif score_a > score_b:
    print(f"Battle {i + 1}: Good triumphs over Evil")
  else:
    print(f"Battle {i + 1}: No victor on this battle field")



