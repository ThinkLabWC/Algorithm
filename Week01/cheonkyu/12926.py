def solution(s, n):
    answer = ''
    str_list = s
    for s in str_list:
        if s == ' ':
            answer += s
            continue
        if ord('a') <= ord(s) and ord('z') >= ord(s):
            answer += chr(ord('a') + ((ord(s) - ord('a') + n) % 26))
        elif ord('A') <= ord(s) and ord('Z') >= ord(s):
            #  s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
            answer += chr(ord('A') + ((ord(s) - ord('A')+ n) % 26))
    return answer

solution('a B z', 4)
# print(ord('a'))
# print(ord('a') + 1)
# print(ord('z'))
# print(ord('a'))
# print(chr(99))
# print(ord('a') + (ord('b') + 1) % ord('z'))
# print(ord('a') + ((ord('z') + 4) % ord('z')))
# print((ord('z') + 4) % ord('z'))
# print((ord('z') + 1) % ord('a'))

print(12 % 10)

print(ord('a') + ((ord('z') + 4) % ord('z')))