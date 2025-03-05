def solution(s):
    num_pair = [
        ("zero", "0"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five" , "5"),
        ("six" , "6"),
        ("seven" , "7"),
        ("eight" , "8"),
        ("nine" , "9"),
    ]
    for p in num_pair:
        s = s.replace(p[0], p[1])
    answer = int(s)
    return answer

solution("one4seveneight")