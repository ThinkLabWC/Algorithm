def solution(wallet, bill):
    answer = 0

    while wallet[0] < bill[0] or wallet[1] < bill[1]:
      [w, h] = bill
      if w > h:
          w = int(w / 2)
      else: 
          h = int(h / 2)
      answer += 1
      bill = [w, h]
      if w <= wallet[0] and h <= wallet[1]:
          break
      if w <= wallet[1] and h <= wallet[0]:
          break
    # print(answer)
    return answer


# solution([30, 15], [26, 17])
solution([50, 50], [100, 241])
