from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    # 철수와 영희의 숫자 카드의 최대 공약수를 구함
    gcdA = nGCD(arrayA)
    gcdB = nGCD(arrayB)
    
    # 조건에 맞는지 검사함
    a1 = gcdA if condition(gcdA,arrayB) else 0
    a2 = gcdB if condition(gcdB,arrayA) else 0
    answer = max(a1,a2)
    return answer

# 정수 배열의 최대 공약수를 구하는 함수
def nGCD(array) :
    result = array[0]
    if ( len(array) == 1 ) :
        return result
    
    for i in range(1,len(array)) :
        result = gcd(result,array[i])
    return result

# 조건을 만족하는지 검사하는 함수
def condition(n,array) :
    if (n == 1) :
        return 0
    for a in array :
        if( a % n == 0) :
            return 0
    return 1