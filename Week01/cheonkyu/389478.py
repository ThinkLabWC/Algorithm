def solution(n, w, num):
    answer = 0
    # [[1,12,13],[2,11,14],[3,10,15],[4,9,16,21],[5,8,17,20],[6,7,18,19]]
    # f = [[]] * w
    boxs = []
    for i in range(0, w):
        boxs.append([])
    bid = 0
    next = 1
    for i in range(1, n + 1):
        boxs[bid].append(i)
        if i % w == 0:
            next *= -1
            continue
        bid += next

    target = []
    for box in boxs:
        if num in box:
            target = box
            break
    answer = len(target) - target.index(num)
    # print(answer)
    return answer


# solution(4, 6, 8) # 3v
# solution(22, 6, 8) # 3
# solution(13, 3, 6) # 4
# [ [ [] for i in range(wid) ] for i in range(hgt) ]