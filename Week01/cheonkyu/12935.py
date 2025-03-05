def solution(arr):
    answer = []
    i = arr.index(min(arr))
    arr.pop(i)
    answer = arr
    if not arr:
        return [-1]
    return answer
