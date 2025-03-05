def solution(s):
    i = int(len(s) / 2)

    if len(s) % 2 != 0:
        return s[i]
    else:
        return s[i-1:i+1]

print(solution("abcde")) # "c"
print(solution("qwer")) # "c"
# "abcde"	"c"
# "qwer"	"we"