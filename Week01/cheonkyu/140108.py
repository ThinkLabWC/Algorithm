def check_split_str(str):
    start = str[0]
    check = []
    for i in range(0, len(str)):
        before = check[i-1] if i > 0 else 0
        if str[i] == start:
            check.append(before + 1)
        else:
            check.append(before - 1)
        if check[i] == 0:
            start = str[min(i+1, len(str) - 1)]
    return check
def solution(str):
    answer = 0
    check = check_split_str(str)
    answer = check.count(0)
    answer += 1 if check[len(check) - 1] != 0 else 0
    # print(check)
    # print(answer)
    return answer

# solution("banana") # 3
# solution("abracadabra") # 6
# solution("aaabbaccccabba") # 3

# [1,0,1,0,1,0]
# [1,2,3,2,1,2,1,0]
# ['a','b','r','a','c','a','d','a','b','r','a']
# [ 1,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1]
