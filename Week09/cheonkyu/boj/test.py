import heapq
import sys

import heapq

def match(pattern, pos, word):
    for i in range(len(word)):
        if pattern[pos + i] != '?' and pattern[pos + i] != word[i]:
            return False
    return True

def has_no_question(formed, pattern):
    for i in range(len(formed)):
        if pattern[i] == '?' :
            continue
        if pattern[i] != formed[i]:
            return False
    return '?' not in pattern[len(formed):]

def solve(N, M, pattern, words):
    words.sort()  # 사전순 우선 탐색
    heap = []
    heapq.heappush(heap, ("", 0, 0))  # (formed_string, position, used_mask)

    visited = {}

    while heap:
        formed, pos, used = heapq.heappop(heap)

        # if pos == N:
        if pos == N or has_no_question(formed, pattern):
            return formed + pattern[len(formed):]

        key = (pos, used)
        if key in visited and visited[key] <= formed:
            continue
        visited[key] = formed  # 사전순으로 더 빠른 것만 갱신

        for i in range(M):
            if (used >> i) & 1:
                continue
            w = words[i]
            if pos + len(w) > N:
                continue
            if not match(pattern, pos, w):
                continue
            heapq.heappush(heap, (formed + w, pos + len(w), used | (1 << i)))

    return ""


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    pattern = input().strip()
    words = [input().strip() for _ in range(M)]

    result = solve(N, M, pattern, words)
    print(result)

if __name__ == "__main__":
    main()
