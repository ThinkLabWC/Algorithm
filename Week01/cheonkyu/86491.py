def solution(sizes):
    answer = 0
    max_size = sizes[0]
    for i in range(1, len(sizes)):
        # print(max_size, sizes[i])
        # # [w, h] = sizes[i]
        # # [mw, mh] = max_size  
        w = min(sizes[i])
        h = max(sizes[i])
        mw = min(max_size)
        mh = max(max_size)
        if mw < w:
            mw = w
        if mh < h:
            mh = h
        max_size = [mw, mh]
    answer = max_size[0] * max_size[1] 
    # print(max_size)
    # print(answer)  
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) # 120
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) # 133