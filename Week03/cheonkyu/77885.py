def solution(numbers): # XOR
    return [((num ^ (num+1)) >> 2) + num + 1 for num in numbers]

# def to_str(n, base):
#   converter = "0123456789ABCDEF"
#   if n < base:
#     return converter[n]
#   else:
#     return to_str(n // base, base) + converter[n % base]
  
# def solution(numbers):
#     answer = []
#     bits_dict = {}
#     for n in numbers:
#         i = n + 1
#         # print(to_str(n, 2))
#         while True:
#             target = 0
#             # print(bits_dict)
#             if i in bits_dict:
#                target = bits_dict[i]
#             else:
#                bits_dict[i] = to_str(i ^ n, 2).count('1')
#                target = bits_dict[i]
            
#             if abs(target) <= 2:
#                answer.append(i)
#                break
#             i += 1
#     print(answer)
#     return answer

solution([15,127,179,3783,819199,9126805503,38588121087,8796093022207,17592186044415])
# [3,11]
# solution([312, 11, 7, 5, 3, 27, 75, 10, 12, 26, 324, 5236])
# print(1000 ^ 1001)
# 110

# [31, 1] [47, 2]
# [10] [11]
# [53214] [53215]
# [4321, 5324, 1111, 444, 666] [4322, 5325, 1115, 445, 667]
# [312, 11, 7, 5, 3, 27, 75, 10, 12, 26, 324, 5236] [313, 13, 11, 6, 5, 29, 77, 11, 13, 27, 325, 5237]