def solution(nums, target):
  nums.sort()
  L = 0
  R = len(nums) - 1
  print(nums)
  cnt = 0
  while L < R:
    # print(L, R)
    if nums[L] + nums[R] == target:
      cnt += 1
    if nums[L] + nums[R] >= target:
        R -= 1
      # break
    elif nums[L] + nums[R] < target:
      L += 1
  print(cnt)
  # 1
# [1,2,3,4,5,6,], 8
# solution([5, 12, 7, 10, 9, 1, 2, 3, 11], 13)
# solution([1,100,99,2,5], 101)
solution([7, 6, 5, 1, 4], 8)
# [1,4,5,6,7]