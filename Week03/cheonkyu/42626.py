import heapq
def solution(scoville, K):
    answer = 0
    if 0 in scoville:
       return -1
    heap = scoville
    heapq.heapify(heap)
    while heap and heap[0] < K:
        # print(heap)
        if len(heap) < 2:
           return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        target = a + (b * 2)
        answer += 1
        if target < K:
          heapq.heappush(heap, target)
          
    # print(answer)
    return answer

solution([1, 2, 3, 9, 10, 12],	7)
