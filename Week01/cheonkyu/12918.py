def solution(s):
    answer = True
    try:
        int(s)
        return answer and (len(s) == 4 or len(s) == 6)
    except Exception:
        return False
    

solution("1234")