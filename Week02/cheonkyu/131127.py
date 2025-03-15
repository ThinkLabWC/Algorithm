def solution(want, number, discount):
    
    # print(len(discount))
    wanted = sum(number)
    answer = 0
    # print(total)
    for i in range(0, len(discount) - wanted + 1):
      want_dict = dict(zip(want, number))
      for j in range(i, wanted + i):
          if discount[j] in want_dict and want_dict[discount[j]] > 0:
              want_dict[discount[j]] -= 1
      if sum(want_dict.values()) == 0:
        answer += 1      
    return answer

# solution(["banana", "apple", "rice", "pork", "pot"],	[3, 2, 2, 2, 1],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
#3
# solution(["apple"],	[10],	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])
#	0