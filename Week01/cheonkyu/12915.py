# 정렬 조건 여러개일때
# https://stackoverflow.com/questions/20145842/python-sorting-by-multiple-criteria

def solution(strings, n):
    answer = []
    strings.sort(key = lambda x: (x[n], x))
    answer = strings
    return answer

# solution(["sun", "bed", "car"], 1)
# ["sun", "bed", "car"]	1	["car", "bed", "sun"]
# ["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]
solution(["abce", "abcd", "cdx"], 2)