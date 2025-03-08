def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
          for k in range(j + 1, len(nums)):
              total = nums[i] + nums[j] + nums[k]
              if is_prime(total):
                  answer += 1
    # print(answer)
    return answer

# a = [1,2,3,4]
# for i in range(0, len(a)):
#   for j in range(i + 1, len(a)):
#     for k in range(j + 1, len(a)):
#       print(a[i], a[j], a[k])

# solution([1,2,3,4])
solution([1,2,7,6,4])