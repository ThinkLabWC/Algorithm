def solution(friends, gifts):
    answer = 0
    history = [ [0]*len(friends) for i in range(len(friends))]
    meta = {}
    for i in range(len(friends)):
        meta[friends[i]] = i

    for gift in gifts:
        # a -> b, a가 b에게 선물
        [a, b] = gift.split(' ')
        history[meta[a]][meta[b]] += 1

    point = {}
    point_list = []
    for i in range(len(friends)):
      # print(friends[i])
      a = sum(history[i])
      b = 0
      for j in range(len(friends)):
          b += history[j][i]
      point[friends[i]] = (a - b)
      point_list.append(a - b)
    # print(point_list)

    next = dict(zip(friends, [0] * len(friends)))
    for i in range(len(friends)):
       for j in range(0, len(friends)):
          if i != j:
            # 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
            if abs(history[i][j] - history[j][i]) > 0:
               if history[i][j] < history[j][i]:
                  next[friends[j]] += 1
            elif history[i][j] == 0 and history[j][i] == 0 or history[i][j] ==  history[j][i]:
              if point_list[i] < point_list[j] and point[friends[i]] != point[friends[j]]:
                next[friends[j]] += 1
            # print(friends[i], '->', friends[j])
            # print(next[friends[j]], history[i][j], history[j][i])
              
    answer = max(next.values(), key=int)
    # print(answer)
    return answer

solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]) # 2
# solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]) # 4
# solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]) # 0
