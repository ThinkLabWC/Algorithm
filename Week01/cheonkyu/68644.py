def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):
        for j in range(1, len(numbers)):
            if i != j:
              answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer

solution([2,1,3,4,1]) # [2,3,4,5,6,7]