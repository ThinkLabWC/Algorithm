def divisor(number):
    result = []
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            if i < number//i:
                result.append(number//i)
    return result 

def solution(number, limit, power):
    answer = 0
    for n in range(1, number + 1):
        p = len(divisor(n))
        if p <= limit:
          answer += p
        else:
          answer += power

    return answer

# a = solution(5, 3, 2) # 10
# a = solution(10, 3, 2) # 21