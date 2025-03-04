def solution(babbling):
    answer = 0
    babySay = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        stack = []
        beforeSay = ''
        for char in b:
          stack.append(char)
          if ''.join(stack) in babySay and ''.join(stack) != beforeSay:
             beforeSay = ''.join(stack)
             stack = []
        # print(b, stack)
        if not stack:
           answer+=1
    # print(answer)
    return answer

solution(["aya", "yee", "u", "maa"]) # 1
# solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	) # 2