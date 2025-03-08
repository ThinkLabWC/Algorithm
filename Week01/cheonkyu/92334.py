def solution(id_list, report, k):
    answer = []
    r = list(set(report))
    report_history = {}
    black_history = {}
    for i in range(0, len(r)):
        [a, b]= r[i].split(' ')
        if not report_history.get(a):
          report_history[a] = [b]
        else:
          report_history[a].append(b)
        if not black_history.get(b):
          black_history[b] = [a]
        else:
          black_history[b].append(a)
    print('report_history', report_history)
    print('black_history', black_history)
    black_set = set()
    for id in id_list:
      if len(black_history.get(id, [])) >= k:
          black_set.add(id)
    # for black in black_history.items():
    black_set = list(black_set)

    result = []
    for id in id_list:
      count = 0
      for report_user in report_history.get(id, set()):
        if report_user in black_set:
            count += 1
      result.append(count)

    answer = result
    return answer
    


# solution(
#     ["muzi", "frodo", "apeach", "neo"]
#     ,["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#     , 2
# )

# solution(
#     ["con", "ryan"]
#     , ["ryan con", "ryan con", "ryan con", "ryan con"]
#     , 3
# )