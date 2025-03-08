def next(pos):
    [m,s] = pos.split(':')
    s = int(s) + 10
    if s >= 60:
        m = int(m) + 1
        s = s % 60
    return str(m).rjust(2, '0') + ":" + str(s).rjust(2, '0')

def prev(pos):
    [m,s] = pos.split(':')
    s = int(s) - 10
    if s < 0:
        m = int(m) - 1
        s = 60 + s
        if m < 0:
            return '00:00'
    return str(m).rjust(2, '0') + ":" + str(s).rjust(2, '0')

def to_int(time):
    return int(''.join(time.split(':')))

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    cur_pos = pos
    if to_int(op_start) < to_int(cur_pos) and to_int(op_end) > to_int(cur_pos):
        cur_pos = op_end
    for command in commands:
        if command == 'next':
            cur_pos = next(cur_pos)
            if to_int(cur_pos) > to_int(video_len):
                cur_pos = video_len
        if command == 'prev':
            cur_pos = prev(cur_pos)
        if to_int(op_start) <= to_int(cur_pos) and to_int(op_end) >= to_int(cur_pos):
            cur_pos = op_end
    answer = cur_pos
    print(answer)
    return answer
    


# solution("34:33",	"13:00",	"00:55",	"02:55",	["next", "prev"]) # "13:00"
# # solution("10:55",	"00:05",	"00:15",	"06:55",	["prev", "next", "next"])	# "06:55"
# solution("07:22",	"04:05",	"00:15",	"04:07",	["next"]) #  "04:17"

solution("07:22",	"04:10",	"00:15",	"04:07",	["prev", "prev"]) #  "04:17"
