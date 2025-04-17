n = input()

data = []
for _ in range(int(n)):
	data.append((input()))
def solution(data):
    s = set()
    for item in data:
        [a, cmd] = item.split(' ')
        if cmd == 'enter':
            s.add(a)
        else: 
            s.remove(a)
    workers = sorted(list(s), reverse = True)
    for w in workers:
        print(w) 
# solution(['Baha enter', 'Baha leave', 'kam enter', 'kim enter'])
solution(data)