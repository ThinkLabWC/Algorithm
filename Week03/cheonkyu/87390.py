def solution(n, left, right):
    answer = []
    r = [i for i in range(1, n + 1)]
    result = []
    for i in range(left, right + 1):
        # print(i, max(int(i / n) - i % n, 0))
        d, m = divmod(i, n)
        if int(d) + 1 == n:
          result.append(n)
        else: 
          result.append(r[m] + max(int(d) - m, 0))
          # r[i] = r[m] + max(int(d) - m, 0)
    answer =result
    # print(r)
    print(answer)
    return answer

solution(3, 2, 5)
solution(4,	7,	14)