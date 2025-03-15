def solution(nums, target):
  R = -1
  answer = 0
  _sum = 0
  for L in range(len(nums)):
    while R + 1 < len(nums) and _sum < target:
      R += 1
      _sum += nums[R]
    if _sum == target:
      answer += 1
    _sum -= nums[L]
    
  print(answer)
      

solution([1, 2, 3, 4, 2, 5, 3, 1, 1, 2], 5)