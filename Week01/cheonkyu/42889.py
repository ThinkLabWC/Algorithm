# O(n) 복잡도 (답 참고)
def solution(N, stages): # 실패율 O(n)
    sum_list=[0]*(N+2)
    dic_list={}
    stages.sort()
    now=len(stages)
    for i in stages:
        sum_list[i]+=1
        

    for i in range(1, N+1):
        if now==0:
            dic_list[i] = 0
            continue
        dic_list[i] = sum_list[i]/now
        now-=sum_list[i]
        
    return sorted(dic_list, key=lambda x : dic_list[x], reverse=True)

# O(n^2) 복잡도 (내가 구현)
# def solution(N, stages):
#     failed = []
#     for i in range(0, N):
#         failed.append((i, 0, 0))
#     # [(0, 0)] * N
#     targets = []
#     for stage in stages:
#         targets.append(range(0, stage))
#     for target in targets:
#         for i in target:
#             if i < N:
#                 failed[i] = (failed[i][0], failed[i][1], failed[i][2] + 1)
#             if i == len(target) - 1 and i < N:
#                 failed[i] = (failed[i][0], failed[i][1] + 1, failed[i][2])
#     per = sorted(failed, key = lambda x: (x[1]/x[2] if x[2] > 0 else 0), reverse=True)
#     answer = list(map(lambda x: x[0] + 1, per))
#     return answer

# solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) # [3,4,2,1,5]
# solution(4, [4,4,4,4]) # [3,4,2,1,5]

# a = (1,1)
# a = (a[0] + 2, a[1])
# print(a)