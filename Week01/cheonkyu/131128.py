# 시간복잡도 이슈 https://school.programmers.co.kr/questions/83242
# 시간복잡도 O(len(X)+ len(Y))
def solution(X, Y):
    answer = ''
    n_XY = {'0':[0,0], '1':[0,0], '2':[0,0], '3':[0,0], '4':[0,0], '5':[0,0], '6':[0,0], '7':[0,0], '8':[0,0], '9':[0,0]}
    n_list = ['9','8','7','6','5','4','3','2','1','0']
    for i in X:
        n_XY[i][0] += 1
    for i in Y:
        n_XY[i][1] += 1

    for i in n_list:
        for j in range(min(n_XY[i])):
            answer += i

    if answer == '':
        return '-1'
    elif answer[0] == '0':
        return '0'

    return answer

# def getDigitCount(number):
#     numstr = str(number)
#     result = list([0] * 10)
#     for s in numstr:
#       result[int(s)] += 1
#     return result
    

# def solution(X, Y):
#     answer = ''
#     A = getDigitCount(X)
#     B = getDigitCount(Y)
    
#     matched = []

#     for i in range(0, len(A)):
#         # print(i , abs(A[i] - B[i]), A[i] != 0 and B[i] != 0 )
#         matched.append(min([A[i], B[i]]) if A[i] != 0 and B[i] != 0 else 0)

#     if sum(matched) == 0:
#        return "-1"

#     sampling = []
#     for i in range(0, len(matched)):
#        if matched[i] > 0:
#           print(matched[i])
#           for j in range(0, int(matched[i])):
#               sampling.append(str(i))
#     sampling.reverse()
#     answer = int(''.join(sampling))
#     return answer

solution("100", "123450")
# # "100"	"123450"	"10"
# print(list([0] * 10))


# print(list(range(0, 10)))