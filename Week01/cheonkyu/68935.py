def get_triple_data(n):
    target = n
    result = []
    while target >= 1:
        mod = target % 3
        target = int(target / 3)
        result.append(mod)
  
    return result

def to_decimal(triple):
    size = len(triple)
    result = 0
    for i in range(0, size):
        result += (triple[size-i - 1] * 3 ** (i))
    return result

def solution(n):
    answer = 0
    triple = get_triple_data(n)
    answer = to_decimal(triple)
    return answer

solution(45)

# a = get_triple_data(45)