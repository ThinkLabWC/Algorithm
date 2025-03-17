def solution(records):
    answer = []
    user = {}

    chatroom = []
    for record in records:
        row = record.split(' ')
        cmd = row[0]
        id = row[1]
        if cmd == "Enter" or cmd == "Change":
            nickname = row[2]
            user[id] = nickname
        if cmd == "Enter" or cmd == "Leave":
            chatroom.append([cmd, id])

    message = []
    for c in chatroom:
        # print(c[0])
        msg = user[c[1]]
        if c[0] == 'Enter':
            msg += "님이 들어왔습니다."
        if c[0] == 'Leave':
            msg += "님이 나갔습니다."
        message.append(msg)
    answer = message
    # print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
#["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]