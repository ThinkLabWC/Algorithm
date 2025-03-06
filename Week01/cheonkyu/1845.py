def solution(nums):
    answer = min(len(nums) / 2, len(list(set(nums))))
    return answer

print(len(list(set([1,2,3,3,1,2]))))