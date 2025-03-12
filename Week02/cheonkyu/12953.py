def get_lcm(num1, num2):
    # n1 = min(num1, num2)
    n = max(num1, num2)
    while True:
        if n % num1 == 0 and n % num2 == 0:
            break
        n += 1
    lcm = n
    return lcm
    
def solution(arr):
    answer = 0
    lcm = arr
    for i in range(0, len(lcm) - 1):
        lcm[i + 1] = (get_lcm(lcm[i], lcm[i + 1]))
    answer = lcm[-1]
    return answer


solution([2,6,8,14]) #	168
solution([1,2,3]) #	6