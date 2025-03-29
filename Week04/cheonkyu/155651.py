def check_gt_time(a, b):
    h, m = map(int, a.split(":"))
    m += 10
    if (m)// 60 == 1:
        h += 1
        m = (m) % 60
    _a = int(''.join([str(h).zfill(2), str(m).zfill(2)]))
    _b = int(b.replace(':', ''))
    return _a > _b

def solution(book_time):
    answer = 0
    book_time.sort(key = lambda x: (x[0], x[1]))
    end_times = []
    for time in book_time:
        print(end_times)
        if not end_times:
          end_times.append(time[1])
          answer += 1
        elif not check_gt_time(end_times[0], time[0]):
          end_times.pop(0)  
          end_times.append(time[1])
        else:
          end_times.append(time[1])
          answer += 1
        end_times.sort()
    print(answer)
    return answer

# solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])  # 3
# solution([["09:10", "10:10"], ["10:20", "12:20"]])
solution([["10:20", "12:55"], ["12:55", "13:30"]])
# 3
# '19:20'
# '17:00'
# '15:20'

# 3
# '19:20'
# '18:20'
# '17:00'