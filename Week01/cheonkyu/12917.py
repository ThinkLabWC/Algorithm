def sortString(str):
    a = list(str)
    b = sorted(a)
    b.reverse()
    return ''.join(b)

def solution(s):
    answer = sortString(s)
    return answer


solution("Zbcdefg")  # "gfedcbZ"