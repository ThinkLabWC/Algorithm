def solution(x):
    return x % sum(list(str(x))) == 0