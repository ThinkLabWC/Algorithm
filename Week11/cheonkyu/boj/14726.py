n = int(input())
cards = [input().strip() for _ in range(n)]

for card in cards:
    total = 0
    for i in range(len(card)):
        num = int(card[i])
        # 오른쪽에서부터의 인덱스
        idx_from_right = len(card) - i
        if idx_from_right % 2 == 0:  # 짝수 번째(오른쪽에서)
            num *= 2
            if num >= 10:
                num = num // 10 + num % 10
        total += num
    result = 'T' if total % 10 == 0 else 'F'
    print(result)