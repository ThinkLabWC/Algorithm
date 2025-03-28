# 2중 for문을 이용하여 문제를 해결하려 했으나 시간초과가 발생하게 되었습니다. 
# 그래서 다른 방법을 찾아보던 중 x값을 이용하여 y의 최대값을 구하는 방법을 알아내어 문제를 해결했습니다.
# 0부터 d+1까지 k의 간격으로 반복하는 for문을 이용하여 피타고라스 정리( y² = r² - x²)를 이용하여 y의 값을 구합니다. 
# max_y를 k로 나눈 정수 몫을 구하고 그 값에 +1을 하여 answer에 저장합니다. 반복이 끝나면 answer을 리턴합니다.
def solution(k, d):
    answer = 0
    v = [[0] * (k + d) for i in range(k + d)]
    # print(v)
    for i in range(0, k + d, k):
        for j in range(0, k + d, k):
            if v[j][i] == 1 or v[i][j] == 1:
                answer += 1
                continue
            if (i ** 2 + j ** 2) <= d ** 2:
                answer += 1
                v[i][j] = 1
                v[j][i] = 1
            # print((i ** 2 + j ** 2) ** 0.5)
    print(answer)
    return answer
# [1,2,3,4,5]
solution(2,	4)	# 6
#  (0, 0), (0, 2), (0, 4), (2, 0), (2, 2), (4, 0)
# solution(1,	5)	# 26
# 1	5	26