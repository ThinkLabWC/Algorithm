def getDecimal(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    print(result)
    return result

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        d = getDecimal(i)
        if len(d) % 2 == 0:
          answer += i
        else:
          answer -= i
    return answer

solution(13, 17)