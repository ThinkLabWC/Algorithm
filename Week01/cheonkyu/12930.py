def solution(s):
    answer = ''
    str_list = s.split(' ')
    trans = []
    for str in str_list:
        new_str = ''
        for i in range(0, len(str)):
            char = str[i]
            if i % 2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            new_str += char
        trans.append(new_str)
    answer = ' '.join(trans)
    return answer