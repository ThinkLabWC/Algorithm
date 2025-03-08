def convertTime(n): # 분 단위로 변환
    h = n // 100
    m = n % 100
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        s = startday
        schedule = convertTime(schedules[i])
        for time in timelogs[i]:
            if s in [6, 7]: # 주말 제외
                s += 1
                if s == 8:  # 일요일 지나면 월요일로
                    s = 1
                continue
            t = convertTime(time)
            if schedule + 10 < t:   # 지각
                break
            else:
                s += 1
        else:
            answer += 1

    return answer

# import datetime

# # date = datetime.datetime.strptime('1557', '%H%M')
# # date = date+datetime.timedelta(minutes=10)
# # print(date.strftime('%H%M'))

# # startday = 1은 월요일, 2는 화요일, 3은 수요일, 4는 목요일, 5는 금요일, 6은 토요일, 7은 일요일
# def solution(schedules, timelogs, startday):
#     answer = 0
#     # s = startday
#     prize_list = []
#     for i in range(0, len(schedules)):
#         # schedules[i]
#         # schedules[i] + 10
#         _limit = datetime.datetime.strptime(schedules[i], '%H%M')
#         limit = (_limit + datetime.timedelta(minutes=10)).strftime('%H%M')

#         timelog = timelogs[i]
#         s = startday
#         prize = True
#         for log in timelog:
#           # print(i, schedules[i], log, s)
#           if log <= limit:
#               True
#           else:
#               if s > 5:
#                 True
#               else:
#                 prize = False
#                 break
#           s = (s + 1) % 8
#         if prize:
#             prize_list.append(i)
#     answer = len(prize_list)
#     print(prize_list)
#     return answer


# # solution(
# #     [700, 800, 1100],
# #     [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]],
# #     5
# # )
# #	3

# # solution(
# #   [730, 855, 700, 720],
# #   [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]],
# #   1
# # )
# # 2


# # solution(
# #   [730, 855],
# #   [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835]],
# #   1
# # )


# # solution(
# #   [750],
# #   [[710, 700, 650, 735, 700, 931, 912]],
# #   1
# # )

# solution(
#   [1150],
#   [[710, 700, 650, 735, 700, 931, 912,]],
#   1
# )